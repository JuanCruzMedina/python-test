from typing import List

from fastapi import APIRouter
from starlette import status

from src.server.models.task import Task
from src.server.repositories.tasks import Repository as TasksRepository

router = APIRouter()


@router.get('/tasks', response_model=List[Task], status_code=status.HTTP_200_OK)
def get_tasks() -> List[Task]:
    """
    Obtiene las tareas.
    :return: Lista de tareas.
    """
    return TasksRepository.get_tasks()
