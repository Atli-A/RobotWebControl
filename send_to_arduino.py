import json
import math
import threading
import rospy
from std_msgs.msg import String


zeroes = [90, 90, 90, 90, 90, 90]



publisher = rospy.Publisher('/evocar/pub', String, queue_size=5)

firstCmdPart = '{"command":"direct","v1":"L:0,R:0,'
lastCmdPart = '"}'




def create_delta_command(deltas):
    first_cmd_part = '{"command":"direct","v1":"L:0,R:0,'
    last_cmd_part = '"}'

    start_string = first_cmd_part
    start_string += ""

    for i in range(len(deltas)):
        tmp = (chr(i + 97) + ":" + "%+.0f" % float(deltas[i]) + ",")
        start_string += tmp

    start_string = start_string[0:-1]
    start_string += last_cmd_part

    return start_string


def printDict(dictInput):
    result = ""
    for i in dictInput:
        result += str(i) + "   "

    return result

# def getSign(numInput):
#     if (numInput > 0):
#         return "+"
#     else:
#         return ""

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
    decoded_input = decodeJson(jsonInput)
    for i in range(len(decoded_input)):
        decoded_input[i] = float(decoded_input[i])
    
    print("decoded_input = " + str(decoded_input))
    print("zeroes = " + str(zeroes))
    

    list_delta = [0, 0, 0, 0, 0, 0]
    
    for i in range(len(decoded_input)):
        list_delta[i] = decoded_input[i] - zeroes[i]
    

    zeroes = decoded_input #sets new values for the zeroes ased on current vals to calculate next delta


    main_string = create_delta_command(list_delta)
   
    # for i in range(len(list_delta)):
    #     if (round(list_delta[i]) != 0):
    #         tmp = chr(i+97) + ":" + getSign(list_delta[i]) + str((list_delta[i])) + ","
    #         main_string += tmp

    #         # print(str(i) +  " tmp = " + tmp)

      
    # main_string = main_string[0:-1]
    # main_string += lastCmdPart
    print("command sent = " + main_string)
    if (String(main_string) != firstCmdPart + lastCmdPart):
        publisher.publish(String(main_string))
    
print("made to end")
