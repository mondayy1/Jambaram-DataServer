from pydantic import BaseModel, Field, field_validator
from typing import List

class Datainput(BaseModel):
    champion_list: List[int] = []

    @field_validator('champion_list')
    def check_champion_list_length(cls, v):
        if not (5 <= len(v) <= 12):
            raise ValueError('champion_list must contain between 5 and 12 items')
        return v

class Predictoutput(BaseModel):
    champions: List[int] = []
    win_prob: float
