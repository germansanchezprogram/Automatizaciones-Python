from PIL import Image

import os

DownloadsFolder = "c:/Users/BANGHO/OneDrive/Downloads"

if __name__ == "__main__":
    for filename in os.lisrdir(DownloadsFolder):
        name, extension = os.path.splitext(DownloadsFolder + filename)

        if extension in [".jpg", "jpeg","png"]:
            picture.save(DownloadsFolder + "compressed_" + filename, optimize=True, quality=60)

