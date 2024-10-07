from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.core.window import Window
from multiprocessing import Process
import random
import winsound
count=0
counto=0
z=0
player1=0
player2=0
a='a'
b='b'




Builder.load_string("""
<Mainpage>
    FloatLayout:
        orientation:'horizontal'
    	size:root.width,root.height
    	Button:
            on_release: root.manager.current = 'menu'
            text:"AI vs you"
            pos_hint: {'center_x': 0.25, 'center_y':0.5}
            size_hint:0.4,0.8
        Button:
            on_release: root.manager.current = 'pvp'
            text:"2-player"
            pos_hint: {'center_x': 0.75, 'center_y':0.5}
            size_hint:0.4,0.8
        Button:
            on_release: root.manager.current = 'settings'
            pos_hint: {'center_x': 0.95, 'center_y':0.95}
            size_hint:0.1,0.1
            background_color:0.7,0.2,0,0.25
            Image:
                source:'setting.png'
                center_x:self.parent.center_x
                center_y:self.parent.center_y
                size: (max(root.size)*0.05, max(root.size)*0.1)
                y: self.parent.y
                x: self.parent.x
                keep_ratio:False
                allow_stretch: True
            

		
    
		
<MyLayout>
	FloatLayout:
		orientation:'horizontal'
		size:root.width,root.height
		Button:
			on_press:root.rock()
			on_release: root.manager.current = 'score'
			text:"rock"
			pos_hint: {'center_x': 0.15, 'center_y':0.5}
			size_hint:0.25,0.8
			Image:
				source:'rock.png'
				center_x:self.parent.center_x
				center_y:self.parent.center_y-160
				
				
				size: (min(root.size)*0.25, min(root.size)*0.2)
				y: self.parent.y 
				x: self.parent.x
				keep_ratio:False
				allow_stretch: True
		Button:
			on_press:root.scissor()
			on_release: root.manager.current = 'score'
			text:"scissor"
			pos_hint: {'center_x': 0.50, 'center_y':0.5}
			size_hint:0.25,0.8
			Image:
				source:'scissor.png'
				center_x:self.parent.center_x
				center_y:self.parent.center_y-160
				
				
				size: (min(root.size)*0.25, min(root.size)*0.2)
				y: self.parent.y 
				x: self.parent.x
				keep_ratio:False
				allow_stretch: True
		Button:
			on_press:root.paper()
			on_release: root.manager.current = 'score'
			text:"paper"
			pos_hint: {'center_x': 0.85, 'center_y':0.5}
			size_hint:0.25,0.8
			Image:
				source:'paper.png'
				center_x:self.parent.center_x
				center_y:self.parent.center_y-160
				
				
				size: (min(root.size)*0.25, min(root.size)*0.2)
				y: self.parent.y 
				x: self.parent.x
				keep_ratio:False
				allow_stretch: True
                FloatLayout:
                    orientation:'horizontal'
                    size:root.width,root.height
                    Label:
                        text:"choose:"
                        font_size: sp(32)
                        pos_hint: {'center_x': 0.2, 'top': 0.95}
                        size_hint:0.25,0
				
<score>:
    FloatLayout:
        Label:
            text: "--> "+ app.w+" <--"
            font_size: sp(20)
            pos_hint: {'center_x': 0.5, 'top': 1.25}
        Button:
            text: 'clear score'
            on_press:
                root.clear()
            pos_hint: {'center_x': 0.5, 'top': 0.2}
            size_hint:0.23,0.1
    FloatLayout:
        FloatLayout:
            Button:
                text: '<--go back'
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'menu'
                pos_hint: {'center_x': 0.1, 'top':1}
                size_hint:0.25,1
        Label:
            text: "AI chose--> "+ app.z+" <--"
            pos_hint: {'center_x': 0.5, 'top':0.4}
            size_hint:0.1,0.1
        Label:
            text:'AI score '+ app.counto
            pos_hint: {'center_x': 0.5, 'top':0.5}
            size_hint:0.1,0.1
        Label:
            text:'your score '+ app.count
            pos_hint: {'center_x': 0.5, 'top':0.6}
            size_hint:0.1,0.1
        FloatLayout:
            Button:
                text: 'main page-->'
                on_press:
                    root.clear()
                on_release:
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'main'
                pos_hint: {'center_x': 0.9, 'top':1}
                size_hint:0.25,1
<second>:
	FloatLayout:
		orientation:'horizontal'
		size:root.width,root.height
		Button:
			on_press:root.rock()
			on_release: root.manager.current = 'pvp2'
			text:"rock"
			pos_hint: {'center_x': 0.15, 'center_y':0.5}
			size_hint:0.25,0.8
			Image:
				source:'rock.png'
				center_x:self.parent.center_x
				center_y:self.parent.center_y-160
				
				
				size: (min(root.size)*0.25, min(root.size)*0.2)
				y: self.parent.y 
				x: self.parent.x
				keep_ratio:False
				allow_stretch: True
		Button:
			on_press:root.scissor()
			on_release: root.manager.current = 'pvp2'
			text:"scissor"
			pos_hint: {'center_x': 0.50, 'center_y':0.5}
			size_hint:0.25,0.8
			Image:
				source:'scissor.png'
				center_x:self.parent.center_x
				center_y:self.parent.center_y-160
				
				
				size: (min(root.size)*0.25, min(root.size)*0.2)
				y: self.parent.y 
				x: self.parent.x
				keep_ratio:False
				allow_stretch: True
		Button:
			on_press:root.paper()
			on_release: root.manager.current = 'pvp2'
			text:"paper"
			pos_hint: {'center_x': 0.85, 'center_y':0.5}
			size_hint:0.25,0.8
			Image:
				source:'paper.png'
				center_x:self.parent.center_x
				center_y:self.parent.center_y-160
				
				
				size: (min(root.size)*0.25, min(root.size)*0.2)
				y: self.parent.y 
				x: self.parent.x
				keep_ratio:False
				allow_stretch: True
                FloatLayout:
                    orientation:'horizontal'
                    size:root.width,root.height
                    Label:
                        text:"player 1:"
                        font_size: sp(32)
                        pos_hint: {'center_x': 0.5, 'top': 0.95}
                        size_hint:0.25,0


<third>:
	FloatLayout:
		orientation:'horizontal'
		size:root.width,root.height
		Button:
			on_press:root.rock()
			on_release: root.manager.current = 're'
			text:"rock"
			pos_hint: {'center_x': 0.15, 'center_y':0.5}
			size_hint:0.25,0.8
			Image:
				source:'rock.png'
				center_x:self.parent.center_x
				center_y:self.parent.center_y-160
				
				
				size: (min(root.size)*0.25, min(root.size)*0.2)
				y: self.parent.y 
				x: self.parent.x
				keep_ratio:False
				allow_stretch: True
		Button:
			on_press:root.scissor()
			on_release: root.manager.current = 're'
			text:"scissor"
			pos_hint: {'center_x': 0.50, 'center_y':0.5}
			size_hint:0.25,0.8
			Image:
				source:'scissor.png'
				center_x:self.parent.center_x
				center_y:self.parent.center_y-100
				
				size: (min(root.size)*0.25, min(root.size)*0.2)
				y: self.parent.y 
				x: self.parent.x
				keep_ratio:False
				allow_stretch: True
		Button:
			on_press:root.paper()
			on_release: root.manager.current = 're'
			text:"paper"
			pos_hint: {'center_x': 0.85, 'center_y':0.5}
			size_hint:0.25,0.8
			Image:
				source:'paper.png'
				size: (min(root.size)*0.25, min(root.size)*0.2)
				y: self.parent.y 
				x: self.parent.x
				keep_ratio:False
				allow_stretch: True
                FloatLayout:
                    orientation:'horizontal'
                    size:root.width,root.height
                    Label:
                        text:"player 2:"
                        font_size: sp(32)
                        pos_hint: {'center_x': 0.5, 'top': 0.95}
                        size_hint:0.25,0

<result>:
    FloatLayout:
        Label:
            text: "--> "+ app.w+" <--"
            font_size: sp(20)
            pos_hint: {'center_x': 0.5, 'top': 1.25}
        Button:
            text: 'clear score'
            on_press:
                root.clear()
            pos_hint: {'center_x': 0.5, 'top': 0.3}
            size_hint:0.23,0.1
    FloatLayout:
        FloatLayout:
            Button:
                text: '<--go back'
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'pvp'
                pos_hint: {'center_x': 0.1, 'top':1}
                size_hint:0.25,1

        Label:
            text:'player1 score: '+ app.player1
            pos_hint: {'center_x': 0.5, 'top':0.5}
            size_hint:0.1,0.1
        Label:
            text:'player2 score: '+ app.player2
            pos_hint: {'center_x': 0.5, 'top':0.6}
            size_hint:0.1,0.1
        FloatLayout:
            Button:
                text: 'main page-->'
                on_press:
                    root.clear()
                on_release:
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'main'
                pos_hint: {'center_x': 0.9, 'top':1}
                size_hint:0.25,1

<Settings>
    canvas.before:
        Color:
            rgba:1,0.1,0,1
        Rectangle:
            pos:self.pos
            size:self.size
    FloatLayout:
    	Button:
            on_press:
                root.play_music()
            text:"MUSIC"
            pos_hint: {'center_x': 0.5, 'center_y':0.8}
            size_hint:0.2,0.2
        Button:
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'main'
            text:"BACK"
            pos_hint: {'center_x': 0.5, 'center_y':0.5}
            size_hint:0.2,0.2
    	Label:
            text:'settings'
            pos_hint: {'center_x': 0.5, 'top':1}
            size_hint:0.1,0.1
            font_size: sp(32)

                    
""")
w="w"
t=0
e=0
who="score: "
winsound.PlaySound('song (1).wav',winsound.SND_ASYNC  + winsound.SND_LOOP)
class Mainpage(Screen):
    def play_music(self,*args):
        pass
    pass
