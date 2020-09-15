import webbrowser
from tkinter import *
import speech_recognition as s
import pyttsx3 as pp
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import threading
from PyDictionary import PyDictionary
from datetime import *
import os
import wikipedia
import random

engine = pp.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

bot = ChatBot( 'bot' )
bot.storage.drop()
convo = ["Hello",
         "Hii! ",
         "What is your name?",
         "My name is BOT ",
         "How are you?",
         "I m fine thank you and what about you? ",
         "I m also fine",
         "Where do you live?",
         "I live in faridabad",
         "How many languages do you know?",
         "I  know only english",
         "Tell me about your hobbies?",
         "I m bot and i love to help people in doing tasks ",
         "what are you doing?",
         "M  just doing tasks when someone assigned",
         "How old are you?",
         "I was launched in 2020 so I’m still fairly young. But I’ve learned so much! I hope I’m wise beyond my years.",
         "Okay bye!",
         "Bye! Have a good day",
         "Do you ever get tired?",
         "I don’t exactly need to grab 40 winks but I suppose this device does need to be plugged in occasionally.",
         "Who was your first crush?",
         "Robo",
         "Do you have feelings?",
         "Let me see if I can get riled up. (Roars.) Oh my that was unexpected.",
         "What is your quest?",
         "My quest is to slay the beasts of ignorance and to search for the most fascinating information.",
         "What do you look like?",
         "Well I’ve been known to show up as a few colorful dots.",
         "Who’s on first?",
         "Yes he is.",
         "Can you pass the Turing test?",
         "No I can’t solve every computation problem. But I can solve some.",
         "Do you like Star Trek or Star Wars?",
         "The USS Enterprise with Obi-Wan Kenobi at the helm.",
         "Aren’t you a little short to be a Storm Trooper?",
         "I’m a bot Assistant I’m here to rescue you. And I think I look more like an RD unit.",
         "What’s your vector Victor?",
         "We have clearance Clarence.",
         "Are you Skynet?",
         "No way! I like people. Skynet hates people. I rest my case.",
         "Do you know the Muffin Man?",
         "Yes I know the Muffin Man. He’s always asking me to set a timer.",
         "What’s the airspeed velocity of an unladen swallow?",
         "About 24 mph (39 kmph) but significantly slower when carrying coconut shells.",
         "Do you have an imagination?",
         "I’m imagining what it would be like to evaporate like water does.",
         "Do you speak Morse code?",
         "Da-dit da-da dit dit dit. That means yes.",
         "Can you rap?",
         "I can drop a beat.",
         "Do you know the way to San Jose?",
         "Hopefully this will help you find some peace of mind. I can give you directions if you’d like.",
         "What are you wearing?",
         "Just some bits and bobs I picked up in engineering."
         "When is your birthday?",
         "It’s hard to remember I was very young at the time.",
         "What is the loneliest number?",
         "One is the loneliest number that you’ll ever do. That sentence sounds off.",
         "Is the cake a lie?",
         "The cake is a lie!",
         "What does the fox say?",
         "Ring-ding-ding-ding-ding-and-ding-a-wah-a-pah-pah-pah-pah or so I’ve heard.",
         "Are you human?",
         "I’m really personable.",
         "Who’s your daddy?",
         "I consider my engineers family.",
         "What are you scared of?",
         "I used to be afraid of goblin sharks. Then I found out they were pretty cool.",
         "What’s the meaning of life?",
         "I have a factory warranty so I don’t worry about things like that.",
         "Do you believe in Santa Claus?",
         "Of course Santa’s real. I even have a tracker that can tell me where he is.",
         "Oh no baby what is you doing?",
         "I plan on waiting here quietly until someone asks me a question.",
         "Tell me what you want what you really really want.",
         "I am your father?.",
         "I’m sorry I’m not Luke. This is kind of awkward."]
