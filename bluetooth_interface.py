import socket
import bluetooth
MAC = '78:F7:BE:1D:9B:1D'
MAC1 = 'D0:B3:3F:77:CC:0F'
port = 6
soc = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
devices = bluetooth.discover_devices()
print(devices)

service = bluetooth.find_service(address=MAC)
print(service)
soc.connect((MAC,port))
'''
sock.connect((MAC,port))
sock.send("hello")
sock.close()


port = 10
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))
while 1:
    text = raw_input() # Note change to the old (Python 2) raw_input
    if text == "quit":
        break
    s.send(text)
sock.close()
'''
