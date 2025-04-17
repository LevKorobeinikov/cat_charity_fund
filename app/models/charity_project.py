from sqlalchemy import Column, String, Text

from app.constants import MAX_LENGHT
from app.models.base import BaseModel


class CharityProject(BaseModel):
    """
    Моедль для благотворительных проектов:
    """

    name = Column(String(MAX_LENGHT), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self):
        base_repr = super().__repr__()
        return (
            f"{base_repr}, "
            f"name={self.name}, description={self.description!r})"
        )