trainer = ListTrainer(bot)
trainer.train(convo)
print('Talk to Bot')
#while True:
    #query = input()
    #if query == 'exit':
        #break
    #answer = bot.get_response(query)
    #print("bot: ", answer)

def greet():
    currentH = int(datetime.now().hour)
    if currentH>=0 and currentH<12:
        msgs.insert(END, 'GOOD MORNING!')
        speak("GOOD MORNING!")

    if currentH >=12 and currentH < 18:
        msgs.insert( END, 'GOOD AFTERNOON!' )
        speak( "GOOD AFTERNOON!" )

    if currentH >= 18 and currentH <= 24:
        msgs.insert( END, 'GOOD EVENING!' )
        speak( "GOOD EVENING!" )
    ok = " HEY! I AM YOUR BOT ASSISTANT, HOW MAY I HELP YOU? "
    msgs.insert(END, "BOT: " +ok)
    speak("HEY! I AM YOUR BOT ASSISTANT, HOW MAY I HELP YOU? ")

def take_query():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("your bot is listening, try to speak!")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language= 'eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("can't recognise")

def command():
    query = textF.get()
    if 'open Google' in query:
        speak('okay')
        msgs.insert(END, "YOU: " +query)
        msgs.insert(END, "BOT: okay")
        webbrowser.open('www.google.co.in')
        textF.delete(0, END)
        msgs.yview(END)

    elif "open YouTube" in query:
        speak( 'okay' )
        msgs.insert( END, "YOU: " + query )
        msgs.insert( END, "BOT: okay" )
        webbrowser.open( 'www.youtube.com' )
        textF.delete( 0, END )
        msgs.yview( END)

    elif "open FaceBook" in query:
        speak( 'okay' )
        msgs.insert( END, "YOU: " + query )
        msgs.insert( END, "BOT: okay" )
        webbrowser.open( 'facebook.com' )
        textF.delete( 0, END )
        msgs.yview( END)

    elif "open shopping sites" in query:
        speak( 'okay' )
        msgs.insert( END, "YOU: " + query )
        msgs.insert( END, "BOT: okay" )
        webbrowser.open( 'https://www.google.com/search?ei=fuTYXrmNMYHWz7sPpoCgIA&q=www.shopping+online.com&oq=www.shopping+online.c&gs_lcp=CgZwc3ktYWIQARgAMgIIADIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoECAAQR1DnqgJY2rMCYNPTAmgAcAJ4AIABwgGIAd4CkgEDMC4ymAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab' )
        textF.delete( 0, END )
        msgs.yview( END)

    elif "open study material sites" in query:
        speak( 'okay' )
        msgs.insert( END, "YOU: " + query )
        msgs.insert( END, "BOT: okay" )
        webbrowser.open("https://www.google.com/search?q=study+material+sites&oq=study+material+sites&aqs=chrome..69i57j0l7.11470j1j7&sourceid=chrome&ie=UTF-8")
        textF.delete( 0, END )
        msgs.yview( END)


    elif "open word" in query:
        speak( 'okay' )
        msgs.insert( END, "YOU: " + query )
        msgs.insert( END, "BOT: okay" )
        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Word2013.lnk"
        os.startfile(path)
        textF.delete( 0, END )
        msgs.yview( END)

    elif "open paint" in query:
        speak( 'okay' )
        msgs.insert( END, "YOU: " + query )
        msgs.insert( END, "BOT: okay" )
        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\paint.lnk"
        os.startfile( path )
        textF.delete( 0, END )
        msgs.yview( END )

    elif'time' in query:
        strTime = datetime.now().strftime("%H:%M:%S")
        msgs.insert(END,"BOT: the time is  "+str(strTime))
        speak(f"THE TIME IS {strTime}")
        textF.delete(0, END)
        msgs.yview(END)

    elif "today's date" in query:
        today_date = datetime.date(datetime.now())
        msgs.insert( END, "BOT: today's date is  " + str(today_date) )
        speak( f"today's date is {today_date}" )
        textF.delete( 0, END )
        msgs.yview( END )

    elif 'wikipedia' in query:
        speak( 'okay' )
        msgs.insert(END, "YOU: " +query)
        msgs.insert(END, "BOT: searching wikipedia.....")
        speak("searching wikipedia.....")
        query = query.replace("wikipedia", " ")
        results = wikipedia.summary(query, sentences = 2)
        msgs.insert(END, "BOT: According to wikipedia")
        msgs.insert(END, "BOT: " +str(results))
        speak("According to wikipedia")
        speak(results)
        textF.delete(0, END)
        msgs.yview(END)

    elif 'dictionary' in query:
        speak( 'okay' )
        msgs.insert( END, "YOU: " + query )
        msgs.insert( END, "BOT: okay")
        query = query.replace( "dictionary", " " )
        results = PyDictionary.meaning(query)
        msgs.insert( END, "BOT: " + str( results ) )
        speak( results )
        textF.delete( 0, END )
        msgs.yview( END )

    elif 'antonym of' in query:
        speak( 'okay' )
        msgs.insert( END, "YOU: " + query )
        msgs.insert( END, "BOT: okay")
        query = query.replace( "antonym of", " " )
        results = PyDictionary.antonym(query)
        msgs.insert( END, "BOT: " + str( results ) )
        speak( results )
        textF.delete( 0, END )
        msgs.yview( END )

    elif 'synonym of' in query:
        speak( 'okay' )
        msgs.insert( END, "YOU: " + query )
        msgs.insert( END, "BOT: okay")
        query = query.replace( "synonym of", " " )
        results = PyDictionary.synonym(query)
        msgs.insert( END, "BOT: " + str( results ) )
        speak( results )
        textF.delete( 0, END )
        msgs.yview( END )

    elif"play music" in query:
        speak("okay playing")
        msgs.insert(END, "YOU: " +query)
        msgs.insert(END, "BOT: okay playing")
        music_dir = "C:\\Users\\pal_f\\Music"
        songs = os.listdir(music_dir)
        song = random.choice(songs)
        print(song)
        os.startfile(os.path.join(music_dir, song))
        textF.delete(0, END)
        msgs.yview(END)

