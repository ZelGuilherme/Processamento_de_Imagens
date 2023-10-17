from cmath import sqrt
import cv2
import glob
from matplotlib import pyplot as plt

def display(image):
    plt.imshow(image)
    plt.show()

def display2(image1, image2):
    fig = plt.figure(figsize=(10,4))
    fig.add_subplot(1, 2, 1)
    plt.imshow(image1)
    plt.title("Imagem Original")

    fig.add_subplot(1, 2, 2)
    plt.imshow(image2)

    plt.show()

def displayHist(hist):
    plt.figure()
    plt.title("Histograma")
    plt.ylabel("N de pixels ")
    plt.plot(hist)
    plt.show()

def displayImgHist(image, flag):
    fig = plt.figure(figsize=(12,4))
    fig.add_subplot(1, 2, 1)
    plt.imshow(image)
    plt.title("Imagem")

    if flag == "gray":
        hist = cv2.calcHist([image], [0], None, [256], [0, 256])
        fig.add_subplot(1, 2, 2)
        plt.title("Histograma")
        plt.ylabel("N de pixels ")
        plt.plot(hist)
    
    elif flag == "rgb":
        colors = ('b', 'g', 'r')
        fig.add_subplot(1, 2, 2)
        plt.title("Histograma")
        plt.ylabel("N de pixels ")
        for i, color in enumerate(colors):
            histogramRGB = cv2.calcHist([image], [i], None, [256], [0, 256])
            plt.plot(histogramRGB, color = color)
            plt.xlim([0, 256])

    plt.show()

def equHistGray(image):
    imageEqu = cv2.equalizeHist(image)
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    imageEqu = cv2.cvtColor(imageEqu, cv2.COLOR_BGR2RGB)

    return [imageGray, imageEqu]

def main():
    imageOneChannel = cv2.imread('images/CAT.jpg', 0)
    imageGray = cv2.cvtColor(imageOneChannel, cv2.COLOR_BGR2RGB)

    imageRGB = cv2.imread('images/CAT.jpg')
    imageRGB = cv2.cvtColor(imageRGB, cv2.COLOR_BGR2RGB)

    #displayImgHist(imageGray, "gray")
    #displayImgHist(imageRGB, "rgb")

    #display2(equHistGray(imageOneChannel)[0], equHistGray(imageOneChannel)[1])

    listaArquivos = glob.glob("compara" + "/*.jpeg")

    #print(listaArquivos)

    imagemS1 = cv2.imread("compara/S1.jpeg", 0)
    histogramaS1 = cv2.calcHist([imagemS1], [0], None, [256], [0, 256])

    comparacoes = {}

    for arquivo in listaArquivos:
        imagemAux = cv2.imread(arquivo, 0)
        histogramaAux = cv2.calcHist([imagemAux], [0], None, [256], [0, 256])

        comaparaCORR = cv2.compareHist(histogramaS1, histogramaAux, cv2.HISTCMP_CORREL)
        comparaCHI = cv2.compareHist(histogramaS1, histogramaAux, cv2.HISTCMP_CHISQR)
        comparaBHA = cv2.compareHist(histogramaS1, histogramaAux, cv2.HISTCMP_BHATTACHARYYA)

        comparaFinal = sqrt((1-comaparaCORR) ** 2 + comparaCHI ** 2 + comparaBHA ** 2)

        comparacoes[arquivo] = comparaFinal

    comparaSorted = sorted(comparacoes, reverse=True)
    print("\nO arquivo " + comparaSorted[0] + " é o mais parecido com a imagem original\n")

main()