import numpy as np
import pandas as pd
import joblib
from itertools import combinations
from typing import List
from sklearn.preprocessing import MinMaxScaler

# Load the model and the dataframe
df = pd.read_csv('/mnt/disk1/hojoong/matches/bone.csv').drop(columns=['win', 'score'])
features = df.columns
champion_list_empty = {col: 0 for col in df.columns}
model = joblib.load('/mnt/disk1/hojoong/models/test_model.pkl')
model_score = joblib.load('/mnt/disk1/hojoong/models/test_model_score.pkl')

coef_score_dict = dict(zip(features, model_score.coef_))

def get_best_combination(champions: List[int], champions_fixed: List[int]):
    remaining_spots = 5 - len(champions_fixed)
    remaining_champions = [champ for champ in champions if champ not in champions_fixed]
    
    combs = combinations(remaining_champions, remaining_spots)

    best_win_prob = 0.0
    best_comb = []

    for comb in combs:
        full_comb = champions_fixed + list(comb)
        input_dict = champion_list_empty.copy()
        for champion in full_comb:
            input_dict[str(champion)] = 1

        win_prob = model.predict_proba([np.array(list(input_dict.values()))])[0][1]

        if win_prob > best_win_prob:
            best_win_prob = win_prob
            best_input_dict = input_dict
            best_comb = full_comb

    score = model_score.predict([np.array(list(best_input_dict.values()))])[0]
    
    best_coef = coef_score_dict[str(best_comb[0])]
    best_coef_id = best_comb[0]
    for champion in best_comb[1:]:
        if best_coef < coef_score_dict[str(champion)]:
            best_coef = coef_score_dict[str(champion)]
            best_coef_id = champion

    return best_comb, best_coef_id, best_win_prob, (score - 60) * 4

def get_feature_importance():
    scaler = MinMaxScaler()

    feature_importance = model.coef_[0]
    feature_importance_scaled = scaler.fit_transform(np.array(feature_importance).reshape(-1, 1)).flatten()

    importance_dict = dict(zip(features, feature_importance_scaled))
    sorted_feature_importance_dict = dict(sorted(importance_dict.items(), key=lambda item: item[1], reverse=True))

    return sorted_feature_importance_dict

    
