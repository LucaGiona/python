from textblob import TextBlob
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Langsamer

voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc==9.0.1"

engine.say("what should I dowith you I dont know?")
engine.runAndWait()

# blob = TextBlob("I really hate you so much more")
# print(blob.sentiment)

print("Enter your emplyee wellness statement: ")
phrase = input("> ")
blob = TextBlob(phrase)

while blob.sentiment.polarity < 0.5:
    print("More positive please: ")
    phrase = input("> ")
    blob = TextBlob(phrase)