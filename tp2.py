# %%
import cv2
import matplotlib.pyplot as plt
import numpy as np

# %%
img = cv2.imread("./city.jpg", cv2.IMREAD_GRAYSCALE)
img

# %%
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()

# %%
hist, bins = np.histogram(img.flatten(), 256, [0, 256])
hist

# %%
plt.plot(range(256), hist)
plt.xlabel('niveau de gris')
plt.show()

# %%
# histogramme cumulé
hist_cum = hist.cumsum()
hist_cum

# %%
# égalisation d'histogramme
equ = cv2.equalizeHist(img)
plt.imshow(equ, cmap='gray', vmin=0, vmax=255)
plt.show()

# %%
# transformation linéaire
lin_img = (img - img.min()) / (img.max() - img.min())
lin_img = lin_img * 255
plt.imshow(lin_img, cmap='gray', vmin=0, vmax=255)
plt.show()

# %%



