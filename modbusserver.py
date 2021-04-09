from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep

# Create an instance of ModbusServer
server = ModbusServer("localhost", 12345, no_block=True)

try:
    print("Start server...")
    server.start()
    print("Server is online")
    state = [0]
    while True:
        # DataBank.set_words(0, [int(1)])
        if state != DataBank.get_words(0):
            state = DataBank.get_words(0)
            print("Value of Register 1 has changed to " +str(state))
        sleep(0.5)

except:
    print("Shutdown server ...")
    server.stop()
    print("Server is offline")
