# %%
import random

import cv2
import matplotlib.pyplot as plt
import numpy as np

# %%
img = cv2.imread("./cat.jpg", cv2.IMREAD_GRAYSCALE)

# %%
img

# %%
highestColor = max(img.flatten())
lowestColor = min(img.flatten())

print(highestColor, lowestColor)

# %%


def show_image(image: np.ndarray):
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.show()


show_image(img)

# %%
# average


def get_image_average(image: np.ndarray):
    average = np.average(image)
    return average

# %%
# ecart type


def get_standard_deviation(image: np.ndarray):
    return np.std(image)


get_standard_deviation(img)

# %%


def get_histogram(image: np.ndarray):
    histogram = []
    flattened_image = image.flatten()
    for i in range(0, 256):
        histogram.append(np.count_nonzero(flattened_image == i))
    return np.array(histogram)


# %%
histogram = get_histogram(img)

# %%


def draw_histogram(histogram):
    plt.plot(range(256), histogram)
    plt.xlabel('niveau de gris')
    plt.show()


draw_histogram(histogram)

# %%


def get_accumulated_histogram(image: np.array):
    histogram = get_histogram(image)
    accumulated_histogram = np.add.accumulate(histogram)
    return accumulated_histogram


draw_histogram(get_accumulated_histogram(img))

# %%
np.shape(img)

# %%
# TP2


def get_proba_accumulated(image: np.ndarray):
    h = get_accumulated_histogram(image)
    return h / (np.shape(image)[0] * np.shape(image)[1])


# %%
get_proba_accumulated(img)

# %%


def get_A(image: np.ndarray):
    p = get_proba_accumulated(image)
    return p * 255


# %%
A = get_A(img)
n1 = A.astype("uint8")
print(n1)

# %%
# TP 3

# %%


def rand_helper(i):
    a = random.randint(0, 20)
    if a == 20:
        return 255
    elif a == 0:
        return 0
    else:
        return i


def add_noise(image: np.ndarray) -> np.ndarray:
    flat_noisy_image = np.array([rand_helper(i) for i in image.flatten()])
    return flat_noisy_image.reshape(image.shape)


# %%
noisy_image = add_noise(img)
show_image(noisy_image)

# %%


def mean_filter(image: np.ndarray, w=1):
    filtered = image.copy()
    for i in range(w, image.shape[0]-w):
        for j in range(w, image.shape[1]-w):
            block = image[i-w:i+w+1, j-w:j+w+1]
            mean_result = np.mean(block, dtype=np.float32)
            filtered[i][j] = int(mean_result)
    return filtered


n = mean_filter(noisy_image, 1)
show_image(n)
show_image(noisy_image)

# %%


def median_filter(image: np.ndarray, w=1):
    filtered = image.copy()
    for i in range(w, image.shape[0]-w):
        for j in range(w, image.shape[1]-w):
            block: np.ndarray = image[i-w:i+w+1, j-w:j+w+1]
            flat_sorted_block = np.sort(block.flatten())
            median_value = flat_sorted_block[4]
            filtered[i][j] = int(median_value)
    return filtered


n = median_filter(noisy_image, 1)
show_image(n)
show_image(noisy_image)

# %%
# measure median difference between images


def calc_noise_signal_ratio(image: np.ndarray, noisy_image: np.ndarray) -> float:
    average_value_image = get_image_average(image)
    s = np.sum(np.power((image - average_value_image), 2))
    b = np.sum(np.power(noisy_image - image, 2))
    return np.sqrt(s/b)

# %%


# %%
