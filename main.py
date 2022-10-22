import os
import numpy as np

#фунция что бы открыть папку
print(os.listdir("C:\2 ИСХОДНЫЕ СНИМКИ для полигонов\96 kv\RGB"))
#фунция что бы открыть папку и считывает сколько там файлов
with print(os.listdir("C:\2 ИСХОДНЫЕ СНИМКИ для полигонов\96 kv\RGB")) as file:
#массив
array = [row.strip() for row in file]
