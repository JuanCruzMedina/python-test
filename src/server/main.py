
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from src.server.routes.tasks import router as tasks_router
from src.server.routes.test import router as test_router
from src.server.routes.users import router as users_router

app = FastAPI(tittle="Mi Rest API")
app.include_router(test_router, tags=['test'])
app.include_router(users_router, tags=['users'])
app.include_router(tasks_router, tags=['tasks'])


@app.get("/")
def root():
    return RedirectResponse(url='/docs')
