from pyModbusTCP.client import ModbusClient


boolvalue= True
# create a modbus client object
client = ModbusClient(host="localhost", port=12345)


def readformserver():
    # start the modbus server
    if client.open():
        #read the value form the server in the specified register
        valuefromserver = client.read_holding_registers(0)
        placeholder = valuefromserver[0]
        # if the value sent from the server is 1 return 1 else 0
        if placeholder == 1:
            return True
            # boolvalue = True
            # return boolvalue
        elif placeholder == 0:
            return False
            # return boolvalue


def writetoserver (value):
    #writes the measured value to the server at the register 1

    client.write_single_register(1, int(round(value, 2)*100))