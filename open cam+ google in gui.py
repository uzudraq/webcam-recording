import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import *


def opencam():
    import cv2

    video = cv2.VideoCapture(0)
    writer = cv2.VideoWriter('E:\output.wmv', cv2.VideoWriter_fourcc(*'MJPG'), 15, (320, 280))

    while True:
        ret, frame = video.read()
        writer.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
#  press esc for stopping the cam
    video.release()
    writer.release()
    cv2.destroyAllWindows()


def openwebbroweser():
    import webbrowser
    webbrowser.open("http://google.com")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(400, 300)
    w.setWindowTitle("noobs")

    app.setStyle("Fusion")

    qp = QPalette()
    qp.setColor(QPalette.ButtonText, Qt.black)
    qp.setColor(QPalette.Window, Qt.white)
    qp.setColor(QPalette.Button, Qt.gray)
    app.setPalette(qp)

    line = QLineEdit()


    btn1 = QPushButton("google")
    btn2 = QPushButton("open camera")
    btn1.clicked.connect(openwebbroweser)
    btn2.clicked.connect(opencam)

    hbox = QHBoxLayout(w)

    hbox.addWidget(btn1)
    hbox.addWidget(btn2)

    w.show()
    sys.exit(app.exec_())
