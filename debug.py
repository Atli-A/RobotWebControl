#!/usr/bin/env python3


print("before import")
import sendToArduino as sta




for i in range(18):
    print(str(i * 10) + " - 90 is: ")
    print(sta.getSign((i*10) - 90))
