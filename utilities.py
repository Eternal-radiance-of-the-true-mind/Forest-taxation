#использование библиотек и файлов
import os
import cv2
import pandas as pd
import glob
from deepforest import main

def prediction_wrapper(image_path, save_dir ="predictions"):
        
        #Загрузите модель
        model = main.deepforest()
        model.use_release()
        
        # Прогнозирование и сохранение изображения
        prediction = model.predict_image(path = image_path, return_plot=True)
        prediction_name = os.path.basename(os.path.splitext(image_path)[0]) + "_prediction.jpg"
        save_path = os.path.join(save_dir,prediction_name)
        cv2.imwrite(save_path,prediction)
        
        return(save_path)
                
def predict_all_images():
        """
        выполните цикл по каталогу и запустите все изображения, чтобы получить прогнозы ограничивающих рамок
        """
        #чтение конфигурации
        model = main.deepforest()
        model.use_release()
        
        #чтение модели
        tifs = glob.glob("data/evaluation/RGB/*.tif")
        print("{} images found for prediction".format(len(tifs)))
        for tif in tifs:
                file_path = os.path.splitext(tif)[0] + ".csv"
                if not os.path.exists(file_path):
                  print(tif)
                  df = model.predict_image(path = tif, return_plot=False)
                  if df is None:
                          continue
                  #сохранение бокса
                  df.to_csv(file_path)
