import cv2

def analyze_frame(frame):

    threshold = 210

    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, threshold, 255, cv2.THRESH_BINARY)

    cv2.imshow('BlackAndWhite', blackAndWhiteImage)

    




def main():
    pass


if __name__ == "__main__":
    main()