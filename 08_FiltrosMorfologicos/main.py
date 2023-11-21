import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

def display(image):
    plt.imshow(image)
    plt.show()

def BGRToRGB(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def getContour(img):
    result = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, (1,1))
    return result

def imgErode(img, kernel, iterations):
    img = cv2.erode(img, kernel, iterations=iterations)
    return img

def imgDilate(img, kernel, iterations):
    img = cv2.dilate(img, kernel, iterations=iterations)
    return img

def createImagesErode(img, kernel, iterations):
    copyImg = img.copy()
    
    incrementAux = 0
    for i in range(10):
        copyImg = imgErode(copyImg, kernel, iterations)
        cv2.imwrite("videoErode/" + str(incrementAux) + ".png", copyImg)
        incrementAux += 1

def createImagesDilate(img, kernel, iterations):
    copyImg = img.copy()
    
    incrementAux = 0
    for i in range(10):
        copyImg = imgDilate(copyImg, kernel, iterations)
        cv2.imwrite("videoDilate/" + str(incrementAux) + ".png", copyImg)
        incrementAux += 1

def createVideos(width, height):
    imageFolderErode = "videoErode/"
    imageFolderDilate = "videoDilate/"

    images = [img for img in os.listdir(imageFolderErode)]

    video = cv2.VideoWriter("VideoErode.avi", 0, 2, (width, height))

    for img in images:
        video.write(cv2.imread(os.path.join(imageFolderErode, img)))

    video.release()

    images = [img for img in os.listdir(imageFolderDilate)]

    video = cv2.VideoWriter("VideoDilate.avi", 0, 2, (width, height))

    for img in images:
        video.write(cv2.imread(os.path.join(imageFolderDilate, img)))

    video.release()

def main():
    img1 = cv2.imread("images/01.png")
    img2 = cv2.imread("images/02.png")
    img3 = cv2.imread("images/03.png")

    kernel = np.ones((3, 3), dtype='uint8')

    #imgBorda = getContour(img1)
    
    imgDeer = imgErode(img2, kernel, 1)
    imgDeer = imgDilate(imgDeer, kernel, 1)

    imgBall = imgDilate(img3, kernel, 1)
    imgBall = imgErode(imgBall, kernel, 2) 

    #display()

    createImagesErode(img1, kernel, 9)
    createImagesDilate(img1, kernel, 7)
    createVideos(460, 386)

main()