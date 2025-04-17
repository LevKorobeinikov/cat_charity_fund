from datetime import datetime
from typing import Optional

from pydantic import (
    BaseModel,
    Extra,
    Field,
    PositiveInt,
    StrictBool,
    validator,
)

from app.constants import FULL_AMOUNT, MAX_LENGHT, MIN_LENGHT


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(
        ...,
        min_length=MIN_LENGHT,
        max_length=MAX_LENGHT,
    )
    description: Optional[str]
    full_amount: PositiveInt


class CharityProjectUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=MAX_LENGHT)
    description: Optional[str] = Field(None)
    full_amount: Optional[PositiveInt]

    class Config:
        extra = Extra.forbid
        min_anystr_length = MIN_LENGHT
        schema_extra = {
            "example": {
                "name": "Mouse for cats",
                "description": "Cats need it",
                "full_amount": FULL_AMOUNT,
            }
        }

    @validator("name", "description", "full_amount", pre=True, always=True)
    def fields_cannot_be_null(cls, value, field):
        if value is None:
            return value
        if isinstance(value, str) and not value.strip():
            raise ValueError(f"Поле '{field.name}' не может быть пустым!")
        return value


class CharityProjectCreate(CharityProjectUpdate):
    name: str = Field(..., max_length=MAX_LENGHT)
    description: str = Field(...)
    full_amount: PositiveInt


class CharityProjectDB(CharityProjectBase):
    id: int
    invested_amount: int
    fully_invested: StrictBool = Field(..., example=False)
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
