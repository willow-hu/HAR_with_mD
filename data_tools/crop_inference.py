import os
import glob
import numpy as np
from PIL import Image
import torch
from torchvision import transforms

# import mmcv
# from mmpretrain.datasets.transforms import RandomCrop

# cropper = RandomCrop(crop_size=(59, 256), pad_if_needed=True)

# Crop
def crop_img(img):
    img_tensor = torch.tensor(np.array(img))
    crop_transform = transforms.RandomCrop((59, 256))
    cropped = crop_transform(img_tensor)
    return np.array(cropped)

def pad_img(image):
    input_array = np.array(image)
    current_width = input_array.shape[1]
    desired_width = 256
    padding_needed = desired_width - current_width
    padding_left = padding_needed // 2
    padding_right = padding_needed - padding_left
    output_array = np.pad(input_array, ((0, 0), (padding_left, padding_right)), mode='constant')
    return output_array

sample_path = 'datasets/micro_doppler_subj/test'

files = glob.glob(os.path.join(sample_path, '*.jpg'))
for img_file in files:
    image = Image.open(img_file)
    if image.width < 256:
        output_array = pad_img(image)
    else:
        output_array = crop_img(image)
    
    output_image = Image.fromarray(output_array)

    # Save the output image
    output_image.save(img_file)
