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
float 0-1 ： 用來决定準確度\
1 是會 100% 合符才會label\
0 是是 0 % 合符就會label 




