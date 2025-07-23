import webbrowser
import os
import subprocess
import psutil
from musicLibrary import music
from core import speak, event_queue, recognizer, getNews
from client import groqAi

def processCommand(c):
    c = c.lower()

    # Open website
    if "search" in c and ".com" not in c:
        try:
            webbrowser.open(f'https://{c.split(" ")[1]}.com')
        except Exception as e:
            speak("Sorry, I couldn't open the website.")
            event_queue.put(f"Error: {e}")

    # Play music
    elif c.startswith("play"):
        try:
            song = c.split(" ")[1]
            link = music.get(song)
            if link:
                webbrowser.open(link)
            else:
                speak("Sorry, I couldn't find that song.")
        except Exception as e:
            speak("Error playing the song.")
            event_queue.put(f"Music Error: {e}")

    # News
    elif "news" in c:
        getNews()

    # System Controls

    elif "shutdown" in c:
        speak("Shutting down the system.")
        os.system("shutdown now")

    elif "restart" in c:
        speak("Restarting the system.")
        os.system("reboot")

    elif "volume up" in c:
        os.system("pactl set-sink-volume @DEFAULT_SINK@ +10%")

    elif "volume down" in c:
        os.system("pactl set-sink-volume @DEFAULT_SINK@ -10%")

    elif "mute" in c:
        os.system("pactl set-sink-mute @DEFAULT_SINK@ toggle")

    elif "screenshot" in c:
        os.system("gnome-screenshot")
        speak("Screenshot taken.")

    # Close apps
    elif "close" in c:
        try:
            app_name = c.split(" ")[1]
            for proc in psutil.process_iter():
                if app_name in proc.name().lower():
                    proc.kill()
                    speak(f"{app_name} closed.")
                    break
        except Exception as e:
            speak("Error closing application.")
            event_queue.put(f"Close App Error: {e}")

    # Open application
    elif "open" in c and "application" in c:
        try:
            app_name = c.split(" ")[1].capitalize()
            subprocess.Popen([app_name])
            speak(f"{app_name} opened.")
        except Exception as e:
            speak(f"Could not open {app_name}.")
            event_queue.put(f"Application Error: {e}")

    # Open folders
    elif "open" in c and any(x in c for x in ["downloads", "documents", "music", "videos", "pictures", "desktop", "home"]):
        folder_map = {
            "downloads": "~/Downloads",
            "documents": "~/Documents",
            "music": "~/Music",
            "videos": "~/Videos",
            "pictures": "~/Pictures",
            "desktop": "~/Desktop",
            "home": "~"
        }

        for key in folder_map:
            if key in c:
                folder_path = os.path.expanduser(folder_map[key])
                subprocess.run(["xdg-open", folder_path])
                speak(f"Opening {key} folder")
                break

    # AI fallback
    else:
        response = groqAi(c)
        speak(response)
