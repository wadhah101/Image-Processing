# %%
import cv2
import matplotlib.pyplot as plt
import numpy as np

# %%
def show_images(image : list[np.ndarray]):
    for i in image:
        plt.imshow(i , cmap='gray', vmin=0, vmax=255)
        plt.show()

# %%
img = cv2.imread("./bird.jpg")
img

# %%
# Calculate histograms
hist_red = cv2.calcHist([img],[0],None,[256],[0,256])
hist_green = cv2.calcHist([img],[1],None,[256],[0,256])
hist_blue = cv2.calcHist([img],[2],None,[256],[0,256])

plt.plot(hist_red, color='r')
plt.plot(hist_green, color='g')
plt.plot(hist_blue, color='b')
plt.xlim([0,256])
plt.show()

# %%
red_channel , green_channel , blue_channel = img[:,:,2],  img[:,:,1] , img[:,:,0]

# %%
show_images([red_channel , green_channel , blue_channel])

# %%
def extract_color_threshold(image : np.ndarray , threshold : int) :
    return np.where(image >= threshold , 255  , 0)

show_images([extract_color_threshold(red_channel , 100)])

# %%
image_seuil_red = extract_color_threshold(red_channel , 126)
image_seuil_green = extract_color_threshold(green_channel , 117)
image_seuil_blue = extract_color_threshold(blue_channel , 106)


# %%
def image_seul_rgb_and(image  : np.ndarray, r , g , b ) :
    red_channel , green_channel , blue_channel = image[:,:,2],  image[:,:,1] , image[:,:,0]
    image_seuil_red = extract_color_threshold(red_channel , r)
    image_seuil_green = extract_color_threshold(green_channel , g)
    image_seuil_blue = extract_color_threshold(blue_channel , b)
    result = np.bitwise_and(image_seuil_red , image_seuil_green , image_seuil_blue)

    r = np.repeat(result , 3  , axis=1)
    r = r.reshape(image.shape)
    output = np.where(r == 255 , image , 0)
    return  output

# %%
def image_seul_and(image  : np.ndarray, r , g , b ) :
    red_channel , green_channel , blue_channel = image[:,:,2],  image[:,:,1] , image[:,:,0]
    image_seuil_red = extract_color_threshold(red_channel , r)
    image_seuil_green = extract_color_threshold(green_channel , g)
    image_seuil_blue = extract_color_threshold(blue_channel , b)
    result = np.bitwise_and(image_seuil_red , image_seuil_green , image_seuil_blue)
    return result

# %%
def image_seul_or(image  : np.ndarray, r , g , b ) :
    red_channel , green_channel , blue_channel = image[:,:,2],  image[:,:,1] , image[:,:,0]
    image_seuil_red = extract_color_threshold(red_channel , r)
    image_seuil_green = extract_color_threshold(green_channel , g)
    image_seuil_blue = extract_color_threshold(blue_channel , b)
    result = np.bitwise_or(image_seuil_red , image_seuil_green , image_seuil_blue)
    return result

# %%
show_images([image_seul_or(img , 127 , 117 , 106)])

# %%



