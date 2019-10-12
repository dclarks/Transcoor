import serial.tools.list_ports
list = serial.tools.list_ports.comports()
connected = []
for element in list:
    connected.append(element.device)
print("Connected COM ports: " + str(connected))

# deu pau por permissao denied
# sudo adduser MyUser dialout
# sudo chmod a+rw /dev/ttyUSB0


ser = serial.Serial(
    port='/dev/ttyUSB0',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
    timeout=0, \
    xonxoff=False, \
    dsrdtr=False, \
    rtscts=False)

print "esta aberto:", ser.is_open
ser.write("\r\nDiga algo:")
rcv = ser.readline()
ser.write("\r\nVoce mandou:" + repr(rcv))



85,9551

