import cv2
from matplotlib import pyplot as plt

def display(image):
    plt.imshow(image)
    plt.show()

def displayDouble(image1, image2, image3, image4, image5, image6, figSizeX, figSizeY):
    fig = plt.figure(figsize=(figSizeX,figSizeY))
    fig.add_subplot(2, 3, 1)
    plt.imshow(image1)
    plt.title("Imagem Média")

    fig.add_subplot(2, 3, 2)
    plt.imshow(image2)
    plt.title("Imagem Gaussiana")

    fig.add_subplot(2, 3, 3)
    plt.imshow(image3)
    plt.title("Imagem Mediana")

    fig.add_subplot(2, 3, 4)
    plt.imshow(image4)
    plt.title("Imagem Sobel")

    fig.add_subplot(2, 3, 5)
    plt.imshow(image5)
    plt.title("Imagem Laplaciana")

    fig.add_subplot(2, 3, 6)
    plt.imshow(image6)
    plt.title("Imagem Canny Edge")

    plt.show()

def BGRToRGB(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def filterAverage(img, ksize1, ksize2):
    img = cv2.blur(img, (ksize1, ksize2))
    return img

def filterGauss(img, ksize1, ksize2):
    img = cv2.GaussianBlur(img,(ksize1,ksize2),cv2.BORDER_DEFAULT) 
    return img

def filterMedian(img, ksize):
    img = cv2.medianBlur(img, ksize)
    return img

def filterSobel(img, ksize):
    img = cv2.Sobel(img, ddepth=-1, dx=1, dy=0, ksize=ksize, scale=1)
    return img

def filterLaplacian(img, ksize):
    img = cv2.Laplacian(img, ddepth=-1, ksize=ksize, scale=1)
    return img

def filterCannyEdge(img, t_lower, t_upper):
    img = cv2.Canny(img, t_lower, t_upper)
    return img

def conv2d(source_image, matrix):
    pass

def main():
    img = cv2.imread("images/02.png")
    img = BGRToRGB(img)
    ksizeA = 5
    ksizeB = 7
    ksizeUnico = 5
    CannyT_upper = 150
    CannyT_lower = 50
    imgAverage = filterAverage(img, ksizeA, ksizeB)
    imgGauss = filterGauss(img, ksizeA, ksizeB)
    imgMedian = filterMedian(img, ksizeUnico)
    imgSobel = filterSobel(img, ksizeUnico)
    imgLaplace = filterLaplacian(img, ksizeUnico)
    imgCannyEdge = filterCannyEdge(img, CannyT_lower, CannyT_upper)
    displayDouble(imgAverage, imgGauss, imgMedian, imgSobel, imgLaplace, imgCannyEdge, 12, 7)

main()