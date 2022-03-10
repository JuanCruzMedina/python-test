import io
import json
import os
from typing import List

from src.server.models.task import Task
from src.server.models.user import User

# Indicamos desde donde se referencian las rutas.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Establecemos una ruta estatica donde buscar los usuarios.
USERS_PATH: str = "../../extra/data/users.json"
TASKS_PATH: str = "../../extra/data/tasks.json"


# Declaracion de constantes que almacenaran los valores de nuestra base de datos falsa.
class Database:
    """
    Base de datos falsa.
    """
    Users: List[User] = []
    Tasks: List[Task] = []


def load(nombre: str, ruta: str, coleccion: List, clase) -> None:
    """
    Permite cargar la base de datos falsa.
    :param nombre: Nombre de la coleccion.
    :param ruta: Ruta del archivo json con los elementos de la coleccion.
    :param coleccion: Coleccion a cargar.
    :param clase: Clase de los elementos dentro de la coleccion.
    """
    print(f'-- Cargango {nombre} ...')
    with io.open(ruta, 'r', encoding='utf8') as jsonFile:
        content = json.load(jsonFile)
        [coleccion.append(clase(**item)) for item in content]


print(f'Usuarios antes de cargar:{len(Database.Users)}')
load('usuarios', USERS_PATH, Database.Users, User)
print(f'Usuarios cargados: {len(Database.Users)}')

print(f'Usuarios antes de cargar:{len(Database.Tasks)}')
load('tareas', TASKS_PATH, Database.Tasks, Task)
print(f'Usuarios cargados: {len(Database.Tasks)}')
