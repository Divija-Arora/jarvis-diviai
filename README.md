# jarvis-diviai
## 📌 Description
**Jarvis - Diviai** is a desktop-based personal voice assistant built using Python. It performs tasks such as playing music, responding to voice commands, searching Wikipedia or Google, managing a to-do list, sending WhatsApp messages, and more.

This project also includes integrated AI features like natural language conversation (ChatGPT API) and image generation. However, due to paid API restrictions, these features are currently commented out. The code is ready and functional for anyone with access to premium API keys to enable them.


---

## ✨ Features

- 🎙️ Speech recognition and voice responses  
- 📅 Tell current date and time  
- 🎵 Play music or bhajans on YouTube  
- 📖 Search content using Wikipedia or Google  
- 📝 Manage To-Do list (add, speak, or show tasks)  
- 📲 Send WhatsApp messages using `pywhatkit`  
- 📧 Send emails using SMTP  
- 🙋 Respond to basic questions like "How are you?" or "Who are you?"  
- 🔊 Understand and respond in Hindi using translation  
- 💡 Personalized as **Diviai** – Divija Arora's voice assistant  
- 🤖 ChatGPT-based conversation system (**commented out**)  
- 🖼️ AI Image generation using prompts (**commented out**)  

---

## 🛠️ Tech Stack / Technologies Used

| Category                | Technology / Library             |
|-------------------------|----------------------------------|
| 💬 Speech Synthesis     | `pyttsx3`                        |
| 🎤 Speech Recognition   | `speech_recognition`, `pyaudio` |
| 🌐 Web Browsing         | `webbrowser`, `pywhatkit`        |
| 📚 Knowledge Base       | `wikipedia`                     |
| 📝 Task Management      | File handling (`todo.txt`)      |
| 🔔 Notifications        | `plyer`                          |
| 📧 Email                | `smtplib`, `ssl`                 |
| 📲 WhatsApp Messaging   | `pywhatkit.sendwhatmsg()`        |
| 🌐 Translation          | `mtranslate`                    |
| ⌨️ Automation           | `pyautogui`                      |
| 🤖 *AI Chat (Optional)* | `openai` (ChatGPT API - commented)
| 🖼️ *Image Gen (Optional)* | `openai` (DALL·E API - commented)

---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/Divija-Arora/jarvis-diviai.git
   cd jarvis-diviai

2. **Create virtual environment & activate it**
   ```bash
   python -m venv env_jarvis
   env_jarvis\Scripts\activate  # On Windows

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

4.	**In user_config.py**
	- Enter the gmail app password (this is not the gmail login password. You have to generate app password  to send emails from python.) 
	- Follow following steps : https://itsupport.umd.edu/itsupport?id=kb_article_view&sysparm_article=KB0015112

Create a new Secret-Key
<img width="1366" height="719" alt="Screenshot (303)" src="https://github.com/user-attachments/assets/8ca0c32e-be8b-40d5-8c1a-16810b2a97ef" />




5. **Enter the openai key**
 
   Enter the required email and phone number in main.py.

6. **Run the assistant**
   ```bash
   python main.py

## 📸 Screenshots & 📹 Demos
- 🎥 [ ] main_screen.mp4 - Shows command and response

- 🖼️ [ ] Screenshot showing to-do list functionality

- 📤 [ ] WhatsApp message demo

- 🔊 [ ] Audio interaction snippet


## 🔐 AI/API Feature Notes
The assistant includes AI functionality such as:

- Asking Jarvis questions (ask ai)
- Generating images via text or speech

These are commented out due to OpenAI's API being paid. You can re-enable them by:

- Adding your OpenAI API key to user_config.py
- Uncommenting the relevant blocks in main.py and openai_request.py
