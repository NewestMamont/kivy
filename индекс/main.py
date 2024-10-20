from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from txt_instruction import txt_instruction, txt_test1, txt_test2, txt_test3,txt_sits
from result import res
from kivy.properties import NumericProperty, StringProperty, BooleanProperty



name = "0"
total = 15
class Seconds(Label):
    done = BooleanProperty(False)
    def __init__(self,total,**kw):
        self.done = False
        self.total = total
        self.current = 0
        my_text = 'Прошло секунд: ' + str(self.current)
        super().__init__(text=my_text)
    def start(self):
        Clock.schedule_interval(self.change, 1)
    def change(self, dt):
        self.current += 1
        self.text = 'Прошло секунд: ' + str(self.current)
        if self.current >= self.total:
            self.done = True
            return False

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

    def check_int(self, str_sum):
        try:
            return int(str_sum)
        except:
            return False
    
    def next(self):
        global age,name
        age = self.check_int(self.in_age.text)
        if not age or age < 7:
            age = 7
            self.in_age.text = str(age)
        else:
            self.manager.current = 'pulse2'
        name = self.in_name.text
        print(10)
class PulseScr1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        instr1 = Label(text=txt_test1)
        res1 = Label(text='Результат', halign='right')
        self.lbl_sec = Seconds(5)
        self.lbl_sec.bind(done = self.sec_finished)
        self.in_res1 = TextInput(multiline=False)
        self.in_res1.set_disabled(True)
        self.btn=Button(text='Начать', size_hint=(.3,.2), pos_hint={'center_x':.5})
        self.btn.on_press = self.next
        line3=BoxLayout(size_hint=(.8,None), height='30sp')
        line3.add_widget(res1)
        line3.add_widget(self.in_res1)
        outer=BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr1)
        outer.add_widget(self.lbl_sec)
        outer.add_widget(line3)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def sec_finished(self, *args):
        self.next_screen = True
        self.btn.set_disabled(False)
        self.in_res1.set_disabled(False)
    def check_int(self, str_num):
        try:
            return int(str_num)
        except:
            return False
        
    def next(self):
        global p1
        p1 = self.check_int(self.in_res1.text)
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.in_res1.set_disabled(True)
            self.lbl_sec.start()
        else:
            if not p1 or p1 <= 0:
                p1 = 0
                self.in_res1.text = str(p1)
            if p1 > 0:
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

    def check_int(self, str_num):
        try: 
            return int(str_num)
        except:
            return False
    def next(self):
        global p2, p3  
        p2 = self.check_int(self.in_res1.text)
        p3 = self.check_int(self.in_res2.text) 
        truefalse1 = False
        truefalse2 = False
        if p2 == False or p2 <= 0:
            p2 = 0
            self.in_res1.text = str(p2)
        else:
            truefalse1 = True

        if p3 == False or p3 <= 0:
            p3 = 0
            self.in_res2.text = str(p3)
        else:
            truefalse2 = True
        
        if truefalse1 and truefalse2:
            self.manager.current = 'resScr'
class Result(Screen):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)
        self.instr = Label(text = '')
        self.add_widget(self.instr)
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