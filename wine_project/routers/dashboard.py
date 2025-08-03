import pandas as pd
from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import Select
from wine_project.database import get_session
from wine_project.schemas.schemas import Message, WinesDashboard
from wine_project.models.models import Wine, EvaluatedWines


router = APIRouter(prefix="/dash", tags=["Dashboards"])

@router.get("/wines", status_code=HTTPStatus.CREATED, response_model=WinesDashboard)
def read_wines(session: Session = Depends(get_session)):
    wines = session.scalars(
        Select(Wine)
    ).all()
    return {'wines':wines}
