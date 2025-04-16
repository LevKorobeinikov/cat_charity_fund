from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, PositiveInt

from app.constants import FULL_AMOUNT


class DonationCreate(BaseModel):
    full_amount: PositiveInt = Field(example=FULL_AMOUNT)
    comment: Optional[str]


class DonationFullDB(DonationCreate):
    id: int
    user_id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True


class DonationShortDB(DonationCreate):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True
