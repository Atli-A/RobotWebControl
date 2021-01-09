#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, SimpleHTTPRequestHandler, HTTPServer
import logging
import simplejson
import arduinoControl as aC

import sendToArduino as sta


# import arduinoControl

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
            possible_name = './' + self.path
        logging.info("possible_name: %s" % possible_name)

        f = open(possible_name, "r")
        contents = f.read().encode()
        self.wfile.write(contents)

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
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
            # sta.sendTo(data)
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
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')


# if __name__ == '__main__':
#     from sys import argv

#     if len(argv) == 2:
#         run(port=int(argv[1]))
#     else:
#         run()
