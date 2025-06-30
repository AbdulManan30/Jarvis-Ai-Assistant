import webbrowser  # For opening websites in the default browser
import os  # For file operations like deleting temporary audio files
import pyaudio  # Required for microphone access (dependency for speech recognition)
import speech_recognition as sr  # Library for converting speech to text
from gtts import gTTS  # Google Text-to-Speech library to convert text into audio
import pygame  # Used to play audio files
import musicLibrary  # Custom module that contains a dictionary of music links
import requests  # To make HTTP requests (used for fetching news)
from client import (
    groqAi,
)  # Custom function that interacts with Groq AI for generating responses

recognizer = sr.Recognizer()  # Create a recognizer object to handle speech input


# Function to convert text to speech and play it
def speak(text):
    tts = gTTS(text)  # Convert the given text to a speech object
    tts.save("sound.mp3")  # Save the speech as an mp3 file

    pygame.init()  # Initialize pygame
    pygame.mixer.init()  # Initialize the mixer for audio playback

    pygame.mixer.music.load('sound.mp3')  # Load the mp3 file
    pygame.mixer.music.play()  # Play the loaded audio

    while pygame.mixer.music.get_busy():
        pass  # Wait until the audio playback is complete
    os.remove("sound.mp3")  # Delete the audio file after playback


# Function to fetch and speak the latest news headlines
def getNews():
    api_key = "Your Api Key"  # Replace with your actual NewsAPI key
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"  # API endpoint
    response = requests.get(url)  # Make a GET request to the news API

    data = response.json()  # Convert the response to JSON format

    if data["status"] == "ok":  # If the request was successful
        articles = data["articles"]  # Get the list of articles
        for i, article in enumerate(
            articles[:15], start=1
        ):  # Loop through top 15 articles
            speak(article["title"])  # Speak out the title of each article
    else:
        print(
            "Failed to fetch news:", data["message"]
        )  # Print the error message if request fails


# Function to process user commands and take appropriate action
def processCommand(c):
    if "open" in c.lower():  # If the command includes 'open'
        webbrowser.open(
            f'https://{c.split(" ")[1]}.com'
        )  # Open the second word as a website
    elif c.lower().startswith("play"):  # If the command starts with 'play'
        song = c.lower().split(" ")[1]  # Get the name of the song
        link = musicLibrary.music[song]  # Retrieve the song link from the music library
        webbrowser.open(link)  # Open the song link in the browser
    elif "news" in c.lower():  # If the command includes 'news'
        getNews()  # Call the getNews function
    else:
        response = groqAi(c)  # Send the command to Groq AI to get a response
        speak(response)  # Speak the response received from the AI


# Main block that starts the program
if __name__ == "__main__":
    speak("Hi Sir Manan, Jarvis is activated")  # Initial welcome message
    while True:  # Run continuously
        with sr.Microphone() as source:  # Use the microphone as the input source
            print("Listening...")
            audio = recognizer.listen(source)  # Listen for any speech input

        try:
            with sr.Microphone() as source:  # Use the mic again to detect wake word
                print("Listening...")
                audio = recognizer.listen(source)  # Capture the audio
            word = recognizer.recognize_google(audio)  # Convert audio to text
            if word.lower() == "jarvis":  # If the word "jarvis" is detected
                speak("Yes")  # Respond verbally

                # Listen for the actual user command
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = recognizer.listen(source)  # Listen again for full command
                    command = recognizer.recognize_google(
                        audio
                    )  # Convert command to text
                    processCommand(command)  # Handle the command accordingly

        except Exception as e:  # Handle any recognition or microphone errors
            speak(
                "Sorry , I didn't catch that, can you repeat?"
            )  # Respond with an error message
