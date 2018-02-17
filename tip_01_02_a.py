import cv2
from matplotlib import pyplot as plt
from enchant.checker.CmdLineChecker import color

img = cv2.imread("dataset/examples/life-of-brian2.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow('Always look on the bright side of life', img)
cv2.waitKey(0)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist, color='gray')

imgeq = cv2.equalizeHist(img)
cv2.imshow('Equalized', imgeq)
cv2.waitKey(0)
hist1 = cv2.calcHist([imgeq], [0], None, [256], [0, 256])
plt.plot(hist1, color='gray')

plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()

cv2.destroyAllWindows()
