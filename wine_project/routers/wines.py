import pandas as pd
from http import HTTPStatus

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from wine_project.database import get_session
from wine_project.dataset_loader import DatasetLoader
from wine_project.models.models import Wine, EvaluatedWines
from wine_project.schemas.schemas import Message


router = APIRouter(prefix='/wines', tags=['Wines'])

@router.post('/load_data', status_code=HTTPStatus.CREATED, response_model=Message)
def load_data(session: Session = Depends(get_session)):
    df = DatasetLoader()
    kwargs = {
        "sep": ";"
    }
    data: pd.DataFrame = df.load_data(**kwargs)
    try:
        for _, row in data.iterrows():
            wine = Wine(
                fixed_accidity= row['fixed acidity'],
                volatile_acidity= row['volatile acidity'],
                citric_acid= row['citric acid'],
                residual_sugar= row['residual sugar'],
                chlorides= row['chlorides'],
                free_sulfur_dioxide= row['free sulfur dioxide'],
                total_sulfur_dioxide= row['total sulfur dioxide'],
                density= row['density'],
                pH= row['pH'],
                sulphates= row['sulphates'],
                alcohol= row['alcohol']
            )
            eval = EvaluatedWines(
                wine = wine,
                quality = row['quality']
            )
            session.add(wine)
            session.add(eval)
            session.commit()
    except Exception as e:
        session.rollback()
        print(f"Failed to insert wines: {e}")
        raise
    return {'message': 'OK'}