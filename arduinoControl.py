import os

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
    os.system("shutdown now")




def reboot():
    os.system("restart")


#
# testing

writeToFile("yeet", "test.txt")