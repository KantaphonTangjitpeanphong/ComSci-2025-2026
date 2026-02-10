import cv2 as cv
from ultralytics import YOLO

model = YOLO("yolo11s.pt")
img = cv.imread(0, cv.IMREAD_COLOR)
source = img 
results = model(source, stream=True)
detected_frame = results[0].plot()

cv.imshow("result", detected_frame)
cv.namedWindow("result", cv.WINDOW_NORMAL)
cv.waitKey(0)
cv.destroyAllWindows()
