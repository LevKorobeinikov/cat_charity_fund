from typing import Optional

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityRoom(CRUDBase):
    async def get_project_id_by_name(
        self,
        project_name: str,
        session: AsyncSession,
    ) -> Optional[int]:
        result = await session.execute(
            select(self.model.id).where(self.model.name == project_name)
        )
        return result.scalars().first()

    @staticmethod
    async def get_projects_by_completion_rate(session: AsyncSession):
        projects = await session.execute(
            select(CharityProject)
            .where(CharityProject.fully_invested.is_(True))
            .order_by(
                func.extract("year", CharityProject.close_date).desc(),
                func.extract("month", CharityProject.close_date).desc(),
                func.extract("day", CharityProject.close_date).desc(),
                func.extract("hour", CharityProject.close_date).desc(),
                func.extract("minute", CharityProject.close_date).desc(),
                func.extract("second", CharityProject.close_date).desc(),
            )
        )
        return projects.scalars().all()


charity_project_crud = CRUDCharityRoom(CharityProject)
