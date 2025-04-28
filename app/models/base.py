from datetime import datetime

from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, Integer

from app.core.db import Base


class BaseModel(Base):
    """
    Абстрактная базовая модель для моделей.
    """

    __abstract__ = True

    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, nullable=False, default=0)
    fully_invested = Column(Boolean, nullable=False, default=False)
    create_date = Column(DateTime, index=True, default=datetime.now)
    close_date = Column(DateTime, index=True)

    __table_args__ = (
        CheckConstraint(
            "full_amount > 0 "
            "AND invested_amount >= 0 AND invested_amount <= full_amount",
            name="check_full_and_invested_amounts",
        ),
    )

    def __repr__(self):
        return (
            f"{type(self).__name__}("
            f"id={self.id}, "
            f"full_amount={self.full_amount}, "
            f"invested_amount={self.invested_amount}, "
            f"fully_invested={self.fully_invested}, "
            f"create_date={self.create_date}, "
            f"close_date={self.close_date})"
        )
