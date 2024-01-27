
from ultralytics import YOLO
import torch
# 加载一个模型
model = YOLO('yolov8n.yaml')  # 从YAML建立一个新模型

# 训练模型 , device=0)

def run():
    torch.multiprocessing.freeze_support()
    results = model.train(data='C:\\Users\\User\\PycharmProjects\\FinallyProject\\dataset\\archive (1)\\data.yaml', epochs=1000, device=0)

if __name__ == '__main__':
    run()