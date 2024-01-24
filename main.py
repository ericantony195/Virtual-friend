from characterai import PyCAI
import pyttsx3  
import elevenlabs
import speech_recognition as sr
import pyttsx3 
import time
import websocket
import json
import requests
from elevenlabs import set_api_key
from elevenlabs import generate, stream
set_api_key("7538bf315f70b94c5b394c8e9c23d230")

r = sr.Recognizer() 
 
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

engine = pyttsx3.init()  

client = PyCAI('7f5ad933e0d0c059ab4e5ebc45bb0e68dc801046')

char = "x1mc3N2Y8dYzFhGZAY5MD7EH4L9puOb6mrFqbNnpRb4"

chat = client.chat.get_chat(char)

participants = chat['participants']

if not participants[0]['is_human']:
    tgt = participants[0]['user']['username']
else:
    tgt = participants[1]['user']['username']
while True:
    with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
    message = MyText

    data = client.chat.send_message(
        chat['external_id'], tgt, message
    )

    name = data['src_char']['participant']['name']
    text = data['replies'][0]['text']

    '''engine.say(text)  
    # play the speech  
    engine.runAndWait()'''

    audio = elevenlabs.generate(
    text,
    voice = "Bella"
)   
    

    
    elevenlabs.play(audio)
    '''audio_stream = generate(
    text="This is a... streaming voice!!",
    stream=True
    )

    stream(audio_stream)    '''
    print(f"{name}: {text}")