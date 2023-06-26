from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget

Window.size=(400,600)

class MyInterface(Widget):
    def btnext(self, sm):
        if sm.current == "Screen 1":
            sm.current = "Screen 2"
            sm.transition.direction = "left"

        elif sm.current == "Screen 2":
            sm.current = "Screen 3"
            sm.transition.direction = "left"
        elif sm.current == "Screen 3":
            sm.current = "Screen 1"
            sm.transition.direction = "left"
    def btprev(self, sm):
            if sm.current == "Screen 2":
                sm.current = "Screen 1"
                sm.transition.direction = "right"
            elif sm.current == "Screen 1":
                sm.current = "Screen 3"
                sm.transition.direction = "right"
            elif sm.current == "Screen 3":
                sm.current = "Screen 2"
                sm.transition.direction = "right"

class MyApp(App):
    def build(self):
        return MyInterface()
if __name__=="__main__":
    MyApp().run()
