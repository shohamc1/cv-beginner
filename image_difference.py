# import the necessary packages
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error as mse
import argparse
import imutils
import random
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True,
	help="first input image")
ap.add_argument("-s", "--second", required=True,
	help="second")
args = vars(ap.parse_args())

# load the two input images
imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])

# convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
s = ssim(grayA, grayB, full=True)
m = mse(grayA, grayB)

m = 1-(1/m)

score = s[0]*100*m*random.random()*100
s1 = 100000*(s[0] + m - 1) + 1000*random.random() + 11000
print("SSIM: {}".format(s[0]))
print("MSE: {}".format(m))
print (s1)