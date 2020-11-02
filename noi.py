import pyttsx3

robot_brain = "I don't want to live forever"
robot_mouth = pyttsx3.init()
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()