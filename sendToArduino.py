import json
import rospy
from std_msgs.msg import String



testjson = [{"positions": [90, 90, 90, 90, 151, 134]}]


for i in testjson:
    print('\n')
    print(i['positions'])

rospy.init_node("customPub")

firstCmdPart = '{"command":"direct","v1":'

publisher = rospy.Publisher('/evocar/status', String, queue_size=5)



def publish(jsonInput):
    publisher.publish( String('{"command":"direct","v1":"L:0,R:0,f:0.4"}'))

#data: "{\"command\":\"direct\",\"v1\":\"L:0,R:0,x:-1.47\"}"

# data: '{"command":"direct","v1":"L:0,R:0,x:-1.47"}'
