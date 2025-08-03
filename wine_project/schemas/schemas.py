from pydantic import BaseModel
from typing import List


class Message(BaseModel):
    message: str


class WineSchema(BaseModel):
    id: int
    fixed_accidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

class WinesDashboard(BaseModel):
    wines: List[WineSchema]