import os, pyautogui, random, socket, wikipedia, cv2 
import time
import playsound
import urllib3
import speech_recognition as sr

from gtts import gTTS
from datetime import datetime
from art import *
from sys import stdout

from face_recognition import faceRecognition
from camera import cam


urllib3.disable_warnings()

now_time = datetime.now()
currentTime = now_time.strftime("%H:%M:%S")
aleyna_version = "1.1"

# Function to detect mic
def speak(audioString):
    print(audioString)
    num=0
    num += 1
    tts = gTTS(text=audioString, lang='en')
    file = str(num)+".mp3"
    tts.save(file)
    playsound.playsound(file, True)
    os.remove(file)

# Record Mic
def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)

    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    print("returning data")
    return data


def aleyna(data):
    
    if "open code" in data:
        pyautogui.hotkey('ctrl', 't')
        time.sleep(2)
        os.system('cd /home/tim/Dokumente/projects/Virtual_assistant')
        os.system('code .')

    elif "introduce yourself" in data:
        speak("I am aleyna. Tims personal Desktop assistant. I am currently on version " + aleyna_version + " I am able to manage and automate a lot of tasks. Here is a demonstration")
        os.system('io.elementary.terminal -n')
        os.system("cd /home/tim/Dokumente(Virtual_assistant")
        os.system("python aleyna_introduction.py")
        time.sleep(4)
        pyautogui.hotkey('alt', 'f4')
        pyautogui.press('left')
        time.sleep(1)
        pyautogui.press('enter')
        speak("I can as well start a program")  
        os.system("io.elementary.terminal -n")
        time.sleep(3)
        pyautogui.typewrite('blender')
        pyautogui.press('enter')
        time.sleep(4)
        pyautogui.hotkey('alt', 'f4')
        speak("Or control the camera")
        cam("Here is Aleyna")
        time.sleep(3)
        pyautogui.hotkey('alt', 'f4')

    elif "hostname" in data:
        hname = socket.gethostname()
        ip = socket.gethostbyname(hname)
        print("Host Name is:" + hname)
        print("Computer IP Address is:" + ip)
        speak("Your hostname is" + hname)
        speak("Your Ip Address is" + ip)

    elif "camera" in data:
        cam("webcam")        

    elif "discord" in data:
        os.system("io.elementary.terminal -n")
        time.sleep(3)
        pyautogui.typewrite("discord")
        pyautogui.press('enter')
        
    elif "what time is it" in data:
        speak("it is " + currentTime)


    elif "terminal" in data:
        print("Opening Terminal")
        pyautogui.hotkey('ctrl', 't')

    elif "zoom" in data:
        os.system("io.elementary.terminal -n")
        time.sleep(3)
        pyautogui.typewrite('zoom-client')
        pyautogui.press('enter')

    elif "blender" in data:
        os.system("io.elementary.terminal -n")
        time.sleep(3)
        pyautogui.typewrite('blender')
        pyautogui.press('enter')

    elif "discord" in data:
        os.system("io.elementary.terminal -n")
        time.sleep(3)
        pyautogui.typewrite("discord")
        pyautogui.press('enter')

    elif "whatsapp" in data:
        os.system("io.elementary.terminal -n")
        time.sleep(3)
        pyautogui.typewrite("whatsapp-for-linux")
        pyautogui.press('enter')

    elif "stop" in data:
        speak("Bye and take care!")
        quit()

    elif "power off" in data:
        print("Shutting down the pc...")
        speak("Goodbye Tim")
        os.system("poweroff")

    elif "reboot" in data:
        print("Rebooting the pc...")
        speak("I am rebooting now")  
        os.system("reboot")  



h = datetime.now().hour
h = h + 1


time.sleep(2)

print("firsttest")

while(True):
    data = recordAudio()
    aleyna(data)



