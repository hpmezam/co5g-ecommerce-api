from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.user import UserCreate, UserResponse
from app.schemas.auth import TokenResponse, LoginRequest
from app.services.user_service import create_user
from app.services.auth_service import login_user
from app.auth.dependencies import get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(
    user_data: UserCreate, 
    db: Session = Depends(get_db)
):
    return create_user(db, user_data)

@router.post(
    "/login", 
    response_model=TokenResponse
)
def login(
    data: LoginRequest, 
    db: Session = Depends(get_db)
):
    return login_user(db, data.email, data.password)

@router.get(
    "/me", 
    response_model=UserResponse
)
def get_me(current_user = Depends(get_current_user)):
    return current_user