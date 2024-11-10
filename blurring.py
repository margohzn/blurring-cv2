import cv2 

pika = cv2.imread("pika.png")

#copyMakeBorder used to make border
pika_border = cv2.copyMakeBorder(pika, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value = 78) 
#first parameter is the image you want to give border, next 4 is top bottom left right, then border style, and value is color

cv2.imshow("Original Pika", pika_border)
cv2.waitKey(0)

#gaussian blur 
gaussian_image = cv2.GaussianBlur(pika, (7,7), 0)
gaussian_border = cv2.copyMakeBorder(gaussian_image, 10,10,10,10, cv2.BORDER_REFLECT, value = 1)
cv2.imshow("Gaussain blur pika", gaussian_border)
cv2.waitKey(0)

#median blur
median_image = cv2.medianBlur(pika, 5)
cv2.imshow("Median blur pika", median_image)
cv2.waitKey(0)

#bilateral blur
bilateral_image = cv2.bilateralFilter(pika, 9, 30, 30)
cv2.imshow("Bilateral blur pika", bilateral_image)
cv2.waitKey(0)


cv2.destroyAllWindows()