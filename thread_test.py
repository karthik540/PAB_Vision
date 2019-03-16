from threading import Thread
import time

class Addition:

    def __init__(self):
        self.num = 0

    def add1(self):
        while True:
            self.num += 1
            print(self.num)
            time.sleep(1)

    def add2(self):
        while True:
            self.num += 2
            print(self.num)
            time.sleep(1)

if __name__ == '__main__':
    a = Addition() 
    Thread(target=a.add1).start()
    Thread(target=a.add2).start()
