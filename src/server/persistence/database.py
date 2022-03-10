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
USERS: List[User] = []
TASKS: List[Task] = []


def load(nombre: str, ruta: str, coleccion: List, clase) -> None:
    print(f'-- Cargango {nombre} ...')
    with io.open(ruta, 'r', encoding='utf8') as jsonFile:
        content = json.load(jsonFile)
        [coleccion.append(clase(**item)) for item in content]


print(f'Usuarios antes de cargar:{len(USERS)}')
load('usuarios', USERS_PATH, USERS, User)
print(f'Usuarios cargados: {len(USERS)}')

print(f'Usuarios antes de cargar:{len(TASKS)}')
load('tareas', TASKS_PATH, TASKS, Task)
print(f'Usuarios cargados: {len(TASKS)}')
