import speech_recognition
import pyttsx3
from datetime import date, datetime
#khoi tao
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""
you = ""

while you != "bye":
       #nghe noi tu mic
       with speech_recognition.Microphone() as mic:
              print("Robot: i'm listening...")
              audio = robot_ear.listen(mic)
       #bat dau nhan dien giong noi
       print("Robot:...")
       
       try: 
              you = robot_ear.recognize_google(audio)
       except:
              you = "You don't say anything"
       
       print("You: " + you)
       
       #xu ly
       if you == "":
              robot_brain = "I can't hear you, try again"
       elif you == "hello":
              robot_brain = "hello ted"
       elif you == "what is today":
              robot_brain = date.today().strftime("%B %d, %Y")
       elif you == "what time is it now":
              robot_brain = datetime.now().strftime("%H:%M:%S")
       elif you == "who is the president of the United States":
              robot_brain = "Donald Trump"
       elif you == "bye":
              robot_brain = "goodbye"
       else:
              robot_brain = "I'm fine thank you, and you"
              
       print("Robot: " + robot_brain)
       
       #tra loi
       robot_mouth.say(robot_brain)
       robot_mouth.runAndWait()
