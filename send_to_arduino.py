import json
import math
import threading
import rospy
from std_msgs.msg import String


zeroes = [90, 90, 90, 90, 90, 90]



publisher = rospy.Publisher('/evocar/pub', String, queue_size=5)

firstCmdPart = '{"command":"direct","v1":"L:0,R:0,'
lastCmdPart = '"}'


def printDict(dictInput):
    result = ""
    for i in dictInput:
        result += str(i) + "   "

    return result

def getSign(numInput):
    if (numInput > 0):
        return "+"
    else:
        return ""

def decodeJson(jsonInput):
    print(type(jsonInput))
    arr = jsonInput
    print("type of arr is " + str(type(arr)))
    arr = arr["positions"]
    for i in range(len(arr)):
       print(i)
       arr[i] = float(arr[i])
    return arr


def publish(jsonInput, current_pos):
    print("recieved")
    global zeroes 
    global publisher
    for i in range(len(current_pos)):
        zeroes[i] = (float(current_pos[i]))
    list = decodeJson(jsonInput)
    for i in range(len(list)):
        list[i] = float(list[i])
    
    print("list = " + str(list))
    print("zeroes = " + str(zeroes))
    mainstring = firstCmdPart
    

    listDelta = [0, 0, 0, 0, 0, 0]
    
    for i in range(len(list)):
        listDelta[i] = list[i] - zeroes[i]
    
    print("listDelta = " + str(listDelta))

    zeroes = list
   
    for i in range(len(listDelta)):
        if (round(listDelta[i]) != 0):
            tmp = chr(i+97) + ":" + getSign(listDelta[i]) + str((listDelta[i])) + ","
            mainstring += tmp

            # print(str(i) +  " tmp = " + tmp)

      
    mainstring = mainstring[0:-1]
    mainstring += lastCmdPart
    print("command sent = " + mainstring)
    if (String(mainstring) != firstCmdPart + lastCmdPart):
        publisher.publish(String(mainstring))
    
print("made to end")
