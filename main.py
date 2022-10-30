import speech_recognition as sr
import os
import sys
import webbrowser


def talk(words):
    print(words)
    os.system("say " + words)  #


talk("Привет, спроси у меня что-либо!")


def command():
    r = sr.Recognizer
    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio).lower()
        print("Вы сказали " + text)
    except sr.UnknownValueError:
        talk("Я вас не поняла")
        text = command()
    return text


def makeSomething(text):
    if 'открой ютуб' in text:
        talk("Уже открываю")
        url = "https://www.youtube.com/"
        webbrowser.open(url)
    elif 'stop' in text:
        talk("Да, конечно, без проблем")
        sys.exit()
    elif 'имя' in text:
        talk("Меня зовут Полинусик - Жопусик")
        sys.exit()

while True:
    makeSomething(command())