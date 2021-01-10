import json
import rospy
from std_msgs.msg import String
# tests
# testjson = [{"positions": [90, 90, 90, 90, 151, 134]}]


# for i in testjson:
#     print('\n')
#     i['positions'])

rospy.init_node("customPub")



firstCmdPart = '{"h": 147.43, "r": 233.14, "pwr": true, "pos": "'
lastCmdPart = 'pwr:1", "v": 70.44}'
publisher = rospy.Publisher('/evocar/pub', String, queue_size=5)



# Example string:
#       '{"h": 147.43, "r": 233.14, "pwr": true, "pos": "a:90,b:88.19,c:108.62,d:90,e:90.87,f:94.80,pwr:1", "v": 70.44}'


def decodeJson(jsonInput) {
    arr = []
    for i in testjson:
        arr = i['positions'])
    
    return arr


}


def publish(jsonInput):
    print("recieved")
    global publisher
    arr = decodeJson(jsonInput)

    for i in range(arr.len):
        arr[i] = int(arr[i])
    
    
    mainstring = firstCmdPart

    for i in len(jsonInput):
        mainstring += chr(i + 97) + ":" + arr[i] + ","

    mainstring += lastCmdPart
    # publisher.publish( String('{"command":"direct","v1":"L:0,R:0,f:+0.8"}'))
    publisher.publish(String(mainstring))

    #example publish
    # publisher.publish(String(
    #     '{"h": 147.43, "r": 233.14, "pwr": true, "pos": "a:90,b:88.19,c:108.62,d:90,e:90.87,f:94.80,pwr:1", "v": 70.44}'))
