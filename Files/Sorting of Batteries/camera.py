import cv2

def get_frame():
    cap = cv2.VideoCapture(0)  # Change the index if using a different camera
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        yield frame
        cv2.imshow('Camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
