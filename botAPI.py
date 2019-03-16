import json
import apiai
import urllib.request
from urllib.parse import quote_plus

CLIENT_ACCESS_TOKEN = '07dffa75a2404bc59cb0101655d300e9'

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
    return data['result']['fulfillment']['speech'] + "\n"

while True:
    #print("User: ")
    user_input = str(input("User: "))
    bot_response = botResponseReciever(user_input)
    print("\nVision: " + str(bot_response))