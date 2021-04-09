from pyModbusTCP.client import ModbusClient


boolvalue= True
client = ModbusClient(host="localhost", port=12345)


def modbusclient():

    if client.open():
        valuefromserver = client.read_holding_registers(0)
        placeholder = valuefromserver[0]
        if placeholder == 1:
            return True
            # boolvalue = True
            # return boolvalue
        elif placeholder == 0:
            return False
            # return boolvalue


def writetoserver (value):
    if client.open():
        try:
            client.write_single_register(1,int(value))
        except:
            print("no objects to measure")