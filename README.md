# RobotWebControl


Note: This project is still a work in progress

This is intended as an alternative method of controlling the EvoArm 1.0

It has some advantages but is not as polished or as complete as the original.

This can also be run in parrellel with the original and that is likely the best way to use its

## Setup and use

To get started, ssh into the raspberry pi zero and run:

```sh
    $ git clone https://github.com/Atli-A/RobotWebControl.git
    $ cd RobotWebControl
```
To run it type EITHER of the following:
```sh
    $ ./main.py

    $ python3 main.py
```

To stop the program run:
```sh
    $ ./kill.sh
```

To use it go to the ip of your raspberry pi and go to port 8888

ex: xxx.xxx.x.xxx:8888

## Advantages

This allows the user to use exect positions on the slider for a simpler and more intuitive ui

This is also more lightweight than the default UI.

It uses Python 3 instead of Python 2 

## Potential improvements

- A nicer looking ui for controlling the robot

- Robot would use absolute positions rather than deltas

- The ability to control the speed

- Allow for custom programs

- Accept camera input