"""
Split train, val and test. Make annotation text for mmcls. 
Format: <filename> <label>.
"""

import os
from tqdm import tqdm
import glob
import random

data_path = 'datasets/micro_doppler_img'
anno_path = 'datasets/anno'
data_list = glob.glob(os.path.join(data_path, '*.jpg'))
data_list = [data.split('/')[-1] for data in data_list]

"""
433 samples in total. A half of them is 'Walking'. 
"""

full_data = {
    'walking': [data for data in data_list if 'WALKING' in data],  # 222
    'running': [data for data in data_list if 'RUNNING' in data],  # 73
    'sitting': [data for data in data_list if 'SITTING' in data],  # 78
    'hands': [data for data in data_list if 'HANDS' in data],  # 60
}

val_ratio = 0.2
test_ratio = 0.2

splits = {
    'train': [],
    'val': [],
    'test': []
}

random.seed(7)  # reproducable
for k in full_data:
    random.shuffle(full_data[k])
    num = len(full_data[k])
    interval1 = int(num * test_ratio)
    interval2 = int(num * val_ratio) + interval1
    splits['test'] += full_data[k][:interval1]
    splits['val'] += full_data[k][interval1:interval2]
    splits['train'] += full_data[k][interval2:]

# create annotation file

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