import numpy as np
import pandas as pd
import joblib
from itertools import combinations
from typing import List

# Load the model and the dataframe
df = pd.read_csv('/mnt/disk1/hojoong/matches/bone.csv').drop(columns=['win', 'score'])
champion_list_empty = {col: 0 for col in df.columns}
model = joblib.load('/mnt/disk1/hojoong/models/test_model.pkl')

def get_best_combination(champions: List[int]):
    combs = combinations(champions, 5)
    best_win_prob = 0.0
    best_comb = []

    for comb in combs:
        input_dict = champion_list_empty.copy()
        for champion in comb:
            input_dict[str(champion)] = 1

        win_prob = model.predict_proba([np.array(list(input_dict.values()))])[0][1]

        if win_prob > best_win_prob:
            best_win_prob = win_prob
            best_comb = comb

    return best_comb, best_win_prob
