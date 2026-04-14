import cv2
faceClassifier = cv2.CascadeClassifier('./haar-cascade-files-master/haarcascade_frontalface_default.xml')
eyeClassifier = cv2.CascadeClassifier('./haar-cascade-files-master/haarcascade_eye.xml')
camera = cv2.VideoCapture(0, cv2.CAP_V4L)
camera.set(cv2.CAP_PROP_BUFFERSIZE, 1) 
while True:
	camera.grab( ) 
	ret, image = camera .read( )
	if ret == False:
		continue
	image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	faces = faceClassifier.detectMultiScale(image_gray)
	eyes = eyeClassifier.detectMultiScale(image_gray)
	for x, y, w, h in faces:
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 4)
	for x, y, w, h in eyes:
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 4)
	cv2.imshow('preview', image) 
	if cv2.waitKey(1) == 27: 
		break
camera.release( )
cv2.destroyAllWindows( )