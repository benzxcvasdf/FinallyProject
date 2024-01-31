import cv2
import numpy as np
import time
from ultralytics import YOLO

model = YOLO('yolov8n-seg.pt')

# video_path = "cars.MOV"
cap = cv2.VideoCapture(1)

while cap.isOpened():

    success, frame = cap.read()

    if success:
        start = time.perf_counter()

        results = model(frame)

        end = time.perf_counter()
        total_time = end - start


