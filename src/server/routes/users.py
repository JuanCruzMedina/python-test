from typing import List

from fastapi import APIRouter
from starlette import status

from src.server.models.user import User
from src.server.repositories.users import Repository as UsersRepository

router = APIRouter()


@router.get('/users', response_model=List[User], status_code=status.HTTP_200_OK)
def get_users() -> List[User]:
    """
    Obtiene los usuarios.
    :return: Lista de usuarios.
    """
    return UsersRepository.get_users()
