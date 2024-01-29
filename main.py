from ultralytics import YOLO
from ultralytics.utils import ASSETS
from ultralytics.models.yolo.detect import DetectionPredictor
import cv2

model = YOLO("/Users/benzxcvasdf/Library/Mobile Documents/com~apple~CloudDocs/FinallyProject/runs/detect/train23/weights/last.pt")
model.predict(source="/Users/benzxcvasdf/Library/Mobile Documents/com~apple~CloudDocs/FinallyProject/testpicture_1.jpg", show=True, save=True) # conf=0.5



