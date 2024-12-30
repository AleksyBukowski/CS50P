from PIL import Image
import numpy as np
import sys

def main():
    argv_len = len(sys.argv)
    if argv_len != 2:
        sys.exit(f"1 additional command-line argument expected, {argv_len-1} given")
    elif not sys.argv[1].endswith((".jpg", ".png", ".jpeg")):
        sys.exit("File must be of JPG, PNG or JPEG type")
    print(f"Brightness: {round(calculate_brightness(sys.argv[1]) * 100)}%")


def calculate_brightness(filename):
    # Open the image using PIL
    try:
        with Image.open(filename) as image:
            # Convert the image to grayscale (L mode)
            grayscale_image = image.convert("L")

            # Convert the grayscale image to a NumPy array and calculate the mean of the pixel values
            brightness = np.mean(np.array(grayscale_image)) / 255  # Normalize the brightness value
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Return the calculated brightness
    return brightness


if __name__ == "__main__":
    main()
