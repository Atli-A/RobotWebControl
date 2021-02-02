#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
import json
print("imported json")
import time
print("imported time")
from std_msgs.msg import String
print("imported String")

from http.server import BaseHTTPRequestHandler, SimpleHTTPRequestHandler, HTTPServer
print("imported http server")
import simplejson
print("imported simplejson")
import logging
print("imported logging")
import arduinoControl as aC
print("imported arduino control")
import sendToArduino as sta
print("imported sTA")
import threading
print("imported thread")
import rospy

print("imported rospy")
current_pos = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f']
num_run = 0
publisher = rospy.Publisher('/evocar/pub', String, queue_size=5)


def get_sign(to_sign):
    if to_sign > 0:
        return "+"
    else:
        return "-"


def status_read(ros_data):
    global current_pos
    global num_run
    first_cmd_part = '{"command":"direct","v1":"L:0,R:0,'
    last_cmd_part = '"}'

    temp_arr = ros_data.data
    temp_arr = json.loads(temp_arr)
    current_pos.clear()
    temp_arr = temp_arr["pos"]
    temp_arr = dict([(i.split(':')) for i in temp_arr.split(',')])
    #print(temp_arr)
    for i in range(6):
        #print(temp_arr[i])
        current_pos.append(temp_arr[alphabet[i]])

        pass


    print("current_pos = " + str(current_pos))
    start_string = first_cmd_part
    start_string += ""

    for i in range(len(current_pos)):
        tmp = chr(i + 97) + ":" + str("%+.0f" % (90 - (float(current_pos[i])))) + ","
        start_string += tmp

    start_string += last_cmd_part
    if num_run < 6:
        num_run += 1
        print("start_string = " + start_string)
        publisher.publish(String(start_string))
        has_run = True
    


def run_spin():
    rospy.spin()

print("finished defining functions")
rospy.init_node("readStatus")

rospy.Subscriber("/evocar/status", String, status_read, queue_size=5) 


rospy_thread = threading.Thread(target=run_spin, name="run_spin")
rospy_thread.daemon = True
rospy_thread.start()


#rospy.spin()






# server stuff starts here

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        #     self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        #        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        #         if self.path == '/test':
        #             self._set_headers()
        #             content = '''
        # <html>
        #   <header><title>Dad rules!</title></header>
        #   <body>
        #     <h1>Dads rule!
        #   </body>
        # </html>'''
        #             self.wfile.write(content.encode())
        #             return
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
        global current_pos
        self._set_headers()
        logging.info("in post method")
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        self.send_response(200)
        self.end_headers()

        data = simplejson.loads(self.data_string)
        logging.info("{}".format(data))

        print(data)

        if "positions" in data:
            print('chose a position')
            sta.publish(data, current_pos)
        else: #for commands
            commandNick = ""
            for i in data:
                commandNick += data[i]

            if (commandNick == "restart"):
                aC.reboot()
            elif (commandNick == "shutdown"):
                aC.shutdown()

            # ------------------------------------------------Dont know if i should block this out but it seems to work--
            # class MyRequestHandler(SimpleHTTPRequestHandler):
            #     def do_GET(self):
            #         possible_nado_me = self.path.strip("/")+'.html'
            #         if self.path == '/test':

            #             logging.info("GET request,\nPath: %s\nHeaders:\n%s\n",
            #                          str(self.path), str(self.headers))
            #             self._set_response()
            #             self.wfile.write("GET request for {}".format(
            #                 self.path).encode('utf-8'))
            #             return
            #         return SimpleHTTPRequestHandler.do_GET(self)





def run(server_class=HTTPServer, handler_class=S, port=8888):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except:
    
        print("yeet")
        #pass
        httpd.server_close()
        exit()
    logging.info('Stopping httpd...\n')


# if __name__ == '__main__':
#     from sys import argv

#     if len(argv) == 2:
#         run(port=int(argv[1]))
#     else:
#         run()
