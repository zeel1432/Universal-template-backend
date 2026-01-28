from fastapi import APIRouter

from app.core.security import create_access_token

router = APIRouter()


@router.post("/login")
async def login():
    return {"access_token": create_access_token("demo-user")}
