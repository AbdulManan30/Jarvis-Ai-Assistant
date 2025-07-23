# core.py
import os
import queue
from gtts import gTTS
import pygame
import speech_recognition as sr
import requests
from client import (
    groqAi,
)  # Custom function that interacts with Groq AI for generating responses

recognizer = sr.Recognizer()
event_queue = queue.Queue()

def speak(text):
    tts = gTTS(text)
    tts.save("sound.mp3")
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("sound.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass
    os.remove("sound.mp3")

def getNews():
    api_key = "Your Api Key"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    if data["status"] == "ok":
        for article in data["articles"][:10]:
            speak(article["title"])
    else:
        speak("Failed to fetch news.")