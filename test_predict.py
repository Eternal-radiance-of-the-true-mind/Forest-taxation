#test image prediction for debugging
from utilities import *
import matplotlib.pyplot as plt
import cv2
import pandas as pd

def test_predict():
    config = read_config()
    model = read_model(config["model_path"], config)
    image = predict_image(image_path="/Users/ben/Downloads/gettyimages-908-47-640x640.jpg",model=model,return_plot=True)

    plt.imshow(image[:,:,::-1])
    plt.show()

#test_predict()
raw_image = cv2.imread("C:/Users/101/Downloads/forest-taxation/TreeDemo-master/upload/tree.JPG")
csv_path = prediction_wrapper(image_path="C:/Users/101/Downloads/TreeDemo-master/forest-taxation/predictions/tree.JPG")
boxes = pd.read_csv(csv_path)
print(boxes)