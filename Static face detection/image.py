import cv2
img = cv2.imread("students.jpg")
gry = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces = face.detectMultiScale(gry,1.1,1)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

cv2.imshow("wscude",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
