import json
import rospy
from std_msgs.msg import String
# tests
# testjson = [{"positions": [90, 90, 90, 90, 151, 134]}]


# for i in testjson:
#     print('\n')
#     i['positions'])

rospy.init_node("customPub")



# firstCmdPart = '{"h": 147.43, "r": 233.14, "pwr": true, "pos": "'
# lastCmdPart = 'pwr:1", "v": 70.44}'
publisher = rospy.Publisher('/evocar/pub', String, queue_size=5)

firstCmdPart = '{"command":"direct","v1":"L:0,R:0,'
lastCmdPart = '"}'



# Example string:
#       '{"h": 147.43, "r": 233.14, "pwr": true, "pos": "a:90,b:88.19,c:108.62,d:90,e:90.87,f:94.80,pwr:1", "v": 70.44}'


def getSign(numInput):
    if (numInput > 0):
        return "+"
    else:
        return "-"

def decodeJson(jsonInput):
    #arr = json.loads(jsonInput)
    arr = jsonInput
    arr = arr["positions"]
   #print("arr = " + str(arr))

   #print("arr is a " + str(type(arr)))
   #res = 0
    for i in range(len(arr)):
       print(i)
       arr[i] = int(arr[i])
    #print(res)
    return arr


def publish(jsonInput):
    # print("recieved")
    global publisher
    list = decodeJson(jsonInput)
    for i in range(len(list)):
        list[i] = int(list[i])
    
    print("list = " + str(list))
    
    mainstring = firstCmdPart

    print(jsonInput)

    for i in range(len(jsonInput)):
        mainstring += chr(i + 97) + ":" + getSign(list[i]-90) + str((list[i]-90 )/10) + ","
    mainstring += lastCmdPart
    print("command sent = " + mainstring)
    #this works somehow
    # publisher.publish( String('{"command":"direct","v1":"L:0,R:0,a:+1"}'))
   #this doesnt work i think
    publisher.publish(String(mainstring))
    publisher.publish('data: "{\"command\":\"action\",\"v1\":\"k\"}"')
    # print("published")
    #example publish
   # publisher.publish(String(
   #     '{"h": 147.43, "r": 233.14, "pwr": true, "pos": "a:50,b:88.19,c:108.62,d:90,e:90.87,f:94.80,pwr:1", "v": 70.44}'))
