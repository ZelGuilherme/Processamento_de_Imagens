import numpy as np
import cv2
import sys

from matplotlib import pyplot as plt


def rescaleImage(image):
    h, w, c = image.shape
    print(image.shape)
    return cv2.resize(image, dsize=(h//2, w//2))


'''def printInfo(image):
    print(f"\nwidth: {imgWidth}\nheight: {imgHeight}")
    print("Channels:", img.shape)
    print(sys.getsizeof(img), "bytes")'''


img = cv2.imread('img/1.png')
imgHeight, imgWidth, imgChannel = img.shape

newImg = rescaleImage(img)#, 600, 300)
newImgHeight, newImgWidth, newImgChannel = newImg.shape

print(f"\nHeight: {imgHeight}\nWidth: {imgWidth}")
print("Channels:", img.shape)
print(sys.getsizeof(img), "bytes")

print(f"\nHeight: {newImgHeight}\nWidth: {newImgWidth}")
print("Channels:", newImg.shape)
print(sys.getsizeof(newImg), "bytes")


imgVazia = np.zeros((300,600,3), dtype=np.uint8)

imgVazia[:,0:200] = (255,0,0)
imgVazia[:,200:400] = (0,0,255)
imgVazia[:,400:600] = (0,255,0)
'''
print("Informacoes sobre os pixels:\n")
for x in range(imgVazia.shape[1]):
    for y in range(imgVazia.shape[0]):
        k = imgVazia[y, x]
        print(k.dtype)'''

#k = imgVazia[]
print("\nTipo de pixels:", imgVazia.dtype)
print(sys.getsizeof(imgVazia), "bytes")
imgVazia = cv2.cvtColor(imgVazia, cv2.COLOR_BGR2RGB)

#imgConc = np.concatenate((imgVazia,newImg), axis=1)

plt.imshow(img)
plt.show()

plt.imshow(newImg)
plt.show()

#plt.imshow(imgVazia)
#plt.show()

#plt.imshow(imgConc)
#plt.show()