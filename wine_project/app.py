from http import HTTPStatus
from fastapi import FastAPI
from wine_project.schemas.schemas import (Message)
from wine_project.routers import wines

app = FastAPI()
app.include_router(wines.router)

@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
async def read_root():
    return {'message': 'Olá Mundo Wine!'}