# main.py
from flask import Flask, render_template, request, jsonify, Response
import threading
from core import speak, event_queue, recognizer
from process_command import processCommand
import speech_recognition as sr


app = Flask(__name__)

def main():
    speak("Jarvis is activated")

    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Listening for wake word...")
                event_queue.put("Listening for wake word...")
                audio = recognizer.listen(source)
                wake = recognizer.recognize_google(audio)

                if "jarvis" in wake.lower():
                    speak("Yes Sir")
                    event_queue.put("Listening for your command...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    print("Command received:", command)
                    event_queue.put(f"Command received: {command}")
                    processCommand(command)
                else:
                    speak("Sorry, I didn't catch that.")

        except Exception as e:
            print("Error:", str(e))
            event_queue.put(f"Error: {str(e)}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-jarvis', methods=['POST'])
def run_jarvis():
    thread = threading.Thread(target=main)
    thread.start()
    return jsonify({'message': 'Jarvis activated!'})

@app.route('/events')
def events():
    def stream():
        while True:
            message = event_queue.get()
            yield f"data: {message}\n\n"
    return Response(stream(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)