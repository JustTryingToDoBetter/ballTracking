import cv2

capture = cv2.VideoCapture("openCVproject/videos/video.mp4")

while capture.isOpened():

    _, img1 = capture.read()
    _, img2 = capture.read()

    diff = cv2.absdiff(img1, img2)

    diff_gray = cv2.cvtColor(diff, cv2. COLOR_BGR2GRAY)

    diff_blur = cv2.GaussianBlur(diff_gray, (5,5), 0)


    _, thresh_bin = cv2.threshold(diff_blur, 20, 255, 
                                cv2.THRESH_BINARY)

    contours , hierarchy = cv2.findContours(thresh_bin, 
                                            cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)


    for contour in contours:
        x,y,w,h = cv2.boundingRect(contour)
        if cv2.contourArea(contour) > 300:
            cv2.rectangle(img1, (x,y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow("detecting ball" , img1)
    if cv2.waitKey(100) == 13:
        exit()
