import cv2
import pytesseract
import numpy as np
import time

def rotate_image_crop(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

def rotate_image(mat, angle):
    """
    Rotates an image (angle in degrees) and expands image to avoid cropping
    """

    height, width = mat.shape[:2] # image shape has 3 dimensions
    image_center = (width/2, height/2) # getRotationMatrix2D needs coordinates in reverse order (width, height) compared to shape

    rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1.)

    # rotation calculates the cos and sin, taking absolutes of those.
    abs_cos = abs(rotation_mat[0,0]) 
    abs_sin = abs(rotation_mat[0,1])

    # find the new width and height bounds
    bound_w = int(height * abs_sin + width * abs_cos)
    bound_h = int(height * abs_cos + width * abs_sin)

    # subtract old image center (bringing image back to origo) and adding the new image center coordinates
    rotation_mat[0, 2] += bound_w/2 - image_center[0]
    rotation_mat[1, 2] += bound_h/2 - image_center[1]

    # rotate image with the new bounds and translated rotation matrix
    rotated_mat = cv2.warpAffine(mat, rotation_mat, (bound_w, bound_h))
    return rotated_mat


def analyze_frame(frame, angle=0):

    # att visa bild funkar typ bara om man också "pausar" med bokstaven "n" (typ)

    threshold = 215
    gray = True
    black_and_white = True
    angle = -5
    #angle = 0

    # Spinna?
    # Högre upplösning
    # "Glid" threshold
    # Prova svart färg

    if gray:
        grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #grayImage = frame

        (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, threshold, 255, cv2.THRESH_BINARY)

        #blackAndWhiteImage = grayImage


        if black_and_white:
            img = rotate_image(blackAndWhiteImage, angle)
            #img = blackAndWhiteImage



            # norm_img = np.zeros((img.shape[0], img.shape[1]))
            # img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
            # img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
            #img = cv2.GaussianBlur(img, (1, 1), 0)


            #img = cv2.bilateralFilter(img, 15*2, 75, 2*75)
            #img = cv2.medianBlur(img, 1)

            # cv2.imwrite("test_images/test.png", img)
            #img = cv2.imread("test_images/entire.png")
            #img = rotate_image_crop(img, -10)

            cv2.imshow('BlackAndWhite', img)
            text = pytesseract.image_to_string(img)

            print(text)


            # Rotera texten rätt! https://pyimagesearch.com/2022/01/31/correcting-text-orientation-with-tesseract-and-python/
            
            # Prova och träna på rotated2.png, se om du kan få den att funka med filtrering

        else:
            img = rotate_image(grayImage, angle)
            #img = grayImage

            cv2.imshow('Gray', img)
            text = pytesseract.image_to_string(img)

            print(text)
        
    else:
        
        img = frame

        #img = cv2.bilateralFilter(img, 15, 75, 75)
        #img = cv2.GaussianBlur(img, (1, 1), 1)
        #img = cv2.medianBlur(img,5)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        img = cv2.Canny(gray, 20*4*2*2, 30*4*2*2)

        img = rotate_image(img, angle)

        cv2.imshow('Plain', img)
        text = pytesseract.image_to_string(img)
        
        print(text)


def main():
    pass

if __name__ == "__main__":
    main()
