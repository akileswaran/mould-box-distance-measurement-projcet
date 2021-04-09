from pyModbusTCP.client import ModbusClient

def modbusclient():
    boolvalue= True
    client = ModbusClient(host="localhost", port=12345)
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