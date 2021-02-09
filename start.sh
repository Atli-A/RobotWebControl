#!/bin/bash

python3 -u main.py > /tmp/RobotControl.log & tail -F /tmp/RobotControl.log
