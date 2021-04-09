import cv2
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import utils
import modbusclient



if __name__ =='__main__':

#####################################################################################
    switch = 0

    while True:
        D = 0
        lastD = 0
        array = []
        dictionary = {}

        # start = input()
        start = modbusclient.modbusclient()
        # print(type(start))
        if start and switch == 0:
            switch+=1
            for i in range(50):
                D = utils.getcontours()
                if D != lastD and D is not None:
                    if D >= 200:
                        array.append(D)
                        lastD = D

            image_number = utils.probableValue(array)

            # output = cv2.imread('output'+str(image_number)+'.jpg')
            # output = cv2.imread('output.jpg')
            # output = cv2.imread('C:/Users/akile/PycharmProjects/test/images/output.jpg')
            # cv2.imshow('output', output)
            # cv2.waitKey(0)
            # key = cv2.waitKey(1) & 0xFF
    #         if cv2.waitKey(1) & 0xFF == ord('q'):
    #             break
    #         else: continue
    # cv2.destroyAllWindows()
        if not start:
            switch = 0
######################################################################################


