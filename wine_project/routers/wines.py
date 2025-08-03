import pandas as pd
from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from kagglehub.exceptions import KaggleApiHTTPError

from sqlalchemy.orm import Session

from wine_project.database import get_session
from wine_project.data_loaders.dataset_loader import DatasetLoader
from wine_project.data_loaders.generate_validation_data import ValidationData
from wine_project.models.models import Wine, EvaluatedWines
from wine_project.schemas.schemas import Message


router = APIRouter(prefix="/wines", tags=["Wines"])


@router.post("/load_data", status_code=HTTPStatus.CREATED, response_model=Message)
def load_data(session: Session = Depends(get_session)):
    try:
        df = DatasetLoader()
        val_data = ValidationData()
        kwargs = {"sep": ";"}
        raw_data: pd.DataFrame = df.load_data(**kwargs)
        data: pd.DataFrame = val_data.generate_csv(raw_data)

        for _, row in data.iterrows():
            wine = Wine(
                fixed_accidity=row["fixed acidity"],
                volatile_acidity=row["volatile acidity"],
                citric_acid=row["citric acid"],
                residual_sugar=row["residual sugar"],
                chlorides=row["chlorides"],
                free_sulfur_dioxide=row["free sulfur dioxide"],
                total_sulfur_dioxide=row["total sulfur dioxide"],
                density=row["density"],
                pH=row["pH"],
                sulphates=row["sulphates"],
                alcohol=row["alcohol"],
            )
            eval = EvaluatedWines(wine=wine, quality=row["quality"])
            session.add(wine)
            session.add(eval)
            session.commit()
        return {"message": "Data Load Successful"}
    except KaggleApiHTTPError:
        raise HTTPException(
            status_code=403,
            detail="Dataset not available on kaggle to create the DB or you do not have permission",
        )
