from typing import List

from src.server.models.user import User
from src.server.persistence.database import Database as Db


class Repository:
    """
    Respositorio de los usuarios.
    """

    @staticmethod
    def get_users() -> List[User]:
        """
        Obtiene todos los usuarios.
        :return: Lista de usuarios.
        """
        return Db.Users
