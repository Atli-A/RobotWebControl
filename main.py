#!/usr/bin/env python3

import server
import time


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        print(server.run(port=int(argv[1])))
    else:
        server.run()

print("finished main")
