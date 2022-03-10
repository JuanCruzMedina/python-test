
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from src.server.routes.test import router as test_router

app = FastAPI(tittle="Mi Rest API")
app.include_router(test_router, tags=['test'])


@app.get("/")
def root():
    return RedirectResponse(url='/docs')
