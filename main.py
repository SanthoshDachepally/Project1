import pyttsx3

if __name__ == '__main__':
    print("Welcome to Robo Speaker 1.1 Created by Santhosh")
    engine = pyttsx3.init()
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "q":
            engine.say('bye bye friend')
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()