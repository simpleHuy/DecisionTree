import json
import pandas as pd
from sklearn.model_selection import train_test_split


def get_stratified_split():
    with open('heart_disease_dataset/heart_disease.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)
    for cell in nb['cells']:
        if cell.get('cell_type') == 'code':
            src = ''.join(cell['source'])
            if 'def stratified_split' in src:
                globals_dict = {'train_test_split': train_test_split}
                exec(src, globals_dict)
                return globals_dict['stratified_split']
    raise RuntimeError('stratified_split not found')


def test_stratified_split_preserves_distribution():
    stratified_split = get_stratified_split()
    X = pd.DataFrame({'feature': range(10)})
    y = pd.Series([0]*5 + [1]*5)
    X_train, X_test, y_train, y_test = stratified_split(X, y, train_size=0.6, random_state=0)
    assert len(X_train) == 6
    assert len(X_test) == 4
    assert y_train.value_counts().to_dict() == {0: 3, 1: 3}
    assert y_test.value_counts().to_dict() == {0: 2, 1: 2}
