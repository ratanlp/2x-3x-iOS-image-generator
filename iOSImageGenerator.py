# Utility class to create @2x and @3x sizes images for iOS development
# @author - Ratan Lal Prasad
# @email - ratan.kgn@gmail.com

from __future__ import print_function
import os, sys
from PIL import Image

STORE_DIRECTORY_PATH = '/Users/ratan/Documents/ios_project/images/'
RESIZED_DIR_PATH = 'RESIZED-IMAGES'

BASE_WIDTH_2X = 130 # Provide the size of the image for 2x
BASE_WIDTH_3X = BASE_WIDTH_2X*1.5

REPLACE_NAME_2X = "@2x."
REPLACE_NAME_3X = "@3x."

# REPLACE_NAME_2X = "."
# REPLACE_NAME_3X = "."

def resizeImagesFor2x(is2x):
    store_dir=STORE_DIRECTORY_PATH+RESIZED_DIR_PATH+"/"

    if not os.path.exists(store_dir) :
        os.mkdir(store_dir)

    for filename in os.listdir(STORE_DIRECTORY_PATH):
        print("Filename is ", filename)

    files = [] # list of tuple with old filename and new filename
    counter = 0

    for file in os.listdir(STORE_DIRECTORY_PATH):
        if not file.startswith('.') and os.path.isfile(STORE_DIRECTORY_PATH +file) and file.find(" ") > 0:
            counter = counter + 1
            os.rename(STORE_DIRECTORY_PATH +file, STORE_DIRECTORY_PATH + file.replace(" ", "_"))

        # print("After Filename is ", file)

        if not file.startswith('.') and os.path.isfile(STORE_DIRECTORY_PATH +file):

            basewidth = BASE_WIDTH_3X
            replaceNameWith = REPLACE_NAME_3X
            if is2x :
                basewidth = BASE_WIDTH_2X
                replaceNameWith = REPLACE_NAME_2X

            width = int(basewidth) # to int
            img = Image.open(STORE_DIRECTORY_PATH+file)
            # print("Image size is ", img.size)
            resizedImg = img.resize((width, width), Image.ANTIALIAS)
            newFname = file.lower().replace(".", replaceNameWith)
            resizedImg.save(store_dir+newFname)

if __name__ == "__main__":
        resizeImagesFor2x(1)
        resizeImagesFor2x(0)