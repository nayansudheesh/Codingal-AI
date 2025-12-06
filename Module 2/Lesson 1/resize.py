import cv2
import matplotlib.pyplot as plt

image = cv2.imread('example.jpg')

if image is None:
    print("Error: Image not found or could not be loaded")
else:
    image_rgb = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10,7))
    plt.imshow(image_rgb)
    plt.title("loaded image")
    plt.axis("off")
    plt.show()

    print(f"image properties: {image.shape}")
    