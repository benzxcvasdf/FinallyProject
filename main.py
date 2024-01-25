from ultralytics import YOLO
from ultralytics.utils import ASSETS
from ultralytics.models.yolo.detect import DetectionPredictor
import cv2

model = YOLO("yolov8n.pt")
model.predict(source=0, show=True, conf=0.3)



