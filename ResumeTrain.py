from ultralytics import YOLO

# Load a model
model = YOLO('/Volumes/SanDisk/FCU/FinallyYearProject/FinallyProject/runs/detect/train23/weights/last.pt')  # load a partially trained model

# Resume training
results = model.train(resume=True)