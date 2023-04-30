"""
Copy image according to given split annotation.
"""
import os
import shutil
import glob


def check_path(path):
    if not os.path.exists(path):
        os.mkdir(path)

anno_path = 'datasets/micro_doppler_subj/anno'
source_path = 'datasets/micro_doppler_img'
target_path = 'datasets/micro_doppler_subj'

annos = glob.glob(os.path.join(anno_path, '*.txt'))

for ann in annos:
    split = ann.split('/')[-1][:-4]
    with open(ann, 'r') as ann_f:
        lines = ann_f.readlines()
        for line in lines:
            image_file = line.split(' ')[0]
            img_fname = image_file.split('/')[-1]
            split_path = os.path.join(target_path, split)
            check_path(split_path)
            shutil.copyfile(os.path.join(source_path, image_file), os.path.join(split_path, img_fname))
