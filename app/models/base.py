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
        CheckConstraint("full_amount > 0", name="check_full_amount_positive"),
        CheckConstraint(
            "invested_amount >= 0", name="check_invested_amount_non_negative"
        ),
        CheckConstraint(
            "invested_amount <= full_amount",
            name="check_invested_amount_not_exceed_full",
        ),
    )

    def __str__(self):
        return f"""{self.__class__.__name__} (ID: {self.id},
        Full Amount: {self.full_amount})"""
