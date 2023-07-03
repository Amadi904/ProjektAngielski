import pyttsx3
import tkinter as tk

class SpeechModule:
    def __init__(self):
        self.engine = pyttsx3.init()
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
class MyInterface(tk.Tk):
    def __init__(self, width, height):
        super().__init__()
        self.configure(bg="lightblue")
        self.geometry(f"{width}x{height}")  # Ustawienie wymiarów interfejsu
        self.label1 = tk.Label(self, text="Witaj w interfejsie graficznym wybierz co chcesz dziś robić!",bg="orange")
        self.label1.pack()
        self.label2 = tk.Label(self, text="Słuchanie",bg="orange")
        self.label2.pack()
        self.button1 = tk.Button(self, text="Wybierz sluchanie",bg="light green",command=self.open_new_window)
        self.button1.pack()
        self.label3 = tk.Label(self, text="Czytanie",bg="orange")
        self.label3.pack()
        self.button2 = tk.Button(self, text="Wybierz czytanie",bg="light green")
        self.button2.pack()
        self.label4 = tk.Label(self, text="Quiz",bg="orange")
        self.label4.pack()
        self.button3 = tk.Button(self, text="Wybierz Quiz",bg="light green")
        self.button3.pack()
        self.label5 = tk.Label(self, text="Nauka slowek",bg="orange")
        self.label5.pack()
        self.button2 = tk.Button(self, text="Wybierz Nauke slowek",bg="light green")
        self.button2.pack()
        self.label6 = tk.Label(self, text="Nauka zwrotów",bg="orange")
        self.label6.pack()
        self.button2 = tk.Button(self, text="Wybierz Nauke zwrotow",bg="light green")
        self.button2.pack()

    def open_new_window(self):
        self.withdraw()  # Ukrywa bieżące okno
        new_window = tk.Toplevel(self)  # Tworzy nowe okno
        new_window.title("Nowe Okno")
        new_window.configure(bg="lightblue")
        new_window.geometry("800x600")
        label = tk.Label(new_window, text="To jest nowe okno", bg="orange")
        label.pack()
        button_back = tk.Button(new_window, text="Powrót", bg="light green", command=self.back_to_main_window) #Przycisk powrotu
        button_back.pack()
    def back_to_main_window(self):
        self.deiconify()  # Przywróć bieżące okno
        # Zamknij drugie okno
        for window in self.winfo_children():
            if isinstance(window, tk.Toplevel):
                window.destroy()

if __name__ == '__main__':


    interface = MyInterface(800, 600)
    interface.mainloop()

    speech = SpeechModule()
    #speech.speak("Witaj, to jest przykładowa wiadomość mowy.")


