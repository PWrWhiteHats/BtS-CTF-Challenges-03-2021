import keras
import cv2
import numpy as np
import os
import sys
import shutil
import random
import re
from tqdm import tqdm

import warnings
warnings.filterwarnings("ignore")

class Predict:
    def __init__(self, path):
        self.path = path

    def load_model(self):
        self.loaded_model = keras.models.load_model(self.path)
        return self.loaded_model
    
    def get_the_flag(self, folder):
        images_files = os.listdir(folder)
        images_number = len(images_files)	
    
        flag_bin = []

        for index in tqdm(range(images_number)):
            f = os.path.join(folder, f"{index}.jpg")
            img = cv2.imread(f)

            img = cv2.resize(img, (64, 64))
            img = np.reshape(img, [1, 64, 64, 3])
            predictions =  self.loaded_model.predict_classes(img)

            if predictions == 0:
                flag_bin.append(0)
            elif predictions == 1:
                flag_bin.append(1)

        result = ''.join(map(str, flag_bin))

        return result

    def create_flag_from_model(self, flag, images, flag_directory):
        binary = string_2_bin(flag)
        all_images = [os.path.join(images, f) for f in os.listdir(images) if os.path.isfile(os.path.join(images, f)) and f.endswith('.jpg')]
        random.shuffle(all_images)        

        all_images = all_images[:2*len(binary)]

        classifier = {'0': [], '1': []} 

        for i, f in tqdm(enumerate(all_images)):
            img = cv2.imread(f)
            if img is not None:
                img = cv2.resize(img, (64, 64))
                img = np.reshape(img, [1, 64, 64, 3])
                predictions = self.loaded_model.predict_classes(img)

                if predictions == 0:
                    classifier['0'].append(f)
                elif predictions == 1:
                    classifier['1'].append(f)

        flag_images = []
        flag_letters = []

        for letter in binary:
            image_path = random.choice(classifier[letter])
            # classifier[letter].remove(image_path) #Uncomment this if you want you images to be unique
            flag_images.append(image_path)
            flag_letters.append(letter)
        
        assert len(binary) == len(flag_letters)
        flag_str_from_images = ''.join(map(str, flag_letters))
        assert binary == flag_str_from_images

        if not os.path.exists(flag_directory):
            os.makedirs(flag_directory)

        for index, f in enumerate(flag_images):
            shutil.copy(f, os.path.join(flag_directory, f'{index}.jpg'))
