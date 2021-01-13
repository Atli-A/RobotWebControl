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
<<<<<<< HEAD
    # arr = json.dumps(jsonInput)

    print(type(arr))
    res = none
    for i in arr:
        res = i
=======
#    arr = json.dumps(jsonInput)
    arr = jsonInput 
    print(type(arr))
    print(arr)
    print(arr)

    print(arr)
    print(arr)
    print(arr)
    res = 0
    for i in arr:
        res= arr['positions']
>>>>>>> 63444cfc1a276c5aa6aae57f1c4cf43ec7457290
    
    print(res)
    return res


def publish(jsonInput):
    print("recieved")
    global publisher
    list = decodeJson(jsonInput)

<<<<<<< HEAD
    for i in range(len(list)):
        list[i] = int(list[i])
=======
    for i in range(len(arr)):
        arr[i] = int(arr[i])
>>>>>>> 63444cfc1a276c5aa6aae57f1c4cf43ec7457290
    
    
    mainstring = firstCmdPart

    for i in range(len(jsonInput)):
        mainstring += chr(i + 97) + ":" + str(arr[i]) + ","

    mainstring += lastCmdPart
    #publisher.publish( String('{"command":"direct","v1":"L:0,R:0,f:+0.8"}'))
    publisher.publish(String(mainstring))
    print("published")
    #example publish
    #publisher.publish(String(
    #    '{"h": 147.43, "r": 233.14, "pwr": true, "pos": "a:50,b:88.19,c:108.62,d:90,e:90.87,f:94.80,pwr:1", "v": 70.44}'))
