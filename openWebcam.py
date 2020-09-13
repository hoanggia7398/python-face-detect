import cv2

cap = cv2.VideoCapture(0)
haar = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
cv2.namedWindow("preview")
ret, frame = cap.read()

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if frame is not None:   
        cv2.imshow("preview", frame)

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray = frame
    faces = haar.detectMultiScale(gray, 1.3, 5)

    for face in faces:
        x, y, w, h = face
        cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('preview', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()