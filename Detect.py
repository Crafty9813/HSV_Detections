import cv2
import numpy as np

def detect_color(frame, lower_hsv, upper_hsv):

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    thing = np.where(mask > 0)

    img = cv2.bitwise_and(frame, frame, mask=mask)

    if len(thing) > 0 and len(thing[1]):
        print(thing[0].min(), thing[0].max())
        print(thing[1].min(), thing[1].max()) 

        midPoint = ((thing[1].min()+thing[1].max())//2, (thing[0].min() + thing[0].max()) // 2)
        color = (0, 0, 255) 
        cv2.circle(img, midPoint, 5, color, 2)

    return img

if __name__ == "__main__":
    #color range (HSV)
    lower_blue = np.array([120, 100, 50])  # change for diff color
    upper_blue = np.array([160, 255, 255]) #BLUE

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        result = detect_color(frame, lower_blue, upper_blue)

        cv2.imshow('original', frame)
        cv2.imshow('result', result)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()