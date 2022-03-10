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
USERS: List[User] = []
TASKS: List[Task] = []


def load_users() -> List[User]:
    lista_usuarios: List[User] = []
    print('-- Cargando usuarios ...')
    with io.open(USERS_PATH, 'r', encoding='utf-8') as jsonFile:
        content = json.load(jsonFile)
        for item in content:
            user = User(**item)
            lista_usuarios.append(user)

    return lista_usuarios


def load_tasks() -> List[Task]:
    lista_tareas: List[Task] = []
    print('-- Cargando usuarios ...')
    with io.open(TASKS_PATH, 'r', encoding='utf-8') as jsonFile:
        content = json.load(jsonFile)
        for item in content:
            task = Task(**item)
            lista_tareas.append(task)

    return lista_tareas


print(f'Usuarios antes de cargar:{len(USERS)}')
USERS = load_users()
print(f'Usuarios cargados: {len(USERS)}')

print(f'Usuarios antes de cargar:{len(TASKS)}')
TASKS = load_tasks()
print(f'Usuarios cargados: {len(TASKS)}')
