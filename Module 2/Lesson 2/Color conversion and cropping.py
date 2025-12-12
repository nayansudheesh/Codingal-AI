import cv2
import matplotlib.pyplot as plt

image = cv2.imread("example2.jpg")

image_rgb = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB image")
plt.show()

gray_image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image , cmap="grey")
plt.title("Grayscale image")
plt.show()


cropped_image = image[100: 300 , 200:400]
cropped_rgb = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("cropped region")
plt.show()