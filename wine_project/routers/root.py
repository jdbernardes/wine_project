from http import HTTPStatus
from fastapi import APIRouter
from wine_project.schemas.schemas import (Message)

router = APIRouter(prefix='/root', tags=['Root'])

@router.get('/', status_code=HTTPStatus.OK, response_model=Message)
async def test_health():
    return {'message': 'Olá Mundo Wine!'}


@router.get('/health', status_code=HTTPStatus.OK, response_model=Message)
async def read_root():
    return {'message': 'API Online'}