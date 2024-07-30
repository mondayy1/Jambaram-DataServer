from fastapi import APIRouter
from models.datamodels import FeatureImportanceOutput
from utils.helpers import get_feature_importance

router = APIRouter()

@router.get('/api/model/champion/feature_importance', response_model=FeatureImportanceOutput)
async def get_Featureimportance():
    FIs = get_feature_importance()
    return {'sorted_feature_importance_dict': FIs}