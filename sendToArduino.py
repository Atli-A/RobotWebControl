import json
import rospy

testjson = [{"positions": [90, 90, 90, 90, 151, 134]}]


for i in testjson:
    print('\n')
    print(i['positions'])


