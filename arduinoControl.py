import os


def readFile(filename):
    f = open(filename, "r")
    return f.read().encode()

# //functions


def writeToFile(data, filename):
    f = open(filename, "a")
    f.write(data)
    f.close()


def overwriteToFile(data, filename):
    f = open(filename, "w")
    f.write(data)
    f.close()


def shutdown():
    os.system("sudo shutdown now")


def reboot():
    os.system("sudo restart")


#
# testing


# writeToFile("yeet", "test.txt")
# reboot()
