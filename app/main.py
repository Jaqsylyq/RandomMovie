from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from app.database import engine, Base
from app.api import movie
from app.models.db_model import Model


app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

app.include_router(movie.router)


@app.get("/api/healthcheck")
async def healthcheck():
    return {'status': True, 'message': 'OK'}


@app.get("/api/docs")
async def get_documentation():
    return get_swagger_ui_html(openapi_url='/api/openapi.json', title='docs')


@app.get("/api/openapi.json")
async def openapi():
    return get_openapi(title='fastapi', version='0.0.1', routes=app.routes)


@app.on_event("startup")
async def start_up():
    engine.connect()


@app.on_event("shutdown")
async def shutdown():
    engine.disconnect()

