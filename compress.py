import numpy as np
import pywt
from PIL import Image
import os
import pickle
import matplotlib.pyplot as plt


def compress(img, level=3, threshold=25, wavelet="haar"):
    image = np.array(img)

    # Split the RGB image into its three color channels
    red_channel = image[:, :, 0]
    green_channel = image[:, :, 1]
    blue_channel = image[:, :, 2]

    # Perform wavelet transformation on each channel
    coeffs_r = pywt.wavedec2(red_channel, wavelet, level=level)
    coeffs_g = pywt.wavedec2(green_channel, wavelet, level=level)
    coeffs_b = pywt.wavedec2(blue_channel, wavelet, level=level)

    # Apply thresholding to compress the coefficients for each channel
    coeffs_thresholded_r = [
        pywt.threshold(c, threshold, mode="soft") if isinstance(c, np.ndarray) else c
        for c in coeffs_r
    ]
    coeffs_thresholded_g = [
        pywt.threshold(c, threshold, mode="soft") if isinstance(c, np.ndarray) else c
        for c in coeffs_g
    ]
    coeffs_thresholded_b = [
        pywt.threshold(c, threshold, mode="soft") if isinstance(c, np.ndarray) else c
        for c in coeffs_b
    ]

    return (
        coeffs_thresholded_r,
        coeffs_thresholded_g,
        coeffs_thresholded_b,
    )


if __name__ == "__main__":
    for folder in os.listdir("./Dataset"):
        if folder == ".DS_Store":
            continue

        for sub_folder in os.listdir("./Dataset/" + folder):
            if sub_folder == ".DS_Store":
                continue

            for file in os.listdir("./Dataset/" + folder + "/" + sub_folder):
                if file == ".DS_Store":
                    continue

                img = Image.open("./Dataset/" + folder + "/" + sub_folder + "/" + file)
                coeffs_r, coeffs_g, coeffs_b = compress(img)
                coefficients = [coeffs_r, coeffs_g, coeffs_b]
                with open(
                    "./Compressed/"
                    + folder
                    + "/"
                    + sub_folder
                    + "/"
                    + file[:-4]
                    + ".pkl",
                    "wb",
                ) as f:
                    pickle.dump(coefficients, f)
