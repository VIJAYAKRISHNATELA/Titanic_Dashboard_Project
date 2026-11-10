
from pydantic import BaseModel


class DatasetStats(BaseModel):
    total_passengers: int
    survived: int
    not_survived: int
    survival_rate: float
    average_age: float
    average_fare: float
