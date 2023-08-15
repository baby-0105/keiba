from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db
from controllers.users import UsersController


router = APIRouter()

@router.get('/users')
async def get_user(db: Session = Depends(get_db)):
    return UsersController.get_name(db=db)
