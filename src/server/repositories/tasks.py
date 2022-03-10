from typing import List

from src.server.models.task import Task
from src.server.persistence.database import Database as Db


class Repository:
    """
    Respositorio de las tareas.
    """

    @staticmethod
    def get_tasks() -> List[Task]:
        """
        Obtiene todas las tareas.
        :return: Lista de tareas.
        """
        return Db.Tasks
