import cv2

imagePath = "dataset/examples/Holy-Grail.jpg"
img = cv2.imread(imagePath, 0)
img1 = cv2.imread(imagePath, 0)


im2show = cv2.subtract(img, img1)

cv2.imshow('image2show', im2show)
cv2.waitKey(0)
cv2.destroyAllWindows()
