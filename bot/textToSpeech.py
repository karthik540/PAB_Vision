from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice")

"""from gtts import gTTS

import os

language = 'en'

def speakText(usr_text):
    speechObj = gTTS(text = usr_text , lang= language , slow= False)
    speechObj.save("bot_conv.mp3")
    os.system("start bot_conv.mp3")

speakText("Hello ! , how are you ?")

"""
def speakText(usr_text):
    speak.Speak(usr_text)
    return