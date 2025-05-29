import serial 

modem=serial.Serial(port='/dev/ttyUSB0',
                    baudrate=9600,      
                    timeout=1)       
#modem.write(b'PWROFF\r')
with modem:
    #modem.write(b'\r') 
    modem.write(b'gethd\r\n') 

    prova=[]
    while True:
        x = modem.read(1024)   
        print(x)
        prova.append(x)

    print(prova)

