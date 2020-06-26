import pyttsx3
import datetime
import smtplib as smt

engine=pyttsx3.init('sapi5')
rate=engine.getProperty('rate')
engine.setProperty('rate',190)
volume=engine.getProperty('volume')

engine.setProperty('volume',10)

def speak(audio):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        t1 = "good morning mister", name
        speak(t1)
    elif hour > 12 and hour < 18:
        t2 = "good afternoon mister", name
        speak(t2)
    else:
        t3 = "good evening mister", name
        speak(t3)


def missme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12                                                                                                         :
        s1="good morning miss",name
        speak("s1")
    elif hour>12 and hour<18:
       s2="good afternoon miss",name
       speak(s2)
    else:
       s3= "good evening miss",name
       speak(s3)




def send():
   print("FROM:_ ")
   emil=input()
   print("PASSWORD:_ ")
   password=input()
   print("TO:_ ")
   to=input()
   print("PLEASE WRITE MESSAGE")
   message=input()
   server=smt.SMTP('smtp.gmail.com',587)
   server.ehlo()
   server.starttls()
   server.ehlo()
   server.login(emil,password)
   server.sendmail(emil,to,message)
   server.quit()
   print("hey email has been sent")

if __name__ == '__main__':

 speak("welcome to python email service , i'm zaira i will asist you in this application so before you get into this application you have to check your internet connection")
 print("WELCOME TO PYMAIL")
 speak("so before you get enter in this application,i want to know your details,because every data from our customer are valueable for our organisation")
 speak("so are you agree with me if yes then type yes else type no")
 upp="If you are get enter into this application press 'yes' else you can press 'no' for come back into this application".upper()
 print(upp)
 x = input()
 y = "yes"
 z = "no"

 if (x == y):
    speak("so you are ready to get your data")
    speak("so first of all you give your first name and then last name ")
    speak("then give your date of birth")
    speak("and finally give your gender ")
    print("FIRST NAME: ")
    name = input()
    print("LAST NAaME: ")
    name2 = input()
    print("D.O.B(only year):")
    dob = input()
    age = 2019 - int(dob)
    print("AGE: ", age)
    print("GENDER: ")
    gender = input()
    if (gender == "male"):
        wishme()
        print("Hello Mr", name, "sir")
        speak("once again welcome sir")
        print("PYTHON ELECTRONICS MAIL")
        send()
        input()
        exit()
    elif (gender == "female"):
     missme()
     print("Hello Mrs", name, "madam")
     speak("once again welcome mam")
     print("PYTHON ELECTRONICS MAIL")
     send()
     input()
     exit()
    else:
     speak("sorry sir or madam you are giving some wrong information,so please try next time")
     exit()

elif (x == z):
            speak("have a nice day sir or mam")
            print("Have a nice day sir or mam")
            exit()
else:
    speak("sorry sir/madam,you are not enter valid answer ")
    speak("so you have to leave this application and again start")
    speak("bye bye")
    exit()


