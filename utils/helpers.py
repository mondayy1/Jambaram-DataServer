import numpy as np
import pandas as pd
import joblib
from itertools import combinations
from typing import List

# Load the model and the dataframe
df = pd.read_csv('/mnt/disk1/hojoong/matches/bone.csv').drop(columns=['win', 'score'])
champion_list_empty = {col: 0 for col in df.columns}
model = joblib.load('/mnt/disk1/hojoong/models/test_model.pkl')

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
            best_comb = full_comb

    return best_comb, best_win_prob