class Settings(Screen):
    def play_music(self):
        global e
        e+=1
        if e%2==0:
            print(e)
            winsound.PlaySound('song (1).wav',winsound.SND_ASYNC  + winsound.SND_LOOP)
        else:
            print(e)
            winsound.PlaySound(None, winsound.SND_PURGE)


class MyLayout(Screen):
    def on_enter(self,*args):
        global who
        self.app=App.get_running_app()
        self.app.count=str(count)
        self.app.counto=str(counto)
        self.app.who=str(who)
        self.app.z=str(z)
        self.app.w=str(w)
    def rock(self):
        RPS=['rock','scissor','paper']
        global z
        z=random.choice(RPS)
        self.app.z= z 
        print(self.app.z)
        y='rock'
        print(z,y)
        if z==y:
            print("draw")
            global w
            w="it was a draw"
            self.app.w=str(w)
        elif z=='paper':
            if y=='rock':
                print('you lost')
                global counto
                counto+=1
                print(counto)
                self.app.counto=str(counto)
                w="YOU LOST!"
                self.app.w=str(w)

            else:
                pass
                
        elif z=='scissor':
            if y=='rock':
                global count
                print("you won")
                count+=1
                print(count)
                self.app.count=str(count)
                w="YOU WON!"
                self.app.w=str(w)
            else:
                pass
    def paper(self):
        RPS=['rock','scissor','paper']
        global z
        z=random.choice(RPS)
        self.app.z=str(z)
        y='paper'
        print(z,y)
        if z==y:
            print("draw")
            global w
            w="it was a draw"
            self.app.w=str(w)
        elif z=='rock':
            if y=='paper':
                print("you won")
                global count
                count+=1
                self.app.count=str(count)
                w="YOU WON!"
                self.app.w=str(w)
            else:
                pass

        elif z=='scissor':    
            if y=='paper':
                print('you lost')
                global counto
                counto+=1
                self.app.counto=str(counto)
                w="YOU LOST!"
                self.app.w=str(w)
            else:
                pass
    def scissor(self):
        RPS=['rock','scissor','paper']
        global z
        z=random.choice(RPS)
        y='scissor'
        self.app.z=str(z)
        print(z,y)
        if z==y:
            print("draw")
            global w
            w="it was a draw"
            self.app.w=str(w)
        elif z=='rock':
            if y=='scissor':
                print('you lost')
                global counto
                counto+=1
                self.app.counto=str(counto)
                w="YOU LOST!"
                self.app.w=str(w)
            else:
                pass
        elif z=='paper':
            if y=='scissor':
                global count
                print("you won")
                count+=1
                self.app.count=str(count)
                w="YOU WON!"
                self.app.w=str(w)  
            else:
                pass
    def clear(self):
        global count
        global counto
        count=0
        counto=0
        

