import cv2
import numpy as np

def detect_color(frame, lower_hsv, upper_hsv):

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    thing = np.where(mask > 0)

    kernel = np.ones((5, 5), np.uint8) 

    img = cv2.bitwise_and(frame, frame, mask=mask)
    img = cv2.erode(img, kernel, iterations=1) 
    img = cv2.dilate(img, kernel, iterations=1) 
    img = cv2.Canny(img, 40, 180) 

    if len(thing) > 0 and len(thing[1]):
        print(thing[0].min(), thing[0].max())
        print(thing[1].min(), thing[1].max()) 

        midPoint = ((thing[1].min()+thing[1].max())//2, (thing[0].min() + thing[0].max()) // 2)
        midPoint2 = (int(thing[1].mean()), int(thing[0].mean()))
        color = (0, 0, 255) 
        color2 = (0, 255, 255)
        cv2.circle(img, midPoint, 7, color, 2)
        cv2.circle(img, midPoint2, 12, color2, 2)

    return img

if __name__ == "__main__":
    #color range (opencv HSV)
    lower_ball = np.array([78, 130, 90])
    upper_ball = np.array([84, 255, 255])

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        result = detect_color(frame, lower_ball, upper_ball)

        cv2.imshow('original', frame)
        cv2.imshow('result', result)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()