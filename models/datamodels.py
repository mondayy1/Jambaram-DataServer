from pydantic import BaseModel, field_validator
from typing import List, Dict

class Datainput(BaseModel):
    champion_list: List[int] = []
    fixed_list: List[int] = []

    @field_validator('champion_list')
    def check_champion_list_length(cls, v):
        if not (5 <= len(v) <= 12):
            raise ValueError('champion_list must contain between 5 and 12 items')
        return v
    
    @field_validator('fixed_list')
    def check_fixed_list_length(cls, v):
        if not (len(v) <= 4):
            raise ValueError('fixed_list must contain 4 or less items')
        return v
    
class Predictoutput(BaseModel):
    champions: List[int] = []
    main_champ: int
    win_prob: float
    score: float
    

class FeatureImportanceOutput(BaseModel):
    sorted_feature_importance_dict: Dict[str, float] = {}