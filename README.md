## image-stitcher
# Making cruder panaromic image


!pip install opencv-python !pip install imutils !pip install numpy

TO TEST RUN THE IMAGE STITCHER WITH SAMPLE OUTPUT CREATE A FOLDER IN IMAGE DIR AND POPULATE IT WITH THE IMAGES TO BE STITCHED TO CREATE A PANAROMA
python img-stitch-v1.py --images images/

--output panaroma-wihoutcrop.jpg
TO TEST RUN THE IMAGE STITCHER WITH THE ASTHETICALLY PLEASING CROPPED OUTPUT IMAGE OF A PANAROMA CREATE A FOLDER IN IMAGE DIR AND POPULATE IT WITH THE IMAGES TO BE STITCHED TO CREATE A CROPPED OUTPUT IMAGE OF A PANAROMA
python img-stitch-v2-withcrop.py --images images/

--output panaroma.jpg --crop 1
