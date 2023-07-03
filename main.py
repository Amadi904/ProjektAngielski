import pyttsx3

class SpeechModule:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()




if __name__ == '__main__':

    speech = SpeechModule()
    speech.speak("Witaj, to jest przykładowa wiadomość mowy.")


