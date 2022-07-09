import cv2
import pytesseract

def analyze_frame(frame):

    threshold = 170
    gray = True
    black_and_white = False

    if gray:
        grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, threshold, 255, cv2.THRESH_BINARY)

        if black_and_white:
            cv2.imshow('BlackAndWhite', blackAndWhiteImage)
            text = pytesseract.image_to_string(blackAndWhiteImage)

        else:
            cv2.imshow('JustGray', grayImage)
            text = pytesseract.image_to_string(grayImage)
        
        print(text)
    else:
        cv2.imshow('Plain', frame)
        text = pytesseract.image_to_string(frame)
        
        print(text)


def main():
    pass


if __name__ == "__main__":
    main()