# 🤖 Jarvis AI Assistant

A voice-activated AI assistant built using Python, Flask, and speech recognition libraries. Jarvis listens to your voice commands and performs actions like opening apps, playing music, reading news, and interacting with AI (via Groq API).

---

## 🚀 Features

- 🎤 Wake word detection (say “Jarvis” to activate)
- 💬 Converts speech to text and vice versa
- 🌐 Opens websites and desktop applications
- 📁 Opens folders like Downloads, Documents, Music, etc.
- 🔉 Controls system volume (up, down, mute)
- 📰 Speaks latest news headlines (using News API)
- 🎵 Plays songs using predefined YouTube links
- 🧠 Responds to custom queries using Groq AI
- 🖥️ Web interface using Flask with dark UI and wave effects
- 
---

## 📁 Folder Structure
```
Jarvis-Ai-Assistant/
├── app.py / main.py # Flask app & assistant logic
├── process_command.py # Handles voice command execution
├── musicLibrary.py # Custom music links
├── templates/
│ └── index.html # Frontend page
├── static/
│ └── styles.css # Wave animation & dark theme
└── README.md
```

---

## ⚙️ Installation

Follow these steps to run the assistant on your machine:

### 1. Clone the repository

git clone https://github.com/AbdulManan30/Jarvis-Ai-Assistant.git
cd jarvis-ai-assistant

### 2. Create a virtual environment

python3 -m venv .venv
source .venv/bin/activate     # For Linux/macOS
### OR
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

### For News API
api_key = "YOUR-NEWSAPI-KEY"

### For Groq
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

📝 License
This project is for educational purposes only.
APIs used are subject to their individual license agreements (Groq, NewsAPI).

🙋‍♂️ About Me
Abdul Manan
💻 Frontend Developer & Python Enthusiast
📧 Contact: abdul.manan232332@gmail.com
🌐 GitHub: https://github.com/AbdulManan30

### Thanks for visiting.


