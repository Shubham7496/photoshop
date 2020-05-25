from tkinter import *
from tkinter import Toplevel
from PIL import Image,ImageTk,ImageFilter
import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
print(voices[0].id)

def speak(audio):

    engine.say(audio)
    engine.runAndWait()

def exit1():
    engine.say("have a nice day")
    engine.runAndWait()
    root.destroy()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("adjustment is going on...........")
        r.adjust_for_ambient_noise(source,duration=1) #adjustment to the surrounding noise
        print("Listening.....")
        r.pause_threshold = 1  #adjust the reponse time
        audio=r.listen(source)
        print(audio)

    try:

        print("Recognizing....")
        query=r.recognize_google(audio,language= 'en-in')

    except Exception as e:

        engine.say("say that again please")
        engine.runAndWait()
        return "None"
    return query

def crop():
    #query=takecommand().lower()
    #query=input("enter the command")
    #print(query)
    #t=takecommand().lower()
    #print(t)
    #if "crop" in query:
    speak("may I get the image : ")
    img1 = takecommand().lower()
    if "lion" in img1:

        engine.say("may i get the dimensions for crop")
        engine.runAndWait()

        '''engine.say("number 1")
        engine.runAndWait()
        dim1=takecommand()
        engine.runAndWait()
        engine.say("number 2")
        engine.runAndWait()
        dim2=takecommand()
        engine.say("number 3")
        engine.runAndWait()
        dim3=takecommand()
        engine.say("number 4")
        engine.runAndWait()
        dim4=takecommand()'''

        engine.say("number 1:half  and  number 2:quarter")
        engine.runAndWait()
        dim=takecommand().lower()
        #dim=input("enter the command")
        print(dim)
        #img=Image.open("imgsayphoto.jpg")

        img=Image.open("lionimg.jpg")
        img.show()
        if "half" in dim:
            width=img.width
            height=img.height

            area=(0,0,width/2,height)
            img=img.crop(area)

            img.save("cropimg.jpg")
            img.show()
        if "quarter" in dim:
            width=img.width
            height=img.height

            area=(0,0,width/2,height/2)
            img=img.crop(area)

            img.save("cropimg.jpg")
            img.show()
    pass

def rotate():
    #query = input("enter the command")
    #print(query)
    speak("may I get the image : ")
    img1=takecommand().lower()
    if "lion" in img1:
        #if "rotate" in query:
        engine.say("may i get the degree for rotate")
        engine.runAndWait()
        '''engine.say("number 1:half  and  number 2:quarter")
        engine.runAndWait()'''
        dim=takecommand().lower()
        #dim = input("enter the command")
        #print(dim)
        #img = Image.open("imgsayphoto.jpg")
        img = Image.open("lionimg.jpg")
        img.show()
        if "45" in dim:
            dim=45
            #img=img.transpose(Image.FLIP_LEFT_RIGHT)
            img=img.rotate(float(dim))
            img.show()
        if "90" in dim:
            dim=90
            img = img.rotate(float(dim))
            img.show()
    pass
def blur():
    #img = Image.open("imgsayphoto.jpg")
    speak("may I get the image : ")
    img1=takecommand().lower()
    if "photo" in img1:
        speak("may i get extention")
        ext=takecommand().lower()
        photo1="photo"
        img = Image.open(photo1+"."+ext)
        img.show()
        img = img.filter(ImageFilter.GaussianBlur(radius=20))
        img.save("blurimg.jpg")
        img.show()
    pass

def edges():
    #img=Image.open("imgsayphoto.jpg")
    speak("may I get the image : ")
    img1 = takecommand().lower()
    if "photo" in img1:
        img = Image.open("photo.jpg")
        img.show()
        img=img.filter(ImageFilter.FIND_EDGES())  #[-1-1-1-18-1-1-1-1]
        img.save("edgesimg.jpg")
        img.show()
    else:
        speak("sorry")
    pass
def imageprocess():
    query=takecommand().lower()
    print(query)
    if "crop" in query:
        crop()
    elif "rotate" in query:
        rotate()
    elif "blur" in query:
        blur()
    elif "border" in query:
        edges()
    elif "grey" in query:
        grey()
    else:
        engine.say("no such functionality..... sorry .....")
        engine.runAndWait()
    pass
