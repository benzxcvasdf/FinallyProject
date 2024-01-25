# TEST FOR YOLOV8 ING

## 安裝 YOLOV8

```angular2html
pip install ultralytics
```
## 導入 YOLOV8

```angular2html
from ultralytics import YOLO
```

## 用來啟動偵測

```angular2html
model.predict(source="number.png", show=True, conf=0.3)
```
#### source:
- 0 ＝ 視像鏡頭
- number.png ＝ 名為number 的 PNG 檔

#### conf:

