text_input = "first time i'm using a package in next.py course"

#step 1 - need to install package - pip install pyttsx3
#step 2 - need to install package - pip install pywin32

import pyttsx3
engine = pyttsx3.init()
engine.say(text_input)
engine.runAndWait()