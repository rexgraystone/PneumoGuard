import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import cv2
import os

path = r'C:\\MachineLearning\\2023\\9.PneumoGuard\\'
data_path = r'ZhangLabData\\CellData\\chest_xray'
splits = ['train', 'test']
classes = ['NORMAL', 'PNEUMONIA']
mask_path = r'Mask'
count = 0
for split in splits:
    for index, class_ in enumerate(classes):
        os.chdir(path)
        os.chdir(f'{data_path}\\{split}\\{class_}')
        for filename in os.listdir(os.getcwd()):
            img = cv2.imread(f'{os.getcwd()}\\{filename}')
            img_ = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = cv2.blur(img_, (3, 3)) 
            kernel_x = np.array([[1, 0], [0, -1]])
            kernel_y = np.array([[0, 1], [-1, 0]])
            x = cv2.filter2D(img, -1, kernel_x)
            y = cv2.filter2D(img, -1, kernel_y)
            img = x ** 2 + y ** 2 # Applying Roberts Cross Edge Detector algorithm
            img = np.sqrt(img)
            img = img.astype(np.float64)
            os.chdir(f'{path}')
            os.chdir(f'{mask_path}\\{split}\\{class_}')
            plt.imsave(fname=str(f'{count+1}.jpeg'), arr=img, cmap='gray')
            os.chdir(f'{path}\\{data_path}\\{split}\\{class_}')
            count += 1
print(f'{count} images have been masked.')