import cv2



video = cv2.VideoCapture(0)

while True:
	_,frame = video.read()
	cv2.imshow("RTSP",frame)
	K = cv2.waitKey(1)
	if k == ord('q'):
		break
video.release()
cv2.destroyAllwindows()
