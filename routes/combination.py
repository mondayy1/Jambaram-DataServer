from fastapi import APIRouter
from models.datamodels import Datainput, Predictoutput
from utils.helpers import get_best_combination

router = APIRouter()

@router.get('/api/model')
async def root():
    return {'message': 'Hello, this is jambaram.xyz\'s Model API Server'}

@router.post('/api/model/combination', response_model=Predictoutput)
async def get_combination(data_request: Datainput):
    champions = data_request.champion_list
    champions_fixed = data_request.fixed_list
    best_comb, main_champ, best_win_prob, score = get_best_combination(champions, champions_fixed)
    return {'champions': list(best_comb),
            'main_champ': int(main_champ),
            'win_prob': float(best_win_prob),
            'score': float(score)}