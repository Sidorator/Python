from kivy.app import App
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivy.core.window import Window


Window.size= (400,600)
Window.geometry = True
Window.clearcolor = get_color_from_hex("#ffffff")


class MyInterface(Widget):
    def dodawanie(self):
        self.a = self.ids.a.text
        self.b = self.ids.b.text

        self.suma = int(self.a) + int(self.b)

        self.ids.wynik.text = str(self.a) + " + " + str(self.b) + " = " + str(self.suma)

    def odejmowanie(self):
        self.a = self.ids.a.text
        self.b = self.ids.b.text

        self.roznica = int(self.a) - int(self.b)

        self.ids.wynik.text = str(self.a) + " - " + str(self.b) + " = " + str(self.roznica)

    def mnozenie(self):
        self.a = self.ids.a.text
        self.b = self.ids.b.text

        self.iloraz = int(self.a) * int(self.b)


        if (int(self.a) or int(self.b) == 0):
            self.ids.wynik.text = str(self.a) + " * " + str(self.b) + " = " + str(self.iloraz)

        elif (int(self.a) or int(self.b) == '' ):
            self.ids.wynik.text = "Podaj dane"
        else:
            self.ids.wynik.text = "bląd"
    def dzielenie(self):
        self.a = self.ids.a.text
        self.b = self.ids.b.text

        self.iloczyn = int(self.a) / int(self.b)

        self.ids.wynik.text = str(self.a) + " / " + str(self.b) + " = " + str(self.iloczyn)

    def odnosnik(self, sm):

        if  (sm.current == 'kalkulator'):
            sm.current = 'kantor'
            sm.transition.direction = "left"
        elif (sm.current == 'kantor'):
            sm.current = 'kalkulator'
            sm.transition.direction = "right"





class MyApp(App):
    def build(self):
        return MyInterface()

MyApp().run()
