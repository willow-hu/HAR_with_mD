"""
Split train, val and test. Make annotation text for mmcls. 
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
target_path = 'datasets/micro_doppler_50train'
check_path(target_path)
anno_path = os.path.join(target_path, 'anno')
check_path(anno_path)

data_list = glob.glob(os.path.join(data_path, '*.jpg'))
data_list = [data.split('/')[-1] for data in data_list]

full_data = {
    'walking': [data for data in data_list if 'WALKING' in data],  # 222
    'running': [data for data in data_list if 'RUNNING' in data],  # 73
    'sitting': [data for data in data_list if 'SITTING' in data],  # 78
    'hands': [data for data in data_list if 'HANDS' in data],  # 60
}

# Split train, val, test
val_ratio = 0.25
test_ratio = 0.25

splits = {
    'train': [],
    'val': [],
    'test': []
}

random.seed(666)  # reproducable
for k in full_data:
    random.shuffle(full_data[k])
    num = len(full_data[k])
    interval1 = int(num * test_ratio)
    interval2 = int(num * val_ratio) + interval1
    splits['test'] += full_data[k][:interval1]
    splits['val'] += full_data[k][interval1:interval2]
    splits['train'] += full_data[k][interval2:]

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