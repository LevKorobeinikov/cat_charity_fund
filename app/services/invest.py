from datetime import datetime

from app.models.base import BaseModel


def invest(target: BaseModel, sources: list[BaseModel]) -> list[BaseModel]:
    updated = []
    close_date = datetime.now()
    for source in sources:
        transfer = min(
            target.full_amount - target.invested_amount,
            source.full_amount - source.invested_amount,
        )
        for obj in (source, target):
            obj.invested_amount += transfer
            if obj.invested_amount >= obj.full_amount:
                obj.fully_invested = True
                obj.close_date = close_date
        updated.append(source)
        if target.fully_invested:
            break
    return updated
