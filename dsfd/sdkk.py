from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
import pandas as pd
df = pd.read_csv('IMDB-Movie-Data.csv')

def knowdir():
    df['Revenue (Millions)'].fillna('0', inplace = True)
    def change_revenue(revenue):
        return float(revenue)
    df['Revenue (Millions)'] = df['Revenue (Millions)'].apply(change_revenue)
    df['Rating'].fillna('0', inplace = True)
    a = df.info()
    df['New'] = df[(df['Director'] == dir)]['Director']
    know = df.groupby(by = ['Year', 'New'])['Rating'].mean()
    txt = know
    return str(txt)

class mainscreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        director = Label(text="Введите имя и фамилию режиссера на английском", halign='right')
        self.in_dir = TextInput(multiline = False)
        self.btn = Button(text="Проверить", size_hint=(.5, .2), pos_hint={'center_x': .5})
        self.btn.on_press = self.next
        line1 = BoxLayout(size_hint=(.8,None), height='30sp')
        line1.add_widget(director)
        line1.add_widget(self.in_dir)
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(line1)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        global dir
        dir = self.in_dir.text
        self.manager.current = 'ans'

class Finalscreen(Screen):
    def __init__(self,**kw):
        super().__init__(**kw)
        txt = Label(text = 'knowdir()', halign = 'center')

class DirectorKnow(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(mainscreen(name='ans1'))
        sm.add_widget(Finalscreen(name='ans'))
        return sm
app = DirectorKnow()
app.run()