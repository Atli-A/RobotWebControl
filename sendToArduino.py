import json
import rospy
from std_msgs.msg import String
#tests
# testjson = [{"positions": [90, 90, 90, 90, 151, 134]}]


# for i in testjson:
#     print('\n')
#     print(i['positions'])

rospy.init_node("customPub")

firstCmdPart = '{"command":"direct","v1":'
publisher = rospy.Publisher('/evocar/pub', String, queue_size=5)



def publish(jsonInput):
    print("recieved")
    global publisher
    publisher.publish( String('{"command":"direct","v1":"L:0,R:0,f:+0.8"}'))
    publisher.publish( String('{"h": 147.43, "r": 233.14, "pwr": true, "pos": "a:90,b:88.19,c:108.62,d:90,e:90.87,f:94.80,pwr:1", "v": 70.44}'))
#data: "{\"command\":\"direct\",\"v1\":\"L:0,R:0,x:-1.47\"}"

# data: '{"command":"direct","v1":"L:0,R:0,x:-1.47"}'

'{"h": 147.43, "r": 233.14, "pwr": true, "pos": "a:90,b:88.19,c:108.62,d:90,e:90.87,f:94.80,pwr:1", "v": 70.44}'

