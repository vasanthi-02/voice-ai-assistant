import speech_recognition as sr
from gtts import gTTS
import os

print("🚀 Voice AI Starting...")

def speak(text):
    print("AI:", text)
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("start response.mp3")

def listen():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("🎤 Microphone opened...")
            r.adjust_for_ambient_noise(source, duration=1)
            print("🎤 Listening...")
            audio = r.listen(source, timeout=5, phrase_time_limit=5)

        text = r.recognize_google(audio)
        print("You:", text)
        return text

    except Exception as e:
        print("ERROR:", e)
        return "error"

def generate_response(text):
    return "You said: " + text

print("🔁 Entering loop...")

while True:
    user_input = listen()

    if user_input == "error":
        speak("I had trouble hearing you")
        continue

    if "exit" in user_input.lower():
        speak("Goodbye!")
        break

    response = generate_response(user_input)
    speak(response)