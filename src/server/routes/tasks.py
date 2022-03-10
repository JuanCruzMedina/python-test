from typing import List

from fastapi import APIRouter
from starlette import status

from src.server.models.task import Task
from src.server.persistence.database import TASKS

router = APIRouter()


@router.get('/tasks', response_model=List[Task], status_code=status.HTTP_200_OK)
def get_users():
    return TASKS
