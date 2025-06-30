import webbrowser
import os
import pyaudio
import speech_recognition as sr
from gtts import gTTS
import pygame
import sys
import contextlib


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


if __name__ == "__main__":
    speak("eldric is online")
    while True:
        with sr.Microphone() as source:
            print("🎙️ Listening...")
            audio = recognizer.listen(source, timeout=1)

        try:
            text = recognizer.recognize_google(audio)
            print("✅ You said:", text)
            if "eldric" in text.lower():
                speak(f"You said: {text}")
        except sr.UnknownValueError:
            print("❌ Could not understand audio")
            speak("Sorry, I could not understand that.")
        except sr.RequestError:
            print("❌ Google API error")
            speak("Network error while accessing Google API.")
