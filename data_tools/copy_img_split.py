"""
Copy image according to given split annotation.
"""
import os
import shutil
import glob

anno_path = 'datasets/micro_doppler/anno'
source_path = 'datasets/micro_doppler_img'
target_path = 'datasets/micro_doppler'

annos = glob.glob(os.path.join(anno_path, '*.txt'))

for ann in annos:
    split = ann.split('/')[-1][:-4]
    with open(ann, 'r') as ann_f:
        lines = ann_f.readlines()
        for line in lines:
            image_file = line.split(' ')[0]
            img_fname = image_file.split('/')[-1]
            shutil.copyfile(os.path.join(source_path, image_file), os.path.join(target_path, split, img_fname))
