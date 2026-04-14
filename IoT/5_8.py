import cv2
classifier = cv2.CascadeClassifier('./haar-cascade-files-master/haarcascade_frontalface_default.xml')
camera = cv2.VideoCapture(0, cv2.CAP_V4L)
camera.set(cv2.CAP_PROP_BUFFERSIZE, 1) 
while True:
	camera.grab( ) 
	ret, image = camera .read( )
	if ret == False:
		continue
	image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	faces = classifier.detectMultiScale(image_gray)
	for x, y, w, h in faces:
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 4)
	cv2.imshow('preview', image) 
	if cv2.waitKey(1) == 27:
		break
camera.release( )
cv2.destroyAllWindows( )