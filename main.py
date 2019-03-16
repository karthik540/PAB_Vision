from threading import Thread
from Machine_Learning.bot.botAPI import *
from Machine_Learning.bot

"""
varia = "Hi !"

if __name__ == '__main__':
    Thread(target=userProgram,args=[varia]).start()

"""
class interface:

    def __init__(self):
        self.buffer = ""
        self.flag = 0
    
    def user_function(self):
        while True:
            Thread(target= userProgram).start()
    
    def process_function(self):
        while True:
            Thread(target= userProgram).start()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

