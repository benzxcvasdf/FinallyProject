from ultralytics import YOLO

# Load a model
model = YOLO('C:\\Users\\User\\PycharmProjects\\FinallyProject\\runs\\detect\\train28\\weights\\last.pt')  # load a partially trained model

# Resume training
results = model.train(resume=True)

git filter-branch --tree-filter 'rm -rf runs/detect/train27/weights/last.pt' HEAD