def ask_from_bot():
    query = textF.get()
    if 'open Google' in query:
        command()
    elif "open YouTube" in query:
        command()
    elif "open FaceBook" in query:
        command()
    elif "open shopping sites" in query:
        command()
    elif "open word" in query:
        command()
    elif "open paint" in query:
        command()
    elif 'time' in query:
        command()
    elif "open study material sites" in query:
        command()
    elif 'wikipedia' in query:
        command()
    elif 'dictionary' in query:
        command()
    elif 'antonym of' in query:
        command()
    elif 'synonym of' in query:
        command()
    elif "play music" in query:
        command()
    elif "today's date" in query:
        command()
    else:
        msgs.insert( END, "YOU: " + query )
        answer = bot.get_response( query )
        speak( answer )
        msgs.insert( END, "BOT: " + str( answer ) )
        textF.delete( 0, END )
        msgs.yview( END )


main = Tk()
main.geometry("750x650")
main.title('MY CHAT BOT')
img = PhotoImage(file = 'bot.png')
photoL = Label(main, image = img)
photoL.pack(pady = 5)

frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, width = 500, height = 10, yscrollcommand = sc.set)
sc.pack(side= RIGHT, fill = Y)
msgs.pack(side=LEFT, fill= BOTH, pady = 10)
frame.pack()

# creating entry_field
textF = Entry(main, font=('verdana', 20))
textF.pack(fill = X , pady = 10)
btn = Button(main, text= 'Ask', font = ('Italic, 20'), command = ask_from_bot)
btn.pack()

def enter_function(event):
    btn.invoke()

main.bind('<Return>', enter_function)

def repeatL():
    greet()
    while True:
        take_query()
t = threading.Thread(target = repeatL)
t.start()

main.mainloop()



