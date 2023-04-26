"""
Transform .npy file (ndarray) to .jpg image file.
"""
import glob
import os
from PIL import Image
import numpy as np
from tqdm import tqdm

npy_path = 'datasets/micro_doppler_stft'
save_path = 'datasets/micro_doppler_img'

files = glob.glob(os.path.join(npy_path, '*.npy'))
for f in tqdm(files):
    arr = np.load(f) * 255
    arr = arr.astype(np.uint8).T

    img = Image.fromarray(arr)
    img.save(os.path.join(save_path, f.split('/')[-1][:-4] + '.jpg'))
