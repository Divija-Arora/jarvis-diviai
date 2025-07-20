import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk
import user_config
import smtplib, ssl



#import openai_request as ai
#import image_generation
import mtranslate # import mtranslate for language translation

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  # here 0 refers to id of voice
engine.setProperty("rate", 170) # setting the speed of speech


def speak(audio): # Speak function to output audio
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def command():
    content = " "
    while content == " ":
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            content = r.recognize_google(audio, language='en-in')
            content = mtranslate.translate(content,to_language="en-in")
            print("You Said............" + content)
        except Exception as e:
            print("Please try again...")
    
    return content

def main_process(): # Main assistant logic loop
    jarvis_chat = []
    while True:
        request = command().lower()
        if "hello" in request: # Greetings
            speak("Welcome, How can i help you.")
        elif "play music" in request: # Play random music
            speak("Playing music")
            song = random.randint(1,3)
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=rWfAwsf4gLk&list=RDrWfAwsf4gLk&start_radio=1")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=tC_OcVCndi8&list=RDtC_OcVCndi8&start_radio=1")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=U6cPjurCOmQ&pp=ygUUY29weXJpZ2h0IGZyZWUgbXVzaWM%3D")
        # Tell time and date
        elif "say time" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            speak("Current time is " + str(now_time))
        elif "say date" in request:
            now_time = datetime.datetime.now().strftime("%d:%m")
            speak("Current date is " + str(now_time))
        # To-do list features
        elif "new task" in request:
            task = request.replace("new task", "")
            task = task.strip()
            if task != "":
                speak("Adding task : "+ task)
                with open ("todo.txt", "a") as file:
                    file.write(task + "\n")
        elif "speak task" in request:
            with open ("todo.txt", "r") as file:
                speak("Work we have to do today is : " + file.read())
        elif "show work" in request:
            with open ("todo.txt", "r") as file:
                tasks = file.read()
            notification.notify(
                title = "Today's work",
                message = tasks
            )
        elif "open youtube" in request:
            webbrowser.open("www.youtube.com")
        elif "open" in request:
            query = request.replace("open", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")
        elif "wikipedia" in request:
            request = request.replace("jarvis ", "")
            request = request.replace("search wikipedia ", "")
            result = wikipedia.summary(request, sentences=2)
            speak(result)

        elif "search google" in request: # Google search
            request = request.replace("jarvis ", "")
            request = request.replace("search google ", "")
            webbrowser.open("https://www.google.com/search?q="+request)
        elif "send whatsapp" in request: # Send WhatsApp message
            pwk.sendwhatmsg("+91XXXXXXXXXX", "Hi, How are you", 2, 10, 30)
        # elif "send email" in request:
        #     pwk.send_mail("xxxxx@xgmail.com", user_config.gmail_password, "Hello", "Hello, How are you", "xxxxx@xgmail.com")
        #     speak("Email sent")
        elif "send email" in request:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("xxxx@gmail.com", user_config.gmail_password)
            message = """
            This is a message sent from diviai using Python
            Thanks by Diviai.

            """
            s.sendmail("xxxx@gmail.com", "xxxx@gmail.com", message)
            s.quit()
            speak("Email sent")

        # elif "image" in request:
        #     request = request.replace("jarvis ", "")
        #     image_generation.generate_image(request)

        elif "image" in request:
            speak("Image generation is not available right now.")

        # elif "ask ai" in request:
        #     jarvis_chat = []
        #     request = request.replace("jarvis ", "")
        #     request = request.replace("ask ai ", "")
        #     jarvis_chat.append({"role": "user","content": request})

        #     response = ai.send_request(jarvis_chat)

        #     speak(response)

        elif "ask ai" in request:
            speak("AI functionality is not right now. I can still answer basic commands.")

        elif "clear chat" in request:
            jarvis_chat = []
            speak("Chat Cleared")
        elif "how are you" in request:
            speak("I'm fine, thanks for asking!")

        elif "time" in request:
            time_now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time_now}")

        elif "date" in request:
            today = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's date is {today}")


        elif "who are you" in request or "whose model are you" in request or "what are you" in request:
            speak("I am Jarvis - diviai , Divija Arora's personal assistant.")

        elif "your date of birth" in request or "when were you born" in request:
            speak("I was created on July 17th, 2025, by Divija Arora.")


        elif "who is" in request or "what is" in request:
            try:
                result = wikipedia.summary(request, sentences=2)
                speak(result)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("Your question is too broad. Can you please be more specific?")
            
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any information on that topic.")
            
            except Exception as e:
                speak("Hmm, something went wrong while searching. Please try again.")

        elif "tell me a joke" in request:
            speak("Why don't scientists trust atoms? Because they make up everything!")

        elif "open youtube" in request:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")

        elif "radha soami ji" in request or "radha swami ji" in request or "radha soami" in request:
            speak("Radha Soami ji, Babaji bless you.")

        # Play bhajan
        elif "play bhajan" in request:
            speak("Playing a bhajan for you on YouTube.")
            pwk.playonyt("bhajan")

        # Default
        else:
            # request = request.replace("jarvis ", "")

            # jarvis_chat.append({"role": "user","content": request})
            # response = ai.send_request(jarvis_chat)

            # jarvis_chat.append({"role": "assistant", "content": response})
            # speak(response)
           
            speak("Sorry, I'm still learning. I can't answer that right now. Please try something else.")




if __name__ == "__main__":
    main_process()
