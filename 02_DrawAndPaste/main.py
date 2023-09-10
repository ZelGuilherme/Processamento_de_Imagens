import numpy as np
import cv2
import sys
#from PIL import Image

from matplotlib import pyplot as plt

def drawLine(image, y1, x1, y2, x2):
    #image = cv2.line(image, (y1, x1), (y2, x2), (0, 0, 0), 1)
    image = cv2.polylines(image, (y1, x1), (y2, x2), (0,0,0), 1)

def drawTriangleEmpty(image, coord1, coord2, coord3):
    image = cv2.line(image, coord1, coord2, (0, 0, 0), 5)
    image = cv2.line(image, coord2, coord3, (0, 0, 0), 5)
    image = cv2.line(image, coord3, coord1, (0, 0, 0), 5)

def drawTriangleFilled(image, coord1, coord2, coord3):
    points = np.array([coord1,coord2,coord3])
    cv2.fillPoly(image, [points], (0,0,0))

def crop(image, y, x, height, width):
    newImage = image[y-(height//2):y+(height//2), x-(width//2):x+(width//2)]
    return newImage

def display(image):
    plt.imshow(image)
    plt.show()

def paste(src, dst, y, x):
    src[y:y + dst.shape[0], x:x + dst.shape[1]] = dst

#def getColor(image, y, x, value):
#    return image.item(y, x, value)

def addTones(image, height, width, channel):
    value = 0

    for y in range(0, height):
        for x in range(0, width):
            value = value + image.item(y, x, channel)
    
    return value

def mostColor(image):
    height, width, channels = image.shape
    imgTotal = height*width

    bAverage = addTones(image, height, width, 2)//imgTotal
    gAverage = addTones(image, height, width, 1)//imgTotal
    rAverage = addTones(image, height, width, 0)//imgTotal
    
    print("\nMedia B: ", bAverage, "\nMedia G: ", gAverage, "\nMedia R: ", rAverage, "\n")
    if(bAverage > gAverage and bAverage > rAverage):
        print("\nA imagem e mais azul")
    elif(gAverage > bAverage and gAverage > rAverage):
        print("\nA imagem e mais verde")
    elif(rAverage > bAverage and rAverage > gAverage):
        print("\nA imagem e mais vermelha")
    else:
        print("\nSituacao inesperada")
    

def main():
    img = cv2.imread('C:/sers/14795836698/Documents/Python/Processamento de Imagens/Atividade_02')
    #img = cv2.imread('img/B.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    print("Coordenadas X e Y do primeiro ponto: ")
    coord1 = np.array([int(x) for x in input().split()])
    
    print("Coordenadas X e Y do segundo ponto: ")
    coord2 = np.array([int(x) for x in input().split()])
    
    print("Coordenadas X e Y do terceiro ponto: ")
    coord3 = np.array([int(x) for x in input().split()])
    
    drawTriangleFilled(img, coord1, coord2, coord3)
    #drawTriangleEmpty(img, coord1, coord2, coord3)
    
    imgCrop = crop(img, 165, 390, 200, 200)
    paste(img, imgCrop, 200, 200)

    mostColor(img)

    display(img)


main()
