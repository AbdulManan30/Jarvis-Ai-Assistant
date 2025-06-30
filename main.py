import webbrowser
import os
import pyaudio
import speech_recognition as sr
from gtts import gTTS
import pygame
import sys
import contextlib
import musicLibrary
import requests
from client import groqAi


# Error suppression function
@contextlib.contextmanager
def suppress_stderr():
    with open(os.devnull, "w") as devnull:
        old_stderr = sys.stderr
        sys.stderr = devnull
        try:
            yield
        finally:
            sys.stderr = old_stderr


recognizer = sr.Recognizer()


def speak(text):
    tts = gTTS(text)
    tts.save("sound.mp3")

    with suppress_stderr():
        pygame.init()
        pygame.mixer.init()

    pygame.mixer.music.load("sound.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pass  # Wait until the audio finishes
    os.remove("sound.mp3")


def getNews():
    api_key = "Your Api Key"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)

    # Convert to JSON
    data = response.json()

    # Check for errors
    if data["status"] == "ok":
        articles = data["articles"]
        for i, article in enumerate(articles[:15], start=1):  # Show top 15 news]
            speak(article["title"])
    else:
        print("❌ Failed to fetch news:", data["message"])


def processCommand(c):
    if "open" in c.lower():
        webbrowser.open(f'https://{c.split(" ")[1]}.com')
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        getNews()
    else:
        # let groqAI handle the request
        response = groqAi(c)
        speak(response)


if __name__ == "__main__":
    speak("Hi Sir Manan, Jarvis is activated")
    while True:
        with sr.Microphone() as source:
            print("🎙️ Listening...")
            audio = recognizer.listen(source)

        try:
            with sr.Microphone() as source:
                print("🎙️ Listening...")
                audio = recognizer.listen(source, phrase_time_limit=1)
            word = recognizer.recognize_google(audio)
            print("✅ You said:", word)
            if word.lower() == "jarvis":
                speak("Yes")
                # Listen for a command
                with sr.Microphone() as source:
                    print("🎙️ Listening...")
                    audio = recognizer.listen(source, phrase_time_limit=1)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            speak("Sorry , I didn't catch that, can you repeat?")
