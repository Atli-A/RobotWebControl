# RobotWebControl


This project is unfinished and not entirely working.
I recommend that you do not install this until it works


The core functionality mostly works however it needs some calibration


Just a piece of adviece but currently the only way to easily kill the program is to ssh into it and type:

```sh
    $ ./kill.sh
```


#Setup and use

To get started, ssh into the raspberry pi zero and run:

```sh
    $ git clone git@github.com:Atli-A/RobotWebControl.git
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

