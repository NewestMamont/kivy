from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from txt_instruction import txt_instruction, txt_test1, txt_test2, txt_test3,txt_sits
from result import res



name = "0"
class mainscreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        instruction = Label(text=txt_instruction)
        name1 = Label(text="Введите имя", halign='right')
        self.in_name = TextInput(multiline = False)
        age1 = Label(text="Введите возраст", halign='right')
        self.in_age = TextInput(multiline=False)
        self.btn = Button(text="Начать", size_hint=(.3, .2), pos_hint={'center_x': .5})
        self.btn.on_press = self.next
        line1 = BoxLayout(size_hint=(.8,None), height='30sp')
        line2 = BoxLayout(size_hint=(.8,None), height='30sp')
        line1.add_widget(name1)
        line1.add_widget(self.in_name)
        line2.add_widget(age1)
        line2.add_widget(self.in_age)
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instruction)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        global age
        age = self.in_age.text
        self.manager.current = 'pulse2'
        print(10)
class PulseScr1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr1 = Label(text=txt_test1)
        res1 = Label(text='Результат', halign='right')
        self.in_res1 = TextInput(multiline=False)
        self.btn=Button(text='Дальше', size_hint=(.3,.2), pos_hint={'center_x':.5})
        self.btn.on_press = self.next
        line3=BoxLayout(size_hint=(.8,None), height='30sp')
        line3.add_widget(res1)
        line3.add_widget(self.in_res1)
        outer=BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr1)
        outer.add_widget(line3)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        global p1
        p1=self.in_res1.text
        self.manager.current = 'pulse3'
class CheckSits(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        instr2=Label(text=txt_sits)
        self.btn=Button(text='Дальше',size_hint=(.3,.2), pos_hint={'center_x':.5})
        self.btn.on_press=self.next
        outer=BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr2)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        self.manager.current='pulse4'       
class PulseScr2(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        instr2=Label(text=txt_test3)
        res1 = Label(text='Первое измерение', halign='right')
        self.in_res1 = TextInput(multiline=False)
        res2 = Label(text='Второе измерение', halign='right')
        self.in_res2 = TextInput(multiline=False)
        self.btn=Button(text='Дальше',size_hint=(.3,.2), pos_hint={'center_x':.5})
        self.btn.on_press=self.next
        line3=BoxLayout(size_hint=(.8,None), height='30sp')
        line3.add_widget(res1)
        line3.add_widget(self.in_res1)
        line3.add_widget(res2)
        line3.add_widget(self.in_res2)
        outer=BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr2)
        outer.add_widget(line3)
        outer.add_widget(self.btn)
        self.add_widget(outer) 
    def next(self):
        global p2, p3   
        p2=self.in_res1.text
        p3=self.in_res2.text
        self.manager.current='resScr'   
class Result(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        outer=BoxLayout(orientation='vertical', padding=8, spacing=8)
        self.instr = Label(text = '')
        self.add_widget(outer)
        self.on_enter = self.before
    def before(self):
        global name,age,p1,p2,p3
        age = int(age)
        p1 = int(p1)
        p2 = int(p2)
        p3 = int(p3)
        self.instr.text = name + "\n" + res(p1,p2,p3,age)
class HeartCheck(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(mainscreen(name='pulse1'))
        sm.add_widget(PulseScr1(name='pulse2'))
        sm.add_widget(CheckSits(name='pulse3'))
        sm.add_widget(PulseScr2(name='pulse4'))
        sm.add_widget(Result(name='resScr'))
        return sm
app = HeartCheck()
app.run()