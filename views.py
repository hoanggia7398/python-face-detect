from flask import render_template
import cv2

def index():
    return "Welcome to Home page"


def index_tem(name, marks):
    #marks = 80
    capture()
    return render_template('index.html', name=name, marks=marks)


def capture():
    cap = cv2.VideoCapture(0)
    haar = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    while (True):
        try:
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Our operations on the frame come here
            #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            gray = frame
            faces = haar.detectMultiScale(gray, 1.3, 5)

            for face in faces:
                x, y, w, h = face
                cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display the resulting frame
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # When everything done, release the capture
            cap.release()
            cv2.destroyAllWindows()
        except:
            return "fail to turn on"
    return "webcam is on"


def index_for():
    data = {
        'statistics': 70,
        'machine learning': 50,
        'deep learning': 75,
        'python': 20
    }
    return render_template('index_for.html', data=data)
