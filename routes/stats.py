from fastapi import APIRouter
from models.datamodels import StatCombinationOutput
from utils.dbclient import db_get_comb

router = APIRouter()

@router.get('/api/model/stats/best_win_all', response_model=StatCombinationOutput)
async def get_best_win_all():
    champions, value = db_get_comb('win', 'alltime')
    return {'champions': champions, 'value': value}

@router.get('/api/model/stats/best_win_today', response_model=StatCombinationOutput)
async def get_best_win_today():
    champions, value = db_get_comb('win', 'today')
    return {'champions': champions, 'value': value}

@router.get('/api/model/stats/best_score_all', response_model=StatCombinationOutput)
async def get_best_score_all():
    champions, value = db_get_comb('score', 'alltime')
    return {'champions': champions, 'value': value}

@router.get('/api/model/stats/best_score_today', response_model=StatCombinationOutput)
async def get_best_score_today():
    champions, value = db_get_comb('score', 'today')
    return {'champions': champions, 'value': value}