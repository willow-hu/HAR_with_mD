import os
import numpy as np
from PIL import Image
from torchvision import transforms

# Crop
def crop_img(img):
    crop_transform = transforms.RandomCrop((59, 256))
    cropped = crop_transform(img)
    return cropped

def pad_img(img):
    input_array = np.array(img)
    current_width = input_array.shape[1]
    desired_width = 256
    padding_needed = desired_width - current_width
    padding_left = padding_needed // 2
    padding_right = padding_needed - padding_left
    output_array = np.pad(input_array, ((0, 0), (padding_left, padding_right), (0, 0)), mode='constant')
    return output_array

