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

This project is originally developed to communicate with a PLC over modbus but if you would like to try out the application follow the steps below:
- Open and run the __modbusserver.py__ script in your favorite ide. Personaly i prefer idle because it is simple to use. (In the original setup the PLC acts as a server and a client which can READ and WRITE data to registers of the modbus network. In our case if we want to WRITE data we need a separate client that is connected to the same server which is exactly what we will do in step 3)
- Open the __Distance_measurement.exe__ file (it is inside the dist folder)(now the program is waiting for input so lets give it an input)
- Open command prompt and execute the following commands one by one 
  - python
  - pip install pyModbusTCP
  - from pyModbusTCP.client import ModbusClient
  - client = ModbusClient(host="localhost", port=12345)
  - client.open()
  - client.write_single_register(0,1)
  - once you get the distance value type client.write_single_register(0,0)
  - alternate between the last two steps and you can keep measuring again and again

