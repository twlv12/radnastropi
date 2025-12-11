import cv2
import math



from exif import Image
from datetime import datetime

def GetTime(image):
    with open(image, "rb") as image_file:
        img = Image(image_file)
        time_str = img.get("datetime_original")
        time = datetime.strptime(time_str, '%Y:%m:%d %H:%M:%S')

def GetTimeDifference(img1, img2):
    time1 = GetTime(img1)
    time2 = GetTime(img2)
    timeDif = time2-time1
    print(time1, time2, timeDif)

def convertToCV2(image1, image2):
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)

    return img1, img2

def calculateImage(image1, image2, featureNumber):
    
    orb = cv2.ORB_create(nfeateatures = featureNumber)
    keypoints1 ,descriptors1 = orb.detectAndCompute(img1,None)
    keypoints2 ,descriptors2 = orb.detectAndCompute(img2, None)

    return keypoints1, keypoints2, descriptors1, descriptors2

def findMatches(descriptors1, descriptors2):
    brute_force = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = brute_force.match(descriptors1, descriptors2)
    matches = sorted(matches, key=lambda x: x.distance)
    return matches

img1, img2 = convertToCV2("image_00.jpg", "image_04.jpg")

timeDif = GetTimeDifference(img1, img2)
keypoints1, keypoints2, descriptors1, descriptors2 = calculateImage()