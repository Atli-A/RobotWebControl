import arduinoControl as arduinoctl 
import server



if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        server.run(port=int(argv[1]))
    else:
        server.run()


