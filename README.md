# mould-box-distance-measurement-projcet
> This Project is still a work in progress
- This project involves the development of a computer vision algorithm to measure the distance between two runners in an array of mould boxes and a program to relay the measured distance to a Siemens PLC using modbus communication protocol. 

**Overview of the algorithm**
- Capture an image from the camera feed (will be changed in future to work in realtime)
- Perform preprocessing on the image to reduce computing time
- Create an edge map using morphological operations and canny edge detection
- detect the outlines of the objects in the edge map
- The outlines are stored in a list and the right most countour is taken as the refference object
- Since the size of the runner holes in the mould is already known (80-120mm) we can compute the size of objects in the image Using the "pixel per metric ratio" identify the size of the countours.
- Then the program loops through each of these countours and computes a rotated bounding box around each countour. Then the bounding box coordinates are rearranged in top-left, top-right, bottom-right, and bottom-left order.
- Then the center of the bounding boxes are calculated
- Then the ordered bounding boxes are unpacked and the midpoint between the top-left, top-right, bottom-right, and bottom-left are computed 
- Then the Euclidean distance between the midpoints are then computed which gives the "pixels-per-metric", allowing to determing how many pixels fit into the known width eg:(80-120mm)
- two object with the coordinates are created.
- the euclidean distance between the centroids is computed and then converted to the distance in pixels to distance in units


![image](https://user-images.githubusercontent.com/62331013/113076862-3bf3f180-91d0-11eb-847f-f0b6fd40f9ce.png)


