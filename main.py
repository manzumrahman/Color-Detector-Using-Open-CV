import cv2
import numpy as np

prev_y = 0

capture = cv2.VideoCapture(0)

lower_blue= np.array([78, 158, 124])
upper_blue = np.array([138, 255, 255])

while True:
    ret, frame = capture.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    contours, hierarachy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        area = cv2.contourArea(c)
        if area > 30:
            x, y, width, height = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+width, y+height), (0, 0, 255), 2)
    cv2.imshow("frame", frame)
    if cv2.waitKey(10) == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()
