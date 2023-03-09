import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import pyjokes
import random 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!!")
    speak("sir i am ROBERT, i am your personal assistent, please tell me how may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please....")
        return "None"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('YOUR EMAIL', 'PASSWORD')
    server.sendmail('YOUR EMAIL',to,content)
    server.close()

def play_game():
    import guess_game
    speak("Welcome to the Game of Guesses, Here computer will genrate a number and you have to guess a number, (Press Enter to Start)")
    start = str(input())
    if start == "":
        speak("Select the level of the game, Say 'Hard' or 'Easy': ")
        lvl = takeCommand().lower()
        if 'easy' in lvl:
            speak("Enter the number you want the computer to genrate number below: ")
            a = int(input("Number you want the computer to genrate the guessig number below : "))
            #randomNum = random.randint(0, a)
            guess_game.guess(random.randint(0, a))
            speak('Congratulations sir, you won!')
        elif 'hard' in lvl:
            #randomNum = random.randint(0, 100)
            guess_game.guess(random.randint(0, 100))
            speak('Congratulations sir, you won!')
        else:
            speak("the game severs are offline, please try agian later")
    else:
        print("Thank you!")


if __name__ == "__main__":
    wishMe()
    chrome_path = 'C://Program Files//Google//Chrome//Application//chrome.exe %s'
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia.....")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'what can you do' in query:
            speak("Try me sir!,i can open websites for you such as, google.com, youtube.com, i can calculate, i can tell you jokes, we can play game and much more")
        elif 'fuck you' in query:
            speak("Fuck you too sir!")
        elif 'close' in query:
            speak('Powering OFF')
            exit()
        elif 'open youtube' in query:	
            webbrowser.get(chrome_path).open("youtube.com")
        elif 'open google' in query:
            webbrowser.get(chrome_path).open("google.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            '''elif 'email to' in query:
            try:
                speak("What should i say to romil?")
                content = takeCommand()
                to = "RECIVER EMAIL"
                sendEmail(to, content)
                speak('Email has been sent!')
            except Exception as e:
                print(e)
                speak("Sorry my friend romil bhai, i am not able to send the E-Mail")'''

        elif 'joke' in query:
            joke = pyjokes.get_joke(language="en", category="neutral")
            print(joke)
            speak(joke)
        elif 'calculator' in query:
            import CalcGUI
        elif 'play a game' in query:
            play_game()
        elif 'calculate' in query:
            query = query.replace('calculate',"")
            speak(eval(query))
        elif 'how are you' in query:
            speak("i am good sir how are you")
        elif 'i am good' in query:
            speak("glad to hear sir")
        elif 'hi' in query:
            speak("Hello sir")