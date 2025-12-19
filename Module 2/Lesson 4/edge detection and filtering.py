import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title , image):
    plt.figure(figsize=(8,8))
    if len(image.shape) == 2:
        plt.imshow(image, cmap="grey")
    else:
        plt.imshow(cv2.cvtColor(image , cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis("off")
    plt.show()

def interactive_edge_detection(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found")
        return
    gray_image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    display_image("Originial grayscale image" , gray_image)

    print("Select an option:")
    print("1. Sobel Edge detection")
    print("2. Canny Edge detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian smoothing")
    print("5. Median filtering")
    print("6. Exit")

    while True:
        choice = input("Enter your choice 1-6")

        if choice == "1":
            soblex = cv2.Sobel(gray_image , cv2.CV_64F , 1 , 0 , ksize=3)
            sobley = cv2.Sobel(gray_image , cv2.CV_64F , 0 , 1 , ksize=3)
            combined_soble = cv2.bitwise_or(soblex.astype(np.uint8), sobley.astype(np.uint8))
            display_image("Sobel edge detection" , combined_soble)
        elif choice == "2":
            print("Adjust thresholds for Canny (Default: 100 and 200)")
            lower_thresh = int(input("Enter lower threshold: "))
            upper_thresh = int(input("Enter Upper threshold: "))
            edges = cv2.Canny(gray_image , lower_thresh , upper_thresh)
            display_image("Canny edge detection" , edges)
        elif choice == "3":
            laplacian = cv2.Laplacian(gray_image , cv2.CV_64F)
            display_image("Laplacian edge detection" , np.abs(laplacian).astype(np.uint8))
        elif choice == "4":
            print("Adjust kernal size for median filtering (must be odd , default:5)")
            kernel_size = int(input("Enter kernel size(odd numbers only):"))
            blurred = cv2.GaussianBlur(image , (kernel_size , kernel_size), 0)
            display_image("Gaussian smoothed image" , blurred)

        elif choice == "5":
            print("Adjust kernal size for median filtering (must be odd , default:5)")
            kernel_size = int(input("Enter kernel size(odd numbers only):"))
            median_filtered = cv2.medianBlur(image , kernel_size)
            display_image("Display gaussian blurred image" , median_filtered)
        
        elif choice == "6":
            print("Exiting")
            break

        else:
            print("Invalid choice , please enter a number between 1 and 6")
        
interactive_edge_detection("example3.jpg")

