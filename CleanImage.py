import os
import glob
images = glob.glob("images/*.png")
for image in images:
    os.remove(image)