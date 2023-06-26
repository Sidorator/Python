import sqlite3
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from database import Database

Window.size = (400, 650)

db = Database('baza.db')


class MainInterface(Widget):
    pass

class MyApp(MDApp):
    def build(self):
        self.theme_cls.accent_palette = "Blue"
        self.data_tables=MDDataTable(
            size_hint=(0.95, 0.90),
            use_pagination=True,
            rows_num=8,
            elevation=2,
            column_data=[
                ("Ulica", dp(20)),
                ("Numer domu",dp(20)),
                ("Kod pocztowy", dp(30))
            ]
        )
        self.data_tables.row_data = self.get_all_data()
        self.root.ids.tab.add_widget(self.data_tables)
        return 0



    def clear_list(self):
        self.data_tables.row_data.clear()


    def dodaj(self,sm):
        sm.current = "screen 1"
        ulica = self.root.ids.ulica.text
        dom = self.root.ids.dom.text
        kod = self.root.ids.kod.text

        conn = sqlite3.connect('baza.db')
        c = conn.cursor()
        if ulica != "" and dom != "" and kod != "":
            c.execute("INSERT INTO uczen (ulica, dom, kod) values (?,?,?);", (ulica, dom, kod))
        conn.commit()
        conn.close()

        self.data_tables.row_data = self.get_all_data()

    def usun(self):
        db.delete(s)
        self.data_tables.row_data = self.get_all_data()

    def czysc(self):
        self.root.ids.ulica.text = " "
        self.root.ids.dom.text = " "
        self.root.ids.kod.text = " "

    def get_all_data(self):
        self.clear_list()
        data = []
        for row in db.fetch_all():
            data.append(row)
        return data



MyApp().run()