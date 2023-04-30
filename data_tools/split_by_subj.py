"""
Split train, val and test by subject. Make annotation text for mmcls. 
Format: <filename> <label>.
"""

import os
from tqdm import tqdm
import glob
import random

def check_path(path):
    if not os.path.exists(path):
        os.mkdir(path)

# Load data
data_path = 'datasets/micro_doppler_img'
target_path = 'datasets/micro_doppler_subj'
check_path(target_path)
anno_path = os.path.join(target_path, 'anno')
check_path(anno_path)

data_list = glob.glob(os.path.join(data_path, '*.jpg'))
data_list = [data.split('/')[-1] for data in data_list]

subj_data = {}

for data in data_list:
    subj_idx = data.split('_')[1]
    if subj_idx not in subj_data:
        subj_data[subj_idx] = []
    subj_data[subj_idx].append(data)
subj_data = {k: subj_data[k] for k in sorted(subj_data)}
# #samples: [87, 81, 76, 55, 47, 43, 44]

# Split train, val, test
# train: 1,2,3; val: 5,6; test: 4,7

splits = {
    'train': subj_data['1'] + subj_data['2'] + subj_data['3'],  # 244
    'val': subj_data['5'] + subj_data['6'],  # 90
    'test': subj_data['4'] + subj_data['7']  # 99
}

# Create annotation file
def label_img(filename):
    """
    Create human active label. 
    walking 0; running 1; sitting 2; hands 3
    """
    label_dict = {
        'WALKING': '0',
        'RUNNING': '1',
        'SITTING': '2',
        'HANDS': '3'
    }
    return label_dict[filename.split('_')[0]]

for split, file_list in splits.items():
    txt = ""
    for file in tqdm(file_list):
        txt += file + ' ' + label_img(file) + '\n'
    
    with open(os.path.join(anno_path, split + '.txt'), 'w') as ann_f:
        ann_f.write(txt)