import cv2
img = cv2.imread("cars.jpg")
gry = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
car = cv2.CascadeClassifier("cars.xml")
cars = car.detectMultiScale(gry,1.1,1)
for (x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

cv2.imshow("wscude",img)
cv2.waitKey(0)
cv2.destroyAllWindows()