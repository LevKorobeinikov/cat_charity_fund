from sqlalchemy import Column, ForeignKey, Integer, Text

from app.constants import USER_ID
from app.models.base import BaseModel


class Donation(BaseModel):
    """
    Модель для пожертований:
    """

    user_id = Column(Integer, ForeignKey(USER_ID), nullable=False)
    comment = Column(Text)

    def __repr__(self):
        base_repr = super().__repr__()
        return (
            f"{base_repr}, "
            f"user_id={self.user_id}, comment={self.comment!r})"
        )
