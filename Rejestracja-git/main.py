from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.widget import Widget
Window.size = (400,600)
Window.clearcolor =(1,1,1,1)

class Interface(Widget):
    pass
class MyApp(MDApp):
    def build(self):
        return Interface()
    def dodaj(self):
        self.email = self.root.ids.email.text
        self.haslo1 = self.root.ids.haslo1.text
        self.haslo2 = self.root.ids.haslo2.text
        if '@' in self.email:
            if self.haslo1 == self.haslo2:
                self.root.ids.text.text = "Witaj "+str(self.email)
            else:
                self.root.ids.text.text = "Hasla nie są identyczne"
        else:
            self.root.ids.text.text = "Nieprawidlowy adres email"
MyApp().run()