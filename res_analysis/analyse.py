"""
Analyse results.

Res format:
<List>
    <Dict>
        'pred_label': 0 ~ 4
        'gt_label': 0 ~ 4
        'pred_score': confidence
"""
import pickle

res = pickle.load(open('work_dirs/microD_try/results/out.pkl', 'rb'))

acc_num = 0

for item in res:
    gt = item['gt_label']
    pred = item['pred_label']
    conf = item['pred_score']
    if gt == pred:
        acc_num += 1

    