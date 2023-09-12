import cv2
import numpy as np

from matplotlib import pyplot as plt

def display(image):
    plt.imshow(image)
    plt.show()

def resizeImage(image, scale):
    h, w, c = image.shape
    height = int(h * scale/100)
    width = int(w * scale/100)
    return cv2.resize(image, dsize=(width, height))

def addImageOverlay(background, foreground, translForeH, translForeW):
    backH, backW, _ = background.shape
    foreH, foreW, _ = foreground.shape
    restH, restW = backH - foreH, backW - foreW

    background = resizeImage(background, 300)

    print(background.shape)
    print(foreground.shape)
    
    crop = background[translForeH : foreH + translForeH, translForeW: foreW + translForeW]

    foregroundGray = cv2.cvtColor(foreground, cv2.COLOR_BGR2GRAY)

    display(foregroundGray)

    '''display(background)
    display(foreground)
    display(crop)'''


def blending(img1, img2, fundo):
    imgA = cv2.imread(img1)
    imgB = cv2.imread(fundo)
    imgB = resizeImage(imgB, 400)
    imgFinal = addImageOverlay(fundo, imgB, 200, 200)

def main():
    imgA = cv2.imread("img/A.jpeg")
    imgB = cv2.imread("img/B.jpeg")

    addImageOverlay(imgA, imgB, 100, 200)


    '''
    alturaA, larguraA, _ = imgA.shape
    imgB = cv2.resize(imgB, (larguraA, alturaA))

    imgAB = cv2.addWeighted(imgA, 0.5, imgB, 0.5, 0)

    alturaAB, larguraAB, _ = imgAB.shape
    imgAB = cv2.resize(imgAB, (int(larguraAB * 0.5), int(alturaAB * 0.5)))

    cv2.imshow(imgAB)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''

main()