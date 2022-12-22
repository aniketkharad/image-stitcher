from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
import os

def main():
    
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--images", type=str, required=True,
		help="path to input directory of images to stitch")
    ap.add_argument("-o", "--output", type=str, required=True,
		help="path to the output image")
    args = vars(ap.parse_args())

    imagePaths = sorted(list(paths.list_images(args["images"])))
    images = []
    print('\n\tREADING IMAGES FROM THE GIVEN DIR COMPLETED\n')

    for imagePath in imagePaths:
        image = cv2.imread(imagePath)
        images.append(image)

    # OR
    # [images.append( cv2.imread(imagesPath) ) for imagePath in imagePaths]

    stitcher = cv2.Stitcher_create()
    (status, stitched) = stitcher.stitch(images)
    print('\tSTITCHING COMPLETED\n')

    if status == 0:
        cv2.imwrite(args["output"], stitched)
        cv2.imshow("Stitched", stitched)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        os._exit(0)
    else:
        print("\tSTITCHING FAILED ({})".format(status))
        os._exit(0)


if __name__ == "__main__":
    main()