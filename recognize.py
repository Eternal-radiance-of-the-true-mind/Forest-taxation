#используемые библиотеки и файлы
from utilities import *
import matplotlib.pyplot as plt
import cv2
import pandas as pd
import os
import PIL
import os.path
import glob
import numpy as np
from PIL import Image
from os import listdir
from os.path import isfile, join
import numpy


#откуда берем фото 
def test_predict():
    config = read_config()
    model = read_model(config["model_path"], config)
    image = predict_image(image_path="C:/Users/alakh/Downloads/TreeDemo-master/upload/gettyimages-908-47-640x640.jpg",model=model,return_plot=True)

    plt.imshow(image[:,:,::-1])
    plt.show()

#test_predict()

#путь вывода обработанной фотографии
mypath='D:/Download/Aviahack_2022/SPB_TKUIK/upload/'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = numpy.empty(len(onlyfiles), dtype=object)

for n in range(0, len(onlyfiles)):
  images[n] = cv2.imread( join(mypath,onlyfiles[n]) )

for i in onlyfiles:
    csv_path = prediction_wrapper(image_path="{}" .format(join(mypath,i)))

