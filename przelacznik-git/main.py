from tkinter import *

root = Tk()
root.title('Przełącznik')
# root.iconbitmap('')
root.geometry("500x300")



# Śledzenie stanu przycisku on/off
global is_on
is_on = True

global blue
blue = True

# Tworzenie Label
my_label = Label(root,
                 text="Przełącznik jest włączony!",
                 fg="green",
                 font=("Helvetica", 30))

my_label.pack(pady=10)


# Definicja funkcji switch
def switch():
    global is_on
    global blue
    # Determin is on or off
    if is_on and blue:
        on_button.config(image=off, bg="red")
        my_label.config(text="Przełącznik jest wyłączony!", fg="black", bg="red")
        root.config(bg="red")
        blue = False
        is_on = False
    else:
        on_button.config(image=on, bg="#EEEEEE")
        my_label.config(text="Przełącznik jest włączony!", fg="black", bg="#EEEEEE")
        root.config(bg="#EEEEEE")
        is_on = True
        blue = True



    # Definicja zdjęć


on = PhotoImage(file="on.png")
off = PhotoImage(file="off.png")

# Tworzenie przycisku
on_button = Button(root, image=on, bd=0, command=switch)
on_button.pack(pady=30)

root.mainloop()
