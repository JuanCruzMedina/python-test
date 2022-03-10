import io
import json
import os
from typing import List

from src.server.models.users import User

# Indicamos desde donde se referencian las rutas.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Establecemos una ruta estatica donde buscar los usuarios.
USERS_PATH: str = "../../extra/data/users.json"
USERS: List[User] = []


def load_users() -> List[User]:
    lista_usuarios: List[User] = []
    print('-- Cargando usuarios ...')
    with io.open(USERS_PATH, 'r', encoding='utf-8') as jsonFile:
        content = json.load(jsonFile)
        for item in content:
            user = User(**item)
            lista_usuarios.append(user)

    return lista_usuarios


# if __name__ == '__main__':
print(f'Usuarios antes de cargar:{len(USERS)}')
USERS = load_users()
print(f'Usuarios cargados: {len(USERS)}')
