from threading import Thread
import time

class Addition:

    def __init__(self):
        self.flag = 0
        self.buffer = ""

    def userProgram(self):
        while True:
            usr_input = input("User:")
            self.buffer = usr_input
            self.flag = 1
            time.sleep(1)

    def processingProg(self):
        while True:
            if self.flag is 1:
                buffer = self.buffer
                print("Server recieved " + buffer)
                self.flag = 0
            time.sleep(1)

if __name__ == '__main__':
    a = Addition() 
    Thread(target=a.userProgram).start()
    Thread(target=a.processingProg).start()
