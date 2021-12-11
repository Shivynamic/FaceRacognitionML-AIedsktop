import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import cv2
import random
import requests
import pywhatkit as kit
import sys
from requests import get
import pyjokes
import pyautogui
import email.mime
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import instaloader
import time
import operator
import PyPDF2
from bs4 import BeautifulSoup
from pywikihow import search_wikihow 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[6].id)
#--------------------to control rate of speech-------
#  engine.setProperty('rate',100)


# >>>>>>>>>> pip install psutil
# -----------import psutil------
#elif "battery percentage" in query or "how much power left" in query:
# battery = psutil.sensors_battery() 
# percentage = battery.percent
# speak(f"mam our system has {percentage} percent battery")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!") 
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")
    speak("Hi There! My name is Alpha. I am a virtual assisstent. I would help you with the task you want me to complete")

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio =r.listen(source)
    
    try:
        print("Still Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    query = query.lower()
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("pamy5421@gmail.com","shivangi@1305")
    server.sendmail('pamy5421@gmail.com',to,content)
    server.close()

def news():
    main_url = 'http://newsapi.org/v2/top-hedlines?sources=techcrunch&apiKey=c5258db6a0f542c0bca7f013467281c2'

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head =[]
    day = ["first", "second", "third", "fourth","fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"The {day[i]} news is {head[i]}")


def pdf_reader():
    # Book name to be entered
    
    book = open('-------------bookname---.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in this book {pages}")
    speak("Mam! Enter the pagenumber you want me to read")
    pg = int(input("Page number here: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)



if __name__ == "__main__":
    speak("This is the Future. Welcome!")
    greetMe() 
    while True:
    
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Mam! What you want me to search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
        
        elif 'send message' in query:
            kit.sendwhatmsg("+918770010691", "A computer generated message is being sent to you.",21,45)
        
        elif "play song on youtube" in query:
            kit.playonyt("Starboy")

        elif 'internet speed' in query:

            import speedtest
            st = speedtest.Speedtest()
            dl= st.download()
            up = st.upload()
            speak(f"Mam This system's downloading speed is {dl}bit per second and its uploading speed is {up}bit per second")
        

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir ='C:\\Users\\shiva\\OneDrive\\Desktop\\Songs\\Songs 2021'
            songs = os.listdir(music_dir)
            # print(songs)
            rd= random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif 'time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam! Right now it is {strTime}")
        
        elif 'open code' in query:
            codepath = "C:\\Users\\shiva\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'mail to shivi' in query:
            try:
                speak("What is the message?")
                content = takeCommand()
                to = "pamy5421@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("OOps ! The email couldnt be delivered")
        elif 'email to shivangi' in query:
            speak("What is to be sent?")
            query = takeCommand().lower()
            if "send attachment" in query:
                email = 'pamy5421@gmail.com'
                password = 'shivangi@1305'
                send_to_email = 'pamy5421@gmail.com'
                speak("Okay mam! what is the subject of this email")
                query = takeCommand().lower()
                subject = query
                speak("and mam, what is the message for this email")
                query2 = takeCommand().lower()
                message = query2
                speak("Mam please provide the path of the file in the shell")
                file_location = input("please enter the path here:")

                speak("please hold on while I am sending the mail")

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message, 'plate'))


                filename =os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application','octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment: filename-%s" %filename)
                
                msg.attach(part)
                server = smtplib.SMTP('smtp.gmail.coom',587)
                server.starttls()
                server.login(email, password)
                text =msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("email has been sent successfully")
            else:
                email = 'pamy5421@gmail.com'
                password = 'shivangi@1305'
                send_to_email = 'pamy5421@gmail.com'
                message = query

                server = smtplib.SMTP('smtp.gmail.coom',587)
                server.starttls()
                server.login(email, password)
                text =msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("email has been sent successfully")

        elif 'temperature'in query:
            search = "temperature in indore" 
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif "activate how to do mode" in query:
            speak("How to do is activated now!!")
            time.sleep(1)
            speak("Mam! please tell me what you wanna know")
            how = takeCommand()
            max_results=1
            how_to =search_wikihow(how, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)

        
        
        
        
        
        elif 'open notepad' in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
        elif 'open command prompt' in query:
            os.system("start cmd")
        elif 'open camera' in query:

            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        
        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'close notepad' in query:
            speak("Closing notepad")
            os.system("taskkill /f /im notepad.exe")
        
        elif 'set alarm' in query:
            nn = int(datetime.datetime.now().hour)
            if nn== 22:
                music_dir ='C:\\Users\\shiva\\OneDrive\\Desktop\\Songs\\Songs 2021'
                songs = os.listendir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
        
        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        
        elif 'news' in query:
            speak("Wait while I am fetching the news mam!")
            news()
        
        elif 'shut down the system' in query:
            os.system("shutdown /s /t 5")
        
        elif 'where am i' in query or 'my location' in query:
            speak("Wait mam! Let me fetch some data")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"Mam as per the data that I am able to fetch, you are in {city} city of {country}")
            except Exception as e:
                speak("Sorry Mam! Unable to get the data right now")
                pass

        
        elif 'instagram profile' in query or 'insta profile' in query:
            speak("Mam please enter the username of the profile you want to visit")
            name = input("Enter username: ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Mam here is the user named {name}'s profile")
            time.sleep(5)
            speak("Mam would you like to download profile picture of this account?")
            condition = takeCommand().lower()
            if 'yes' in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only =True)
                speak("I am done mam, profile picture is saved in your main folder. Ready to perform another task!!")

            else:
                pass

        elif 'take screenshot' in query or 'screenshot' in query:
            speak("Mam, please tell me the name for this screenshot file")
            name = takeCommand().lower()
            speak("Stay on the screen for a sec while I am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("The screenshot is saved. I am ready for next task")

        elif 'read pdf' in query:
            pdf_reader()

        elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
            speak("mam please tell me if you want to hide this folder or make it visible for everyone")
            condition =takeCommand().lower()
            if "hide" in condition:
                os.system("attrib +h /s /d")
                speak("mam all files in this folder are now hidden")

            elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak("mam, all files in this folder are visible now") 

            elif "do some calculation" in query or "calculations" in query or "calculate" in query:
                r = sr. Recognizer()
                with sr. Microphone() as source:
                    speak("what you want to calculate mam?")
                    print("Listening........")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string = r.recognize_google()
                print(my_string)
                def get_operator_fn(op):
                    return{
                        '+' : operator.add,
                        '-' : operator.sub,
                        'x' : operator.mul,
                        'dividend' : operator.__truediv__,
                    }[op]
                
                def eval_binary_expr(op1, oper , op2):
                    op1, op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                speak("your result is")
                speak(eval_binary_expr(*(my_string.split())))


        elif 'alarm' in query:
            speak("Mam! Tell me the time to set alarm. You need to say set alarm to time")
            tt= takeCommand()
            tt = tt.replace("set alarm to","")
            tt = tt.replace(".","")
            tt = tt.upper()
            import MyAlarm
            MyAlarm.alarm(tt)



        elif 'open mobile camera' in query:
            import urllib.request
            import cv2
            import numpy as np
            import time
            URL ="http://192.168.29.150:8080/shot.jpg"
            while True:
                img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype = np.uint8)
                img = cv2.imdecode(img_arr,-1)
                cv2.imshow('IPWebcam',img)
                q= cv2.waitKey(1)
                if q== ord("q"):
                    break;
            cv2.destroyAllWindows()



        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")
        
        
               
        elif 'no thank you' in query:
            speak('Have a good day Mam!. Hope to see you back again!')  
            sys.exit() 
        
        elif 'thanks alpha' in query:
            speak("Its my Pleasure mam! glad to help!")

        speak("Anything else mam?")