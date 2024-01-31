from ultralytics import YOLO
from ultralytics.utils import ASSETS
from ultralytics.models.yolo.detect import DetectionPredictor
import cv2

model = YOLO("/Volumes/SanDisk/FCU/FinallyYearProject/FinallyProject/runs/detect/train23/weights/best.pt")
model.predict(source="/Volumes/SanDisk/FCU/FinallyYearProject/FinallyProject/testpicture/testpicture_3.png", show=True, save=True) # conf=0.5



