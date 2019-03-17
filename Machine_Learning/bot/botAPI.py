import json
import apiai
import urllib.request
from urllib.parse import quote_plus
#from speechOutput import *
from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice")

CLIENT_ACCESS_TOKEN = '07dffa75a2404bc59cb0101655d300e9'

def textToSpeech(message):    
    speak.Speak(message)
    return


def botResponseReciever(queryMessage):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.query = queryMessage

    response = request.getresponse()

    rawData = str(response.read())
    rawData = rawData.replace(r"\n" , "")       #Remove \n 
    rawData = rawData.replace(r"b'" , "" , 1)   #Remove b'
    rawData = rawData.replace(r"\'" , "")   #Remove \' which causes prob in the bot message
    jsonData = rawData[0:-1]                        #Remove ' in the end

    data = json.loads(jsonData)
    textToSpeech(data['result']['fulfillment']['speech'])
    return data['result']['fulfillment']['speech']
#botResponseReciever("Friend Karthik")

def userProgram():
    user_input = str(input("User: "))
    bot_response = botResponseReciever(user_input)
    print("\nVision: " + str(bot_response))
    return user_input

if __name__ == '__main__':
	while True:
		userProgram()   

 