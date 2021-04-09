import utils
import modbusclient

if __name__ =='__main__':

#####################################################################################
    switch = True

    while True:
        D = 0
        lastD = 0
        array = []
        dictionary = {}

        # start = input()
        # reads boolean the data (1 or 0) from the server and saves it is a variable
        start = modbusclient.readformserver()
        # print(type(start))
        if start and switch == True:
            # To prevent continuous execution switch is set to false
            switch = False
            # loop through the getcountour function 50 times in order to get accurate results
            for i in range(50):
                D = utils.getcontours()
                if D != lastD and D is not None:
                    # Save the measured value in a array only if it is above 200mm i.e this is done to remove outliers
                    if D >= 200:
                        array.append(D)
                        lastD = D
            # Reads the final output value
            measured_distance = utils.probableValue(array)
            # Writes the value back to the server
            modbusclient.writetoserver(measured_distance)
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
            switch = True
######################################################################################


