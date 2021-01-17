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
    print("recieved")
    global publisher
    list = decodeJson(jsonInput)
    print("list = " + str(list))
    for i in range(len(list)):
        list[i] = int(list[i])
    
    
    mainstring = firstCmdPart

    for i in range(len(jsonInput)):
        mainstring += chr(i + 97) + ":" + str(list[i]) + ","

    mainstring += lastCmdPart
    #this works somehow
    publisher.publish( String('{"command":"direct","v1":"L:0,R:0,a:+1"}'))
   #this doesnt work i think
    publisher.publish(String(mainstring))
    print("published")
    #example publish
   # publisher.publish(String(
   #     '{"h": 147.43, "r": 233.14, "pwr": true, "pos": "a:50,b:88.19,c:108.62,d:90,e:90.87,f:94.80,pwr:1", "v": 70.44}'))
