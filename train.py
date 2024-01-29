
from ultralytics import YOLO
import torch
# 加载一个模型
model = YOLO('yolov8n.yaml')  # 从YAML建立一个新模型
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

# 训练模型 , device=0)

def run():
    torch.multiprocessing.freeze_support()
    results = model.train(data='/Volumes/SanDisk/FCU/FinallyYearProject/FinallyProject/dataset/archive (1)/data.yaml', epochs=10)

if __name__ == '__main__':
    run()