def opentext():
    new_wintext = Toplevel()
    new_wintext.geometry("720x720")
    new_wintext.title("good")
    lab1=Label(new_wintext,text="ENTER THE COMMAND : ",bg="black",font="Italic 36 bold",padx=15,pady=50,fg="cyan")
    lab1.pack()
    ''' Label(new_wintext,text="1. CROP",bg="black",fg="cyan").grid(row=2)
    Label(new_wintext, text="2. ROTATE", bg="black", fg="cyan").grid(row=3)
    Label(new_wintext, text="3. BLUR", bg="black", fg="cyan").grid(row=4)
    Label(new_wintext, text="4. EDGES\n", bg="black", fg="cyan").grid(row=5)
    Entry(new_wintext,textvariable=command).grid(row=6)
    Label(new_wintext,text="", bg="black").grid(row=7)'''
    b4=Button(new_wintext,fg="cyan",text="BLUR",bg="black",command=blurtext).pack()
    Label(new_wintext,text="",bg="black").pack()
    b6=Button(new_wintext,fg="cyan",text="EDGES",bg="black",command=edgestext).pack()
    Label(new_wintext,text="",bg="black").pack()
    b5=Button(new_wintext,fg="cyan",text="GREYSCALE",bg="black",command=greytext).pack()
    new_wintext.configure(background="black")
    Label(new_wintext,text="",bg="black").pack()
    b4 = Button(new_wintext, fg="cyan", text="EXIT", bg="black", command=exit1).pack()
    new_wintext.configure(background="black")
    new_wintext.mainloop()
    pass

def grey():
    speak("may I get the image : ")
    img1 = takecommand().lower()
    if "lion" in img1:
        img=Image.open("lionimg.jpg")
        img.show()
        img=img.convert("1") #Y' = 0.2989 R + 0.5870 G + 0.1140 B
        img.show()
        img.save("greyimg.jpg")
    else:
        speak("sorry")

    pass
def greytext():
    img = Image.open("lionimg.jpg")
    img.show()
    img = img.convert("1")  # Y' = 0.2989 R + 0.5870 G + 0.1140 B
    img.show()
    img.save("greyimg.jpg")
    pass
def edgestext():
    img = Image.open("lionimg.jpg")
    img.show()
    img = img.filter(ImageFilter.FIND_EDGES())  # [-1-1-1-18-1-1-1-1]
    img.save("edgesimg.jpg")
    img.show()
    pass

def blurtext():
    img = Image.open("lionimg.jpg")
    img.show()
    img = img.filter(ImageFilter.GaussianBlur(radius=20))
    img.save("blurimg.jpg")
    img.show()
    pass
def wishme():

    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("good morning! sir")

    elif hour>=12 and hour<18:
        speak("Good afternoon! sir")

    else:
        speak("Good evening!")

    speak("welcome to say photoshop lite !!! ")
    speak("how can I help you sir ?")
    pass
if __name__=="__main__":
    root=Tk()
    root.geometry("900x900")
    wishme()

    lab=Label(text="SAY PHOTO-SHOP LITE !!!",bg="black",font="Italic 36 bold",padx=15,pady=50,fg="cyan")

    lab.pack()

    image = Image.open("imgsayphoto.jpg")
    photo = ImageTk.PhotoImage(image)

    imglabel= Label(image=photo)
    imglabel.pack()
    Label(text="", bg="black").pack()
    f1 = Frame(root, bg="black", relief=SUNKEN)
    f1.pack()

    b1 = Button(f1, fg="cyan", text="SPEAK ",bg="black",command=imageprocess)
    b1.pack(padx=34)
    Label(f1,text="",bg="black").pack()
    b2 = Button(f1, fg="cyan", text="TEXT", bg="black", command=opentext, padx=7)
    b2.pack()
    Label(f1, text="", bg="black").pack()
    exit = Button(f1, fg="cyan", text="EXIT ", bg="black", command=exit1, padx=7)
    exit.pack(padx=32)
    Label(f1, text="", bg="black").pack()
    root.configure(background='black')

    root.mainloop()