class score(Screen):
    def on_enter(self,*args):
        self.app=App.get_running_app()
        self.app.count=str(count)
        self.app.counto=str(counto)
    def clear(self):
        global count
        global counto
        count=0
        counto=0
        self.app.count=str(count)
        self.app.counto=str(counto)

class second(Screen):
    def on_enter(self,*args):
        self.app=App.get_running_app()
        self.app.player1=str(player1)
        self.app.player2=str(player2)
        self.app.a=str(a)
    def rock(self):
        global a
        a="rock"
        self.app.a=str(a)
    def scissor(self):
        a="scissor"
        self.app.a=str(a)
        print(a)
    def paper(self):
        a="paper"
        self.app.a=str(a)

class third(Screen):
    def on_enter(self,*args):
        self.app=App.get_running_app()
        self.app.player1=str(player1)
        self.app.player2=str(player2)
        self.app.w=str(w)
        self.app.b=str(b)
    def rock(self):
        global b
        b="rock"
        self.app.b=str(b)
        if self.app.a==b:
            print("draw")
            global w
            w="it was a draw"
            self.app.w=str(w)
            print(a,b)
        elif self.app.a=='paper':
            if b=='rock':
                print('you lost')
                global player1
                player1+=1
                print(player1)
                self.app.player1=str(player1)
                w="player 1 WON!"
                self.app.w=str(w)
                print(a,b)
            else:
                pass
                
        elif self.app.a=='scissor':
            global player2
            print("you won")
            player2+=1
            print(player2)
            self.app.player2=str(player2)
            w="player 2 WON!"
            self.app.w=str(w)
            print(a,b)

    def scissor(self):
        b="scissor"
        self.app.b=str(b)
        if self.app.a==b:
            print("draw")
            global w
            w="it was a draw"
            self.app.w=str(w)
        elif self.app.a=='paper':
            if b=='scissor':
                global player2
                print("you won")
                player2+=1
                print(player2)
                self.app.player2=str(player2)
                w="player 2 WON!"
                self.app.w=str(w)
                print(a,b)

            else:
                pass
                
        elif self.app.a=='rock':
            if b=='scissor':
                print('you lost')
                global player1
                player1+=1
                print(player1)
                self.app.player1=str(player1)
                w="player 1 WON!"
                self.app.w=str(w)
                print(a,b)
            else:
                pass
    def paper(self):
        b="paper"
        self.app.b=str(b)
        if self.app.a==b:
            print("draw")
            global w
            w="it was a draw"
            self.app.w=str(w)
            print(a,b)
        elif self.app.a=='scissor':
            if b=='paper':
                print('you lost')
                global player1
                player1+=1
                print(player1)
                self.app.player1=str(player1)
                w="player 1 WON!"
                self.app.w=str(w)
                print(a,b)
            else:
                pass
                
        elif self.app.a=='rock':
            if b=='paper':
                global player2
                print("you won")
                player2+=1
                print(player2)
                self.app.player2=str(player2)
                w="player 2 WON!"
                self.app.w=str(w)
                print(a,b)
            else:
                pass
        def clear(self):
            global player1
            global player2
            player1=0
            player2=0


class result(Screen):
    def on_enter(self,*args):
        self.app=App.get_running_app()
        self.app.player1=str(player1)
        self.app.player2=str(player2)
    def clear(self):
        global player1
        global player2
        player1=0
        player2=0
        self.app.player1=str(player1)
        self.app.player2=str(player2)
    
class AwesomeApp(App):
    count=StringProperty()
    count2=StringProperty()
    counto=StringProperty()
    player1=StringProperty()
    player2=StringProperty()
    z=StringProperty()
    w=StringProperty()
    a=StringProperty()
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(Mainpage(name='main'))
        sm.add_widget(MyLayout(name='menu'))
        sm.add_widget(score(name='score'))
        sm.add_widget(second(name='pvp'))
        sm.add_widget(third(name='pvp2'))
        sm.add_widget(result(name='re'))
        sm.add_widget(Settings(name='settings'))
        Window.clearcolor=(0.7,0.1,0,0.25)
        return sm


if __name__=='__main__':
    AwesomeApp().run()
