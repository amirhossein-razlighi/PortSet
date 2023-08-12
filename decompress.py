import numpy as np
import pywt
from PIL import Image
import os
import pickle
import matplotlib.pyplot as plt
import sys


def decompress(coeffs_r, coeffs_g, coeffs_b, wavelet="haar"):
    # Reconstruct the compressed channels
    reconstructed_r = pywt.waverec2(coeffs_r, wavelet)
    reconstructed_g = pywt.waverec2(coeffs_g, wavelet)
    reconstructed_b = pywt.waverec2(coeffs_b, wavelet)

    # Stack the reconstructed channels to form the compressed RGB image
    reconstructed_img = np.stack(
        (reconstructed_r, reconstructed_g, reconstructed_b), axis=-1
    )

    return reconstructed_img


if __name__ == "__main__":
    for folder in os.listdir("./Compressed"):
        if folder == ".DS_Store":
            continue

        for sub_folder in os.listdir("./Compressed/" + folder):
            if sub_folder == ".DS_Store":
                continue

            for file in os.listdir("./Compressed/" + folder + "/" + sub_folder):
                if file == ".DS_Store":
                    continue

                with open(
                    "./Compressed/" + folder + "/" + sub_folder + "/" + file,
                    "rb",
                ) as f:
                    coefficients = pickle.load(f)

                decompressed = decompress(
                    coefficients[0], coefficients[1], coefficients[2]
                )

                decompressed = (decompressed).astype(np.uint8)
                decompressed = Image.fromarray(decompressed, "RGB")

                decompressed.save(
                    "./Decompressed/" + folder + "/" + sub_folder + "/" + file[:-4] + ".jpg", "JPEG", quality=100
                )
