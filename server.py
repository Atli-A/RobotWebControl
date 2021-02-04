#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
import rospy
import threading
import send_to_arduino as sta
import arduino_control as aC
import logging
import simplejson
from http.server import BaseHTTPRequestHandler, SimpleHTTPRequestHandler, HTTPServer
from std_msgs.msg import String
import time
import json
print("imported json")
print("imported time")
print("imported String")

print("imported http server")
print("imported simplejson")
print("imported logging")
print("imported arduino control")
print("imported sTA")
print("imported thread")

print("imported rospy")
current_pos = []
num_run = 0
reset = False
publisher = rospy.Publisher('/evocar/pub', String, queue_size=5)



def status_read(ros_data):
    global current_pos
    global reset
    global num_run


    first_cmd_part = '{"command":"direct","v1":"L:0,R:0,'
    last_cmd_part = '"}'



    temp_arr = ros_data.data
    temp_arr = json.loads(temp_arr)
    current_pos.clear()
    temp_arr = temp_arr["pos"]
    temp_arr = dict([(i.split(':')) for i in temp_arr.split(',')])
    # print(temp_arr)
    for i in range(6):
        # print(temp_arr[i])
        current_pos.append(temp_arr[chr(i+97)])

    # print("current_pos = " + str(current_pos))
    if reset or num_run < 6:
        start_string = first_cmd_part
        start_string += ""

        for i in range(len(current_pos)):
            tmp = (chr(i + 97) + ":" + str("%+.0f" %
                                           (90 - (float(current_pos[i])))) + ",")
            start_string += tmp

        start_string = start_string[0:-1]
        start_string += last_cmd_part
        print("reset or numrun called")
        num_run += 1
    # print("start_string = " + start_string)
        publisher.publish(String(start_string))
        has_run = True
        reset = False


def run_spin():
    rospy.spin()


print("finished defining functions")
rospy.init_node("readStatus")

rospy.Subscriber("/evocar/status", String, status_read, queue_size=5)


rospy_thread = threading.Thread(target=run_spin, name="run_spin")
rospy_thread.daemon = True
rospy_thread.start()


# server stuff starts here

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        #     self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()

        logging.info("GET request,\nPath: %s\n", str(self.path))
        if self.path == '/':
            possible_name = './index.html'
        else:
            possible_name = '.' + self.path
        logging.info("possible_name: %s" % possible_name)

        f = open(possible_name, "r")
        contents = f.read().encode()
        self.wfile.write(contents)

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        global reset
        global current_pos
        self._set_headers()
        logging.info("in post method")
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        self.send_response(200)
        self.end_headers()

        data = simplejson.loads(self.data_string)
        logging.info("{}".format(data))

        if "positions" in data:  # for position setting
            sta.publish(data, current_pos)
        else:  # for commands
            commandNick = ""
            for i in data:
                commandNick += data[i]

            if (commandNick == "restart"):
                aC.reboot()
            elif (commandNick == "shutdown"):
                aC.shutdown()
            elif (commandNick == "reset"):
                print("reset definetly called")
                reset = True


def run(server_class=HTTPServer, handler_class=S, port=8888):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except:
        httpd.server_close()
        exit()
    logging.info('Stopping httpd...\n')
