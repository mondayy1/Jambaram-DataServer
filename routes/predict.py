from fastapi import APIRouter
from models.datamodels import Datainput, Predictoutput
from utils.helpers import get_best_combination

router = APIRouter()

@router.get('/api')
async def root():
    return {'message': 'Hello, this is jambaram.xyz\'s API Server'}

@router.post('/api/combination', response_model=Predictoutput)
async def get_combination(data_request: Datainput):
    champions = data_request.champion_list
    best_comb, best_win_prob = get_best_combination(champions)
    return {'champions': list(best_comb), 'win_prob': float(best_win_prob)}
