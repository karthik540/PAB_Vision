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
    
    def user_function(self):
        while True:
            usr_input = userProgram()
            if("launch"):
                self.buffer = "render"
                self.flag = 1
            time.sleep(1)
    
    def process_function(self):
        obj = object_detect()
        render_flag = 0
        while True:
            if self.flag is 1:
                if self.buffer is "render":
                    render_flag = 1
                    self.flag = 0
            while render_flag is 1:
                obj.render_frame()
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            if render_flag is 1:
                obj.video_capture.release()
                cv2.destroyAllWindows()
            

if __name__ == '__main__':
    a = interface() 
    Thread(target=a.user_function).start()
    Thread(target=a.process_function).start()
    
