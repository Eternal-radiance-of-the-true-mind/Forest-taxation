import os
import PIL
import os.path
import glob
import numpy as np
from PIL import Image

#фунция что бы открыть папку и считывает сколько там файлов
with print(os.listdir("C:\2 ИСХОДНЫЕ СНИМКИ для полигонов\96 kv\RGB")) as file:
#массив
array = [row.strip() for row in file]

#обрезка фото
# Обрезает исходное изображение до 20 * 20 пикселей
def convertjpg(jpgfile,outdir,width=1920,height=1240):
    img=Image.open(jpgfile)
    try:
        new_img=img.resize((width,height),Image.BILINEAR)   
        new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    except Exception as e:
        print(e)
        
# Равномерно разрезать весь формат PNG под этой папкой
for jpgfile in glob.glob('/home/luke/INRIAPerson/neg/*.png'):
        
# создаем папку вывода и выводим туда фото
if not os.path.isdir("foto"):
     os.mkdir("foto")
      convertjpg(jpgfile,'foto')
