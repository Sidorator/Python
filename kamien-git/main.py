from tkinter import *
import random


class Aplikacja:



    def __init__(self, okno):

        self.komputer = random.choice(["kamien", "papier", "nozyce"])

        print(self.komputer)


        self.label = Label(text="wybierz:")
        self.label.grid(row=0, column=3)


        self.img = PhotoImage(file="kamien.png")
        self.przycisk1 = Button(okno, image=self.img, command=lambda:self.sprawdzanie(1))
        self.przycisk1.grid(row=1,column=2)

        self.img1 = PhotoImage(file="papier.png")
        self.przycisk2 = Button(okno, image=self.img1, command=lambda:self.sprawdzanie(2))
        self.przycisk2.grid(row=1, column=3)

        self.img2 = PhotoImage(file="nozyce.png")
        self.przycisk3 = Button(okno, image=self.img2, command=lambda:self.sprawdzanie(3))
        self.przycisk3.grid(row=1, column=4)




    def sprawdzanie(self, liczba):
        global restart
        if liczba ==1:
            self.wybor = "kamien"
        elif liczba ==2:
            self.wybor = "papier"
        else:
            self.wybor = "nozyce"

        if self.wybor=="kamien" and self.komputer == "kamien":
            Label(okno,text="Kamien vs kamien, Remis!").grid(row=2, column=1, columnspan=4)


        elif self.wybor=="kamien" and self.komputer == "papier":
            Label(okno, text="Kamien vs papier, Przegrana!").grid(row=2, column=1, columnspan=4)


        elif self.wybor=="kamien" and self.komputer == "nozyce":
            Label(okno, text="Kamien vs nozyce, Wygrana!").grid(row=2, column=1, columnspan=4)


        elif self.wybor=="papier" and self.komputer == "kamien":
            Label(okno, text="papier vs kamien, Wygrana!").grid(row=2, column=1, columnspan=4)


        elif self.wybor=="papier" and self.komputer == "papier":
            Label(okno, text="papier vs papier, Remis!").grid(row=2, column=1, columnspan=4)


        elif self.wybor=="papier" and self.komputer == "nozyce":
            Label(okno, text="papier vs nozyce, Przegrana!").grid(row=2, column=1, columnspan=4)


        elif self.wybor=="nozyce" and self.komputer == "kamien":
            Label(okno, text="nozyce vs kamien, Przegrana!").grid(row=2, column=1, columnspan=4)


        elif self.wybor=="nozyce" and self.komputer == "papier":
            Label(okno, text="nozyce vs papier, Wygrana!").grid(row=2, column=1, columnspan=4)


        elif self.wybor=="nozyce" and self.komputer == "nozyce":
            Label(okno, text="nozyce vs nozyce, Remis!").grid(row=2, column=1, columnspan=4)






okno = Tk()
okno.title("Kamien Papier Nozyce")
okno.geometry("300x300")

app = Aplikacja(okno)
okno.mainloop()