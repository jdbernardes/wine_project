import pandas as pd
from http import HTTPStatus

from fastapi import APIRouter

from wine_project.dataset_loader import DatasetLoader
#from wine_project.models.models import Wine
from wine_project.schemas.schemas import Message


router = APIRouter(prefix='/wines', tags=['Wines'])

@router.post('/load_data', status_code=HTTPStatus.CREATED, response_model=Message)
def load_data():
    df = DatasetLoader()
    kwargs = {
        "sep": ";"
    }
    data: pd.DataFrame = df.load_data(**kwargs)
    wines = data.drop(columns='quality')
    #quality = data['quality']
    print(wines)
    return {'message': 'OK'}