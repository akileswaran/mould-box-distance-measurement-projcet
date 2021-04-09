import cv2
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import os


def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

cap = cv2.VideoCapture(0)
cap.set(10, 150)
cap.set(3, 1920)
cap.set(4, 1080)
def getcontours():
    # load the image, convert it to grayscale, and blur it slightly
    ret, image = cap.read()
    r = 250.0 / image.shape[0]
    dim = (int(image.shape[1] * r), 250)
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)

    # perform edge detection, then perform a dilation + erosion to
    # close gaps in between object edges
    edged = cv2.Canny(gray, 50, 100)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)
    # edged = medfilt2(edged,[10 10],'symmetric');
    # find contours in the edge map
    cnts, a = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # cnts = cnts[0] #if imutils.is_cv2() else cnts[1]
    # print (cnts)
    # sort the contours from left-to-right and, then initialize the
    # distance colors and reference object
    (cnts, _) = contours.sort_contours(cnts, method='right-to-left')
    colors = ((0, 0, 255), (240, 0, 159), (0, 165, 255), (255, 255, 0),
              (255, 0, 255))
    refObj = None
    # print(cnts)

    # loop over the contours individually
    for c in cnts:
        # if the contour is not sufficiently large, ignore it
        if cv2.contourArea(c) < 100:
            continue
        # compute the rotated bounding box of the contour
        box = cv2.minAreaRect(c)
        # print(box)
        box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
        box = np.array(box, dtype="int")
        # print(box)

        # order the points in the contour such that they appear
        # in top-left, top-right, bottom-right, and bottom-left
        # order, then draw the outline of the rotated bounding
        # box
        box = perspective.order_points(box)

        # compute the center of the bounding box
        cX = np.average(box[:, 0])
        cY = np.average(box[:, 1])

        # if this is the first contour we are examining (i.e.,
        # the left-most contour), we presume this is the
        # reference object
        if refObj is None:
            # unpack the ordered bounding box, then compute the
            # midpoint between the top-left and top-right points,
            # followed by the midpoint between the top-right and
            # bottom-right
            (tl, tr, br, bl) = box
            (tlblX, tlblY) = midpoint(tl, bl)
            (trbrX, trbrY) = midpoint(tr, br)

            # compute the Euclidean distance between the midpoints,
            # then construct the reference object
            D = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
            refObj = (box, (cX, cY), D / 80)
            continue
        # draw the contours on the image
        orig = image.copy()
        # one = cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)
        # two = cv2.drawContours(orig, [refObj[0].astype("int")], -1, (0, 255, 0), 2)

        # stack the reference coordinates and the object coordinates
        # to include the object center
        refCoords = np.vstack([refObj[1]])
        objCoords = np.vstack([(cX, cY)])
        # print (refCoords)

        # loop over the original points

        for ((xA, yA), (xB, yB), color) in zip(refCoords, objCoords, colors):
            # draw circles corresponding to the current points and
            # connect them with a line
            cv2.circle(orig, (int(xA), int(yA)), 5, color, -1)
            cv2.circle(orig, (int(xB), int(yB)), 5, color, -1)
            cv2.line(orig, (int(xA), int(yA)), (int(xB), int(yB)),
                     color, 2)
            # compute the Euclidean distance between the coordinates,
            # and then convert the distance in pixels to distance in
            # units
            D = dist.euclidean((xA, yA), (xB, yB)) / refObj[2]
            (mX, mY) = midpoint((xA, yA), (xB, yB))
            cv2.putText(orig, "{:.2f}mm".format(D), (int(mX), int(mY - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, color, 2)
            # show the output image
            measured_distance = float(D)
            # cv2.imwrite('output' + str(image_number) + '.jpg', orig)
            # image_number += 1
            # cv2.imwrite('output.jpg',orig)
            cv2.imshow('output',orig)
            cv2.waitKey(300)
            return measured_distance

def probableValue(array):
    dictionary = {}
    # print(array)
    for elem in array:
        if array.count(elem) > 1:
            dictionary[elem] = array.count(elem)
    # print(dictionary)
    if bool(dictionary):

        max_key = max(dictionary, key=dictionary.get)
        print("repeating number",max_key)
        for element in range(len(array)):
            if array[element] == max_key:
                return element
    else:
        try:
            average = sum(array) / len(array)
            print("average number",average)
            for element in range(len(array)):
                if array[element] == average:
                    return element
        except:
            print("No contours found in the image. Adjust the camera to bring the runners in the field of view of the camera")


