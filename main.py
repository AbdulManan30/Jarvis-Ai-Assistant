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

    pygame.mixer.music.load("sound.mp3")  # Load the mp3 file
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
# Entry point of the program
if __name__ == "__main__":
    speak(
        "Hi Sir Manan, Jarvis is activated"
    )  # Speak a welcome message when the assistant starts

    while True:  # Run the assistant continuously
        try:
            # Use the microphone as the input source
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(
                    source
                )  # Adjust for background noise
                print(
                    "Listening for wake word..."
                )  # Prompt for the wake word (e.g., "Jarvis")
                audio = recognizer.listen(source)  # Listen to the microphone
                wake = recognizer.recognize_google(audio)  # Convert speech to text

                if "jarvis" in wake.lower():  # If the wake word "jarvis" is detected
                    speak("Yes Sir")  # Respond with a confirmation
                    print(
                        "Listening for your command..."
                    )  # Prompt for the actual command
                    audio = recognizer.listen(
                        source
                    )  # Listen again for the user's command
                    command = recognizer.recognize_google(
                        audio
                    )  # Convert command speech to text
                    print("Command received:", command)  # Print the recognized command
                    processCommand(
                        command
                    )  # Process the command with appropriate logic

        except Exception as e:
            print("Error:", str(e))  # Print the error for debugging
            speak(
                "Sorry, I didn't catch that."
            )  # Respond if there was an error in recognition
