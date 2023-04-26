import os
from tqdm import tqdm
import glob
import random

data_path = 'datasets/micro_doppler_stft'
data_list = glob.glob(os.path.join(data_path, '*.npy'))
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

train = []
val = []
test = []

random.seed(7)  # reproducable
for k in full_data:
    random.shuffle(full_data[k])
    num = len(full_data[k])
    interval1 = int(num * test_ratio)
    interval2 = int(num * val_ratio) + interval1
    test = test + full_data[k][:interval1]
    val = val + full_data[k][interval1:interval2]
    train = train + full_data[k][interval2:]

a=1