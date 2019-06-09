from tkinter import *

def button1():
    top= Toplevel()
    top.title("tell to type")
    import speech_recognition as sr

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say something")
        audio = r.listen(source)
    try:
        text11 = r.recognize_google(audio, language = "kn-IN")
        text12 = r.recognize_google(audio, language= "hi-IN")
        text13 = r.recognize_google(audio)
        print("you said :\n "
              "{}".format(text11))
        print(text12)
        print(text13)
        label3 = Label(top, text="SUCCESSFULL!!!!!"
                                 " result for what you said")
        text1 = Text(top, bg="black", fg="yellow")
        text1.insert(INSERT, "\n\nyour words in kannada format :\n{}".format(text11))
        text1.insert(INSERT, "\n\n\n\nyour words in hindi format :\n{}".format(text12))
        text1.insert(INSERT, "\n\n\n\nyour words in English  format :\n{}".format(text13))
        text1.pack()

        label3.pack()

    except:
        labe2 = Label(top, text="Sorry could not recognized")
        labe2.pack()
        print("sorry could not recognize")


def button2():
    import speech_recognition as sr
    import webbrowser as wb
    chrome_path = 'C:/Users/Ruqsar/AppData/Local/Google/Chrome/Application/chrome.exe %s'
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say something")
        audio = r.listen(source)
        print("done!")

    try:
        text = r.recognize_google(audio)
        print("google thinks you said :\n " + text)
        f_text = "https://www.google.co.in/search?q=" + text
        wb.get(chrome_path).open(f_text)
    except Exception as e:
        print(e)


def button3():
    import speech_recognition as sr
    import webbrowser as wb
    import speech
    top = Toplevel()
    top.title("Your words")

    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Say Something!')
        audio = r.listen(source)
        print('Done!')

    try:
        text = r.recognize_google(audio)
        print('Google thinks you said:\n' + text)
        label3 = Label(top, text="SUCCESSFULL!!!!!"
                                 " result for what you said")
        text1 = Text(top, bg="black", fg="red")
        text1.insert(INSERT, "you said :\n{}".format(text))
        text1.pack()
        label3.pack()
        lang = 'en'

        speech.tts(text, lang)

        f_text = 'https://www.google.co.in/search?q=' + text
        wb.get(chrome_path).open(f_text)
        text1.pack()
        label3.pack()
    except Exception as e:
        print(e)



def button4():

    import speech_recognition as sr
    top= Toplevel()
    top.title("speak and get text file")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say something")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("you said :\n "
              "{}".format(text))
        label3 = Label(top, text="SUCCESSFULL!!!!!"
                                 " result for what you said")
        text1 = Text(top, bg="black", fg="red")
        text1.insert(INSERT, "you said :\n{}".format(text))
        text1.pack()
        label3.pack()
        f = open("result.txt", "w")
        f.write(text)
    except:
        labe2 = Label(top, text="Sorry could not recognized")
        labe2.pack()
        print("sorry could not recognize")

1
root = Tk()
root.configure(background='black')
root.geometry("500x500")
root.title("Tell-To-Type")
button1 = Button(root, text='get your words in multi-text-format', bg="skyblue", width=40, command=button1)
button2 = Button(root, text="tell to google", bg="skyblue", width=40, command=button2)
button3 = Button(root, text='get words from machine', bg="skyblue", width=40, command=button3)
button4 = Button(root, text='save your words in text file', bg="skyblue", width=40, command=button4)
button1.place(x=100, y=100)
button2.place(x=100, y=150)
button3.place(x=100, y=200)
button4.place(x=100, y=250)

root.mainloop()