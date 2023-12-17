import cv2 as cv2

Camera = 0
video = cv2.VideoCapture(Camera)
# for IP cam 
#Camera = "rtps:/Username:Password@IP:554/Straming/Channels/401"
while True:
	_,frame = video.read()
	cv2.imshow("RTSP",frame)
	K = cv2.waitKey(1)
	if k == ord('q'):
		break
video.release()
cv2.destroyAllwindows()