import cv2

video= cv2.VideoCapture(0)
writer= cv2.VideoWriter('E:\output.wmv', cv2.VideoWriter_fourcc(*'MJPG'), 15, (640,480))


while True:
    ret,frame= video.read()
    writer.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

video.release()
writer.release()
cv2.destroyAllWindows()
