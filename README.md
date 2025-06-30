# 🤖 Jarvis AI Assistant

**Jarvis** is a Python-based voice assistant that performs tasks based on your speech commands. Powered by **speech recognition**, **gtts voices**, **Groq AI for natural language replies**, and **live news updates**, Jarvis acts like your personal AI companion — just like Iron Man's assistant!

It listens for the keyword `"Jarvis"` and responds smartly using voice.

---

## 🧩 Features

- 🗣️ Wake word detection: Say “Jarvis” to activate
- 🔍 Ask any question and get a spoken reply via Groq LLaMA models
- 📰 Fetch top 15 news headlines and read them aloud
- 🎵 Play music by name (from YouTube links)
- 🌐 Open websites by saying “Open YouTube”, “Open Google”, etc.
- 🎧 Text-to-speech powered by ElevenLabs API (with realistic voices)

---

## ⚙️ Installation

Follow these steps to run the assistant on your machine:

### 1. Clone the repository

git clone https://github.com/yourusername/jarvis-ai-assistant.git
cd jarvis-ai-assistant

### 2. Create a virtual environment

python3 -m venv .venv
source .venv/bin/activate     # For Linux/macOS
# OR
.venv\Scripts\activate        # For Windows

### 3. Install dependencies

pip install -r requirements.txt


### 4. 🔑 API Keys Required

| Service    | Link to Get API Key                                      |
| ---------- | -------------------------------------------------------- |
| Groq       | [https://console.groq.com/](https://console.groq.com/)   |
| News API   | [https://newsapi.org/](https://newsapi.org/)             |

### 5. Replace in code:
Update these lines with your actual keys:

# For News API
api_key = "YOUR-NEWSAPI-KEY"

# For Groq
client = Groq(api_key="YOUR-GROQ-KEY")

### 6. Example Usage
python main.py

Then say:
Jarvis → wakes the assistant
What is gravity? → answered by Groq LLaMA
Play ijazat → opens music
Read news → reads headlines
Open github → opens GitHub in browser
Jarvis listens, processes your command, and replies using gtts voice output.

### 7. 📦 Project Structure
📁 jarvis-ai-assistant/
├── main.py           # Main assistant script
├── client.py         # Groq integration
├── musicLibrary.py   # Music links dictionary
├── .venv/            # Python virtual environment
├── README.md         # This file
└── requirements.txt  # All dependencies

📝 License
This project is for educational purposes only.
APIs used are subject to their individual license agreements (Groq, NewsAPI).

### Thanks for visiting.


