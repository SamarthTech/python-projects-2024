import cv2
cap = cv2.VideoCapture("cars_video.mp4")

while True:
    r, f = cap.read()
    if r == True:
        gry = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
        car = cv2.CascadeClassifier("cars.xml")

        cars = car.detectMultiScale(gry, 1.2, 3)

        for (x, y, w, h) in cars:
            cv2.rectangle(f, (x, y), (x + w, y + h), (0, 0, 255), 3)

        cv2.imshow("wscube", f)
        if cv2.waitKey(25) & 0xff == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()