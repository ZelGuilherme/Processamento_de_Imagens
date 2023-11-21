import cv2
import os, glob
import numpy as np
from matplotlib import pyplot as plt

def display(image):
    plt.imshow(image)
    plt.show()

def limiarType(image, thresh, max, type):
    if type == "binary":
        thresh, image = cv2.threshold(image, thresh, max, cv2.THRESH_BINARY)
        return image
    if type == "binaryInv":
        thresh, image = cv2.threshold(image, thresh, max, cv2.THRESH_BINARY_INV)
        return image
    if type == "trunc":
        thresh, image = cv2.threshold(image, thresh, max, cv2.THRESH_TRUNC)
        return image
    if type == "toZero":
        thresh, image = cv2.threshold(image, thresh, max, cv2.THRESH_TOZERO)
        return image
    if type == "toZeroInv":
        thresh, image = cv2.threshold(image, thresh, max, cv2.THRESH_TOZERO_INV)
        return image

def BGRToRGB(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def displayDouble(tipo, image1, image2, figSizeX, figSizeY):
    fig = plt.figure(figsize=(figSizeX,figSizeY))
    fig.add_subplot(1, 2, 1)
    plt.imshow(image1)
    plt.title("Imagem Original: " + tipo)

    fig.add_subplot(1, 2, 2)
    plt.imshow(image2)
    plt.title("Imagem PGM")

    plt.show()

def displayAllLimiar(image, thresh, max, figSizeX, figSizeY):
    binary = limiarType(image, thresh, max, "binary")
    binaryInv = limiarType(image, thresh, max, "binaryInv")
    trunc = limiarType(image, thresh, max, "trunc")
    toZero = limiarType(image, thresh, max, "toZero")
    toZeroInv = limiarType(image, thresh, max, "toZeroInv")

    fig = plt.figure(figsize=(figSizeX,figSizeY))
    fig.add_subplot(2, 3, 1)
    plt.imshow(image)
    plt.title("Imagem Original")

    fig.add_subplot(2, 3, 2)
    plt.imshow(binary)
    plt.title("Binary")

    fig.add_subplot(2, 3, 3)
    plt.imshow(binaryInv)
    plt.title("Binary Inv")
    
    fig.add_subplot(2, 3, 4)
    plt.imshow(trunc)
    plt.title("Trunc")

    fig.add_subplot(2, 3, 5)
    plt.imshow(toZero)
    plt.title("To Zero")

    fig.add_subplot(2, 3, 6)
    plt.imshow(toZeroInv)
    plt.title("To Zero Inv")

    plt.show()

'''def datasetBinary(thresh, max):
    pathImg = "dataset/data/"
    pathPgm = "dataset/groundtruth"
    imgs = glob.glob(os.path.join(pathImg, '*.jpg'))
    i = 0
    for img in imgs:
        imgs[i] = limiarType(cv2.imread(img), thresh, max, "binary")
        i = i + 1
    
    pgms = glob.glob(os.path.join(pathPgm, '*.pgm'))
    j = 0
    for pgm in pgms:
        pgms[j] = cv2.imread(pgm)
        j = j + 1

    maisSemelhante = ""
    valorMaisSemelhante = 99999999999999999

    aux = 0
    for img in imgs:
        err = mse(imgs[aux], pgms[aux])
        if err < valorMaisSemelhante:
            valorMaisSemelhante = err
            maisSemelhante = aux
        aux = aux + 1
    
    displayDouble("Binary", imgs[maisSemelhante], pgms[maisSemelhante], 14, 8)
    return maisSemelhante, valorMaisSemelhante, imgs[maisSemelhante], pgms[maisSemelhante]

def datasetBinaryInv(thresh, max):
    pathImg = "dataset/data/"
    pathPgm = "dataset/groundtruth"
    imgs = glob.glob(os.path.join(pathImg, '*.jpg'))
    i = 0
    for img in imgs:
        imgs[i] = limiarType(cv2.imread(img), thresh, max, "binaryInv")
        i = i + 1
    
    pgms = glob.glob(os.path.join(pathPgm, '*.pgm'))
    j = 0
    for pgm in pgms:
        pgms[j] = cv2.imread(pgm)
        j = j + 1
    
    maisSemelhante = ""
    valorMaisSemelhante = 99999999999999999

    aux = 0
    for img in imgs:
        err = mse(imgs[aux], pgms[aux])
        if err < valorMaisSemelhante:
            valorMaisSemelhante = err
            maisSemelhante = aux
        aux = aux + 1
    
    displayDouble("BinaryInv", imgs[maisSemelhante], pgms[maisSemelhante], 14, 8)
    return maisSemelhante, valorMaisSemelhante, imgs[maisSemelhante], pgms[maisSemelhante]

def datasetTrunc(thresh, max):
    pathImg = "dataset/data/"
    pathPgm = "dataset/groundtruth"
    imgs = glob.glob(os.path.join(pathImg, '*.jpg'))
    i = 0
    for img in imgs:
        imgs[i] = limiarType(cv2.imread(img), thresh, max, "trunc")
        i = i + 1
    
    pgms = glob.glob(os.path.join(pathPgm, '*.pgm'))
    j = 0
    for pgm in pgms:
        pgms[j] = cv2.imread(pgm)
        j = j + 1
    
    maisSemelhante = ""
    valorMaisSemelhante = 99999999999999999

    aux = 0
    for img in imgs:
        err = mse(imgs[aux], pgms[aux])
        if err < valorMaisSemelhante:
            valorMaisSemelhante = err
            maisSemelhante = aux
        aux = aux + 1
    
    displayDouble("Trunc", imgs[maisSemelhante], pgms[maisSemelhante], 14, 8)
    return maisSemelhante, valorMaisSemelhante, imgs[maisSemelhante], pgms[maisSemelhante]

def datasetToZero(thresh, max):
    pathImg = "dataset/data/"
    pathPgm = "dataset/groundtruth"
    imgs = glob.glob(os.path.join(pathImg, '*.jpg'))
    i = 0
    for img in imgs:
        imgs[i] = limiarType(cv2.imread(img), thresh, max, "toZero")
        i = i + 1
    
    pgms = glob.glob(os.path.join(pathPgm, '*.pgm'))
    j = 0
    for pgm in pgms:
        pgms[j] = cv2.imread(pgm)
        j = j + 1

    maisSemelhante = ""
    valorMaisSemelhante = 99999999999999999

    aux = 0
    for img in imgs:
        err = mse(imgs[aux], pgms[aux])
        if err < valorMaisSemelhante:
            valorMaisSemelhante = err
            maisSemelhante = aux
        aux = aux + 1
    
    displayDouble("ToZero", imgs[maisSemelhante], pgms[maisSemelhante], 14, 8)
    return maisSemelhante, valorMaisSemelhante, imgs[maisSemelhante], pgms[maisSemelhante]

def datasetToZeroInv(thresh, max):
    pathImg = "dataset/data/"
    pathPgm = "dataset/groundtruth"
    imgs = glob.glob(os.path.join(pathImg, '*.jpg'))
    i = 0
    for img in imgs:
        imgs[i] = limiarType(cv2.imread(img), thresh, max, "toZeroInv")
        i = i + 1
    
    pgms = glob.glob(os.path.join(pathPgm, '*.pgm'))
    j = 0
    for pgm in pgms:
        pgms[j] = cv2.imread(pgm)
        j = j + 1

    maisSemelhante = ""
    valorMaisSemelhante = 99999999999999999

    aux = 0
    for img in imgs:
        err = mse(imgs[aux], pgms[aux])
        if err < valorMaisSemelhante:
            valorMaisSemelhante = err
            maisSemelhante = aux
        aux = aux + 1
    
    displayDouble("ToZeroInv", imgs[maisSemelhante], pgms[maisSemelhante], 14, 8)
    return maisSemelhante, valorMaisSemelhante, imgs[maisSemelhante], pgms[maisSemelhante]'''

def dataset(thresh, max, type):
    pathImg = "dataset/data/"
    pathPgm = "dataset/groundtruth"
    imgs = glob.glob(os.path.join(pathImg, '*.jpg'))
    i = 0
    for img in imgs:
        imgs[i] = limiarType(cv2.imread(img), thresh, max, type)
        i = i + 1
    
    pgms = glob.glob(os.path.join(pathPgm, '*.pgm'))
    j = 0
    for pgm in pgms:
        pgms[j] = cv2.imread(pgm)
        j = j + 1

    #maisSemelhante = ""
    listaValorSemelhante = []

    aux = 0
    imgBestMSE = imgs[0]
    pgmBestMSE = pgms[0]
    auxMaisSemelhante = 999999999
    for img in imgs:
        err = mse(imgs[aux], pgms[aux])
        if err < auxMaisSemelhante:
            auxMaisSemelhante = err
            imgBestMSE = imgs[aux]
            pgmBestMSE = pgms[aux]
        listaValorSemelhante.insert(aux, err)
        aux = aux + 1
    
    somaListaSemelhante = sum(listaValorSemelhante)

    return somaListaSemelhante, imgBestMSE, pgmBestMSE

def similarity(imageA, imageB):
    imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    height, width = imageA.shape
    equalPixelAmount = 0
    for y in range(height):
            for x in range(width):
                if imageA[y][x] == imageB[y][x]:
                    equalPixelAmount = equalPixelAmount + 1
                    #print(equalPixelAmount)
    
    #print(equalPixelAmount)
    #print(height * width)
    similarityValue = (equalPixelAmount / (height * width))
    return similarityValue


def mse(imageA, imageB):
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err = err / (float(imageA.shape[0] * imageA.shape[1]))
	
	return err

def printInfo(valRes, thresh, tipo):
    print("\nTipo: " + tipo)
    print("Valor MSE desse Thresh: " + str(valRes))
    print("O melhor Thresh foi: " + str(thresh)) 
    #similaridade = similarity(img, pgm)
    #print(f"Porcentagem de similaridade: {similaridade:.3f}\n")
    #displayDouble(type, img, pgm, 12, 6)

def printInfoPercent(valRes, thresh, tipo, bestImg, bestPgm):
    print("\nTipo: " + tipo)
    print("Valor MSE desse Thresh: " + str(valRes))
    print("O melhor Thresh foi: " + str(thresh)) 
    similaridade = similarity(bestImg, bestPgm)
    print(f"Imagem com melhor semelhanca: {similaridade:.3f}\n")
    displayDouble(tipo, bestImg, bestPgm, 12, 6)

def checkBestThresh(thresh, max, type):
    bestThresh = 999999999999
    auxThresh = 0
    for i in range(len(thresh)):
        somaRes, bestImg, bestPgm = dataset(thresh[i], max, type)
        if somaRes < bestThresh:
            bestThresh = somaRes
            auxThresh = thresh[i]

    return bestThresh, auxThresh, bestImg, bestPgm

def checkAllBestThresh(max, type):
    bestThresh = 999999999999
    auxThresh = 0
    for i in range(255):
        somaRes = dataset(i, max, type)
        if somaRes < bestThresh:
            bestThresh = somaRes
            auxThresh = i

    return bestThresh, auxThresh

def main():
    '''imgGetul = cv2.imread("images/carta_getulio.jpg")
    imgMap1 = cv2.imread("images/mapa1.jpg")
    imgMap2 = cv2.imread("images/mapa2.jpg")
    imgMap3 = cv2.imread("images/mapa3.jpg")

    #display(limiarType(imgGetul, 120, 255, "binaryInv"))

    displayAllLimiar(BGRToRGB(imgGetul), 135, 255, 12, 6)

    displayAllLimiar(BGRToRGB(imgMap1), 180, 255, 12, 6)
    displayAllLimiar(BGRToRGB(imgMap2), 220, 255, 12, 6)
    displayAllLimiar(BGRToRGB(imgMap3), 200, 255, 12, 6)'''

    threshList = [25, 90, 120, 170, 210]
    max = 255

    bestResBinary, threshBinary, bestImgBinary, bestPgmBinary = checkBestThresh(threshList, max, "binary")#checkAllBestThresh(max, "binary")
    printInfoPercent(bestResBinary, threshBinary, "binary", bestImgBinary, bestPgmBinary)

    bestResBinaryInv, threshBinaryInv, bestImgBinaryInv, bestPgmBinaryInv = checkBestThresh(threshList, max, "binaryInv")#checkAllBestThresh(max, "binaryInv")
    printInfoPercent(bestResBinaryInv, threshBinaryInv, "binaryInv", bestImgBinaryInv, bestPgmBinaryInv)

    bestResTrunc, threshTrunc, bestImgTrunc, bestPgmTrunc = checkBestThresh(threshList, max, "trunc")#checkAllBestThresh(max, "trunc")
    printInfoPercent(bestResTrunc, threshTrunc, "trunc", bestImgTrunc, bestPgmTrunc)

    bestResToZero, threshToZero, bestImgToZeroy, bestPgmToZero = checkBestThresh(threshList, max, "toZero")#checkAllBestThresh(max, "toZero")
    printInfoPercent(bestResToZero, threshToZero, "toZero", bestImgToZeroy, bestPgmToZero)

    bestResToZeroInv, threshToZeroInv, bestImgToZeroInv, bestPgmToZeroInv = checkBestThresh(threshList, max, "toZeroInv")#checkAllBestThresh(max, "toZeroInv")
    printInfoPercent(bestResToZeroInv, threshToZeroInv, "toZeroInv", bestImgToZeroInv, bestPgmToZeroInv)

main()