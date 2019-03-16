from threading import Thread
import cv2 , time
from Machine_Learning.bot.botAPI import *
from Machine_Learning.objectDetection import *

"""
varia = "Hi !"

if __name__ == '__main__':
    Thread(target=userProgram,args=[varia]).start()

"""


class interface:

    def __init__(self):
        self.buffer = ""
        self.flag = 0
        self.obj = object_detect()
    
    def user_function(self):
        while True:
            uinput = userProgram()
            if uinput in "launch":
                self.buffer = "render"   
                self.flag = 1
            elif uinput in "sleep":
                self.buffer = "sleep"   
                self.flag = 1
            
            print(self.flag)
            
            time.sleep(1)
    
    def process_function(self):        
        render_flag = 0
        while True:
            if self.flag is 1:
                if self.buffer is "render":
                    render_flag = 1
                elif self.buffer is "sleep":
                    render_flag = 0
                self.flag = 0 
            if render_flag is 1:
                self.obj.render_frame()
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            if render_flag is 0:
                cv2.destroyAllWindows()


if __name__ == '__main__':
    a = interface()   
    user_thread = Thread(target= a.user_function)
    user_thread.start()
    process_thread = Thread(target= a.process_function)
    process_thread.start()