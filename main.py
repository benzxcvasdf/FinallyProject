from ultralytics import YOLO
from ultralytics.utils import ASSETS
from ultralytics.models.yolo.detect import DetectionPredictor
import cv2

model = YOLO("/Users/benzxcvasdf/Library/Mobile Documents/com~apple~CloudDocs/FinallyProject/runs/detect/train20/weights/best.pt")
model.predict(source="testpicture_1.jpg", show=True, conf=0.5)



