from fastapi import APIRouter

from app.api.endpoints import (
    charity_project_router,
    donation_router,
    google_api_router,
    user_router,
)
from app.constants import (
    CHARITY_PROJECT_PREFIX,
    CHARITY_PROJECT_TAG,
    DONATION_PREFIX,
    DONATION_TAG,
)

main_router = APIRouter()

main_router.include_router(
    charity_project_router,
    prefix=CHARITY_PROJECT_PREFIX,
    tags=[CHARITY_PROJECT_TAG],
)

main_router.include_router(
    donation_router,
    prefix=DONATION_PREFIX,
    tags=[DONATION_TAG],
)
main_router.include_router(
    google_api_router,
    prefix="/google",
    tags=["Google"],
)

main_router.include_router(user_router)
