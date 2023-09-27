import matplotlib.pyplot as plt
from skimage import io
from skimage.color import rgb2gray
from skimage.util import img_as_ubyte


rgb_image = io.imread("house_island.jpg") #Enter Your RGB Image Here
gray_image = rgb2gray(rgb_image)

#Axes
fig, axes = plt.subplots(1, 2, figsize=(16, 8))
ax = axes.ravel()
ax[0].imshow(rgb_image)
ax[0].set_title("Original Image")
ax[1].imshow(gray_image, cmap=plt.cm.gray)
ax[1].set_title("Grayscale Image")
fig.tight_layout()

#Save Place
save_gray_image = input("Do you want to also save the grayscale image? (yes/no): ").strip().lower()
gray_image_8bit = img_as_ubyte(gray_image)
if save_gray_image == 'yes':
    io.imsave("gray_image.jpg", gray_image_8bit)

#Remove numeric labels on the axes
ax[0].set_xticks([])
ax[0].set_yticks([])
ax[1].set_xticks([])
ax[1].set_yticks([])

#pltshow
plt.show()
