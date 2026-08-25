#CNN(Convolution NEural Network)
#A Convolutional Neural Network (CNN) is a deep learning algorithm mainly used for #image processing and computer vision tasks such as image classification, object #detection, facial recognition, and medical image analysis.

#CNN automatically learns important features (edges, shapes, textures, objects) from #images without manual feature extraction.
#Input Image
     
#Convolution Layer
     
#Activation Function (ReLU)
     
#Pooling Layer
     
#Fully Connected Layer
     
#Output Layer

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Give Image path
image_path = r"C:\Users\3328458\Desktop\DL\SUNFLOWER.jpg"

# Read image
img = Image.open(image_path).convert('L')
image = np.array(img)

# Edge detection kernel
kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

# Convolution
rows, cols = image.shape
k = kernel.shape[0]

output = np.zeros((rows-k+1, cols-k+1))

for i in range(rows-k+1):
    for j in range(cols-k+1):
        region = image[i:i+k, j:j+k]
        output[i, j] = np.sum(region * kernel)

# Display images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(output, cmap='gray')
plt.title("CNN Feature Map")

plt.show()