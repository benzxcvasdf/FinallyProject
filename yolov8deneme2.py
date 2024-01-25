from ultralytics import YOLO
from ultralytics.utils import ASSETS
from ultralytics.models.yolo.detect import DetectionPredictor
import cv2

model = YOLO("deneme.pt")

# model.predict(source="0", show=True, conf=0.5)
# print(model)


model.predict(source="number.png", show=True, conf=0.3)
# if model == '1':
print(model)



