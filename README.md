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

Steps are shown below as well:



After clicking on the above link, you will be directed to the below page -


<img width="1366" height="713" alt="Screenshot (304)" src="https://github.com/user-attachments/assets/4bb9e69d-b290-4913-80c5-6c2d4dbaf6ed" />


Generate App Password -


<img width="1366" height="689" alt="Screenshot (305)" src="https://github.com/user-attachments/assets/35b47c3f-1bf7-461d-b045-ff2af6efa273" />


Create a new Secret-Key -


<img width="1366" height="719" alt="Screenshot (303)" src="https://github.com/user-attachments/assets/8ca0c32e-be8b-40d5-8c1a-16810b2a97ef" />




5. **Enter the openai key**
 
   Enter the required email and phone number in main.py.

6. **Run the assistant**
   ```bash
   python main.py

## 📸 Screenshots & 📹 Demos

- #### Who are you?
- https://drive.google.com/file/d/13k1_-248IUHkOTU_A7r9b0WZi6NRuRl1/view?usp=drive_link

- #### DOB
- https://drive.google.com/file/d/1vbFVXr4aYtJ1JYA17YB_e9xEy9amWfdy/view?usp=drive_link
  
- #### WhatsApp message demo
- https://drive.google.com/file/d/15f4bn_Kz89KwfVix06DM1jTPpUtsPJdP/view?usp=drive_link

- #### Today's Time
- https://drive.google.com/file/d/1Y01pRiiSfY3lFDKPI2YHQ3rEDYKg39kW/view?usp=drive_link

- #### Today's Date
- https://drive.google.com/file/d/1VYPBaE9hVbMhaBcSe8-2bvXPtRC_6ADO/view?usp=drive_link

- #### Special Geetings
- https://drive.google.com/file/d/1oCtpfyM9zOkO4k6cxV3aqw-UdLBM2N5d/view?usp=drive_link

- #### Playing Bhajan
- https://drive.google.com/file/d/1QwsyXG7xn32oXihs-Dl8BnBHT9JXxvrl/view?usp=drive_link

- #### Playing music
- https://drive.google.com/file/d/16WpjVaIM5mIAp6o9vUTMJS0doW8yEW9A/view?usp=drive_link

- #### Open Youtube
- https://drive.google.com/file/d/1DpZ0SEhlf6gHFjmNI7zkYax0KVXSEUxR/view?usp=drive_link

- #### Tell a joke
- https://drive.google.com/file/d/1oSnX3dxK2Ba3ozhmhdgFHI78xqnoQhYO/view?usp=drive_link

- #### Image Generation
- https://drive.google.com/file/d/1JU2Vkv5s0mItgFXiq5ntdaerUkuwcQ7t/view?usp=drive_link

- #### Greetings
- https://drive.google.com/file/d/1SfMQHfJfcX8t8otxMWSvlyccgqh29cq1/view?usp=drive_link

- #### General Query
- https://drive.google.com/file/d/1Pbh3L9hZzVV2NbnDcYosApdPT-liBdhF/view?usp=drive_link

- #### Ask AI
- https://drive.google.com/file/d/1VYPBaE9hVbMhaBcSe8-2bvXPtRC_6ADO/view?usp=drive_link



## 🔐 AI/API Feature Notes
The assistant includes AI functionality such as:

- Asking Jarvis questions (ask ai)
- Generating images via text or speech

These are commented out due to OpenAI's API being paid. You can re-enable them by:

- Adding your OpenAI API key to user_config.py
- Uncommenting the relevant blocks in main.py and openai_request.py
