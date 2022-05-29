# %%
import cv2
import matplotlib.pyplot as plt
import numpy as np

# %%
img = cv2.imread("./bird.jpg")
img

# %%
# Calculate histograms
hist_red = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_green = cv2.calcHist([img], [1], None, [256], [0, 256])
hist_blue = cv2.calcHist([img], [2], None, [256], [0, 256])

plt.plot(hist_red, color='r')
plt.plot(hist_green, color='g')
plt.plot(hist_blue, color='b')
plt.xlim([0, 256])
plt.show()

# %%
def class_average(cl, start, end):
    niv = np.arange(start, end)
    return np.sum(cl * niv) / np.sum(cl)

def get_variance(hist, s):
    c0 = hist[:s]
    c1 = hist[s:]
    pc0 = np.sum(c0) / np.sum(hist)
    pc1 = np.sum(c1) / np.sum(hist)
    m = class_average(hist, 0, 255)
    m0 = class_average(c0, 0, s)
    m1 = class_average(c1, s, 255)
    return pc0 * (m0 - m)**2 + pc1 * (m1 - m)**2

def otsu_thresholding(hist):
    max_variance = 0
    seuil = 0
    for s in range(1, 254):
        variance = get_variance(hist, s)
        if variance > max_variance:
            max_variance = variance
            seuil = s
    return seuil

otsu_thresholding(hist_blue)

# %%
def class_average(cl, start, end):
    niv = np.arange(start, end)
    return np.sum(cl * niv) / np.sum(cl)

def get_variance(hist, s):
    c0 = hist[:s]
    c1 = hist[s:]
    pc0 = np.sum(c0) / np.sum(hist)
    pc1 = np.sum(c1) / np.sum(hist)
    m = class_average(hist, 0, 255)
    m0 = class_average(c0, 0, s)
    m1 = class_average(c1, s, 255)
    return pc0 * (m0 - m)**2 + pc1 * (m1 - m)**2

def otsu_thresholding(hist):
    max_variance = 0
    seuil = 0
    for s in range(1, 254):
        variance = get_variance(hist, s)
        if variance > max_variance:
            max_variance = variance
            seuil = s
    return seuil

otsu_thresholding(hist_blue)

# %%



