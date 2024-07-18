import numpy as np
import joblib
import psycopg2
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, conlist, field_validator
from itertools import combinations
import warnings
warnings.filterwarnings(action='ignore')

class Datainput(BaseModel):
    champion_list: List[int] = []
    
    @field_validator('champion_list')
    def check_champion_list_length(cls, v):
        if not (5 <= len(v) <= 12):
            raise ValueError('champion_list must contain between 5 and 10 items')
        return v

class Predictoutput(BaseModel):
    champions: List[int] = []
    win_prob: float

n_champions = 168

app = FastAPI()

champion_list_empty = [0 for i in range(n_champions)]

model = joblib.load('/mnt/disk1/hojoong/models/test_model.pkl')

@app.get('/')
async def root():
    return {'message': 'Hello, this is jambaram.xyz\'s API Server'}

@app.post('/combination', response_model=Predictoutput)
async def get_combination(data_request: Datainput):
    
    champions = data_request.champion_list
    combs = combinations(champions, 5)

    best_win_prob = 0.0
    best_comb = []

    for comb in combs:
        
        input = champion_list_empty
        for champion in comb:
            input[champion] = 1

        win_prob = model.predict_proba([np.array(input)])[0][1]

        if win_prob > best_win_prob:
            best_win_prob = win_prob
            best_comb = comb

    return {'champions': best_comb,'win_prob': float(best_win_prob)}