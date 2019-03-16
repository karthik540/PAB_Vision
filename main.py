from threading import Thread
from Machine_Learning.bot.botAPI import *

varia = "Hi !"

if __name__ == '__main__':
    Thread(target=userProgram,args=[varia]).start()