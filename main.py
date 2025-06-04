import serial 
import time
import json
#import logging

###################### Functions ######################

def serialWrite(serialObj,message,doEcho=True):
    serialObj.write(bytes(message+"\r\n", 'utf-8'))
    if doEcho: print(message)
    
def serialRead(serialObj,doPrint=True):
    message=bytearray()
    while serialObj.in_waiting>0:
        message.extend(serialObj.read()) 
        time.sleep(0.01)
    if doPrint: print(message.decode())
    return(message)

def commandSetting(serialObj,message,doEcho,doPrint):
    serialWrite(serialObj,message,doEcho)
    time.sleep(4) 
    replyMessage=serialRead(serialObj,doPrint)
    return replyMessage

def ListCommandSetting(serialObj,list,doEcho,doPrint):
    for i in list:
        commandSetting(serialObj,i,doEcho,doPrint)
        time.sleep(1) 


###################### MAIN PROGRAM ######################

"""logging.basicConfig(filename='runLog.log', filemode='w', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Program started')"""

with open("immConfig.json", 'r') as file:
    immConfig=json.load(file)  
with open("slaveConfig.json", 'r') as file:
    slaveConfig=json.load(file)  

modem=serial.Serial(port='/dev/ttyUSB0',
                    baudrate=9600,      
                    timeout=1)     

with modem:
    #ListCommandSetting(modem,immConfig["initialConfig"],doEcho=True,doPrint=True)
    time.sleep(3)
    ListCommandSetting(modem,slaveConfig["captureLine"],doEcho=True,doPrint=True)

    for slave in slaveConfig["slavePrefix"]:
        for message in slaveConfig["initialConfig"]:
            commandSetting(modem,slave+message,doEcho=True,doPrint=True)

    for slave in slaveConfig["slavePrefix"]:
        pass
    
    prova=bytearray()
    while modem.in_waiting>0:
        prova.extend(modem.read()) 
    print(prova.decode())


