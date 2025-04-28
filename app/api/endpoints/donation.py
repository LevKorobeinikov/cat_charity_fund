from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud import charity_project_crud, donation_crud
from app.models import User
from app.schemas import DonationCreate, DonationFullDB, DonationShortDB
from app.services.invest import invest

router = APIRouter()


@router.get(
    "/",
    response_model=list[DonationFullDB],
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session),
):
    """
    Только для суперюзеров.
    """
    return await donation_crud.get_multi(session=session)


@router.post(
    "/",
    response_model=DonationShortDB,
    response_model_exclude_none=True,
)
async def create_new_donation(
    donation: DonationCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    """
    Только для авторизованных пользователей.
    """
    new_donation = await donation_crud.create(
        obj_in=donation,
        session=session,
        user=user,
        commit=False,
    )
    active_projects = await charity_project_crud.get_active_objs(session)
    session.add_all(invest(new_donation, active_projects))
    await session.commit()
    await session.refresh(new_donation)
    return new_donation


@router.get(
    "/my",
    response_model=list[DonationShortDB],
    response_model_exclude_none=True,
)
async def get_user_donations(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    """
    Только для авторизованных пользователей.
    """
    return await donation_crud.get_user_donation(session=session, user=user)
