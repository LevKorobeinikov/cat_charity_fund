from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (
    check_charity_project_before_edit,
    check_charity_project_exists,
    check_charity_project_is_not_invested,
    check_charity_project_name_uniqueness,
)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud import charity_project_crud, donation_crud
from app.schemas import (
    CharityProjectCreate,
    CharityProjectDB,
    CharityProjectUpdate,
)
from app.services.invest import invest

router = APIRouter()


@router.get(
    "/",
    response_model=list[CharityProjectDB],
    response_model_exclude_none=True,
)
async def get_all_charity_projects(
    session: AsyncSession = Depends(get_async_session),
):
    return await charity_project_crud.get_multi(session=session)


@router.post(
    "/",
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def create_new_charity_project(
    project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Только для суперюзеров.
    """
    await check_charity_project_name_uniqueness(project.name, session)
    new_charity_project = await charity_project_crud.create(
        obj_in=project,
        session=session,
        commit=False,
    )
    session.add_all(
        invest(
            new_charity_project,
            await donation_crud.get_active_objs(session),
        )
    )
    await session.commit()
    await session.refresh(new_charity_project)
    return new_charity_project


@router.patch(
    "/{project_id}",
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def partially_update_charity_project(
    project_id: int,
    update_data: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Только для суперюзеров.
    """
    charity_project = await check_charity_project_exists(project_id, session)
    check_charity_project_before_edit(charity_project, update_data)
    if update_data.name is not None:
        await check_charity_project_name_uniqueness(update_data.name, session)
    return await charity_project_crud.update(
        db_obj=charity_project,
        obj_in=update_data,
        session=session,
    )


@router.delete(
    "/{project_id}",
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def delete_charity_project(
    project_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Только для суперюзеров.
    """
    charity_project = await check_charity_project_exists(project_id, session)
    check_charity_project_is_not_invested(charity_project)
    return await charity_project_crud.remove(charity_project, session)
