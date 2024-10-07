from tkinter import *
import random
import tkinter as tk
from tkinter import ttk
import winsound
from PIL import *
from PIL import Image, ImageTk
from tkinter import ttk

#start of GUI
window=tk.Tk()
window.title("Vydehi School of Excellence | Student Council 2022-23 Election Voting ")
window.attributes("-fullscreen",True)

#notebook deployed
notebook = ttk.Notebook(window)
notebook.place(x=0,y=0)

#images
front_img_2=Image.open("AR.png")
resize_vselogo_img=front_img_2.resize((225,225))
img=ImageTk.PhotoImage(resize_vselogo_img)
ImgLabel=Label(frame1,image=img)
ImgLabel.front_img_2=img
ImgLabel.place(x=1170, y=0)

#frames
frame1 = ttk.Frame(notebook,width=10000,height=900)

frame2 = ttk.Frame(notebook,width=10000,height=900)

frame3 = ttk.Frame(notebook,width=10000,height=900)

frame4 =  ttk.Frame(notebook,width=10000,height=900)

frame5 =  ttk.Frame(notebook,width=10000,height=900)

frame6 =  ttk.Frame(notebook,width=10000,height=900)

frame7 =  ttk.Frame(notebook,width=10000,height=900)


#frames placed
frame1.place(x=0,y=0)

frame2.place(x=0,y=0)

frame3.place(x=0,y=0)

frame4.place(x=0,y=0)

frame5.place(x=0,y=0)

frame6.place(x=0,y=0)

frame7.place(x=0,y=0)

#frames deployed
notebook.add(frame1, text='0')

notebook.add(frame2, text='1')

notebook.add(frame3, text='2')

notebook.add(frame4, text='3')

notebook.add(frame5, text='4')

notebook.add(frame6, text='5')

notebook.add(frame7, text='6')

#hiding the tab tiles

#variables
winsound.PlaySound('song (1).wav',winsound.SND_ASYNC  + winsound.SND_LOOP)
count=0
counto=0
z=0
player1=0
player2=0
a='a'
b='b'
e=0
counti='0'
countoi='0'
countp = StringVar()
countop = StringVar()
countop.set(countoi)
countp.set(counti)

#images
photo1=Image.open("rock.png")
resize_button_img1=photo1.resize((500,500))
img1=ImageTk.PhotoImage(resize_button_img1)

photo2=Image.open("paper.png")
resize_button_img2=photo2.resize((250,325))
img2=ImageTk.PhotoImage(resize_button_img2)

photo3=Image.open("scissor.png")
resize_button_img3=photo3.resize((250,325))
img3=ImageTk.PhotoImage(resize_button_img3)

photo4=Image.open("setting.png")
resize_button_img4=photo4.resize((250,325))
img4=ImageTk.PhotoImage(resize_button_img4)


#commands
def play_music():
    global e
    e+=1
    if e%2==0:
        print(e)
        winsound.PlaySound('song (1).wav',winsound.SND_ASYNC  + winsound.SND_LOOP)
    else:
        print(e)
        winsound.PlaySound(None, winsound.SND_PURGE)


def go_to_main_menu():
    notebook.select(0)

def go_to_AI_result_rock():
    notebook.select(2)
    RPS=['rock','scissor','paper']
    global z
    z=random.choice(RPS)
     
    y='rock'
    print(z,y)
    if z==y:
        print("draw")
        global w
        w="it was a draw"
        
    elif z=='paper':
        if y=='rock':
            print('you lost')
            global counto
            global countoi
            counto+=1
            countoi=str(counto)
            countop.set(countoi)
            print(counto)
            
            w="YOU LOST!"
            
            
        else:
            pass
                
    elif z=='scissor':
        if y=='rock':
            global count
            global counti
            print("you won")
            count+=1
            counti=str(count)
            countp.set(counti)
            print(counti)
            
            w="YOU WON!"
            
        else:
            pass

def go_to_AI_result_paper():
    notebook.select(2)
    RPS=['rock','scissor','paper']
    global z
    z=random.choice(RPS)
    
    y='paper'
    print(z,y)
    if z==y:
        print("draw")
        global w
        w="it was a draw"
        
    elif z=='rock':
        if y=='paper':
            print("you won")
            global count
            global counti
            count+=1
            counti=str(count)
            countp.set(counti)
            w="YOU WON!"
            
        else:
            pass
    elif z=='scissor':
        if y=='paper':
            print('you lost')
            global counto
            global countoi
            counto+=1
            countop.set(countoi)
            countoi=str(counto)
            w="YOU LOST!"
            print(counto)
            
        else:
            pass
    

def go_to_AI_result_scissor():
    notebook.select(2)
    RPS=['rock','scissor','paper']
    global z
    z=random.choice(RPS)
    y='scissor'
    
    print(z,y)
    if z==y:
        print("draw")
        global w
        w="it was a draw"
        
    elif z=='rock':
        if y=='scissor':
            print('you lost')
            global counto
            global countoi
            counto+=1
            countoi=str(counto)
            countop.set(countoi)
            w="YOU LOST!"
            print(counto)
        else:
            pass
    elif z=='paper':
        if y=='scissor':
            global count
            global counti
            print("you won")
            count+=1
            counti=str(count)
            countp.set(counti)
            
            w="YOU WON!"
            
        else:
            pass
def clear():
    global count
    global counto
    count=0
    counto=0
    countoi=str(counto)
    countop.set(countoi)
    counti=str(count)
    countp.set(counti)

def go_to_AImode():
    notebook.select(1)

def go_to_player1():
    notebook.select(3)
    
def go_to_player2_rock():
    notebook.select(4)
    global a
    a="rock"

def go_to_player2_paper():
    notebook.select(4)
    a="scissor"
    print(a)

def go_to_player2_scissor():
    notebook.select(4)
    a="paper"
    print(a)

def go_to_result_pvp_rock():
    notebook.select(5)
    global b
    b="rock"
    
    if a==b:
        print("draw")
        global w
        w="it was a draw"
        print(w)
        print(a,b)
    elif a=='paper':
        if b=='rock':
            print('you lost')
            global player1
            player1+=1
            print(player1)
            
            w="player 1 WON!"
            print(w)
            print(a,b)
        else:
            pass
    elif a=='scissor':
            global player2
            print("you won")
            player2+=1
            print(player2)
            
            w="player 2 WON!"
            print(w)
            print(a,b)

def go_to_result_pvp_paper():
    notebook.select(5)
    b="paper"
    
    if a==b:
        print("draw")
        global w
        w="it was a draw"
        print(w)
        print(a,b)
    elif a=='scissor':
        if b=='paper':
            print('you lost')
            global player1
            player1+=1
            print(player1)
            
            w="player 1 WON!"
            print(w)
            print(a,b)
        else:
            pass
    elif a=='rock':
        if b=='paper':
            global player2
            print("you won")
            player2+=1
            print(player2)
            
            w="player 2 WON!"
            print(w)
            print(a,b)
        else:
            pass
def clearo():
    global player1
    global player2
    player1=0
    player2=0
    

def go_to_result_pvp_scissor():
    notebook.select(5)

def go_to_settings():
    notebook.select(6)

#variables


#main frames(add 3 buttons one-AI one-2player and one-settings
button=Button(frame1,text="settings",width=8,height=2,bg="#afd6de",font= ('Helvetica 10 bold'),command=go_to_settings)
button.place(x=1210,y=0)

button=Button(frame1,text="2 player",width=20,height=14,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_player1)
button.place(x=700,y=100)

button=Button(frame1,text="AI mode",width=20,height=14,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_AImode)
button.place(x=180,y=100)

#AI frame or frame 2
button=Button(frame2,text="Rock",width=18,height=14,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_AI_result_rock)
button.place(x=40,y=70)

i=Label(frame2,image=img1)
i.place(x=40,y=150)

button=Button(frame2,text="paper",width=18,height=14,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_AI_result_paper)
button.place(x=450,y=70)

button=Button(frame2,text="scissor",width=18,height=14,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_AI_result_scissor)
button.place(x=860,y=70)


#2player frame(first player) or frame 4 
button=Button(frame4,text="Rock",width=18,height=14,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_player2_rock)
button.place(x=40,y=80)

button=Button(frame4,text="paper",width=18,height=14,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_player2_paper)
button.place(x=450,y=80)

button=Button(frame4,text="scissor",width=18,height=14,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_player2_scissor)
button.place(x=860,y=80)

l1=Label(frame4,text="PLAYER 1:",font=('Helvetica 35 bold'))
l1.place(x=510,y=15,height=35)

#2player frame(second player) or frame 5

button=Button(frame5,text="Rock",width=18,height=14,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_result_pvp_rock)
button.place(x=40,y=70)

button=Button(frame5,text="paper",width=18,height=14,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_result_pvp_paper)
button.place(x=450,y=70)

button=Button(frame5,text="scissor",width=18,height=14,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_result_pvp_scissor)
button.place(x=860,y=70)

l1=Label(frame5,text="PLAYER 2:",font=('Helvetica 35 bold'))
l1.place(x=510,y=15,height=35)

#settings frame
button=Button(frame7,text="MUSIC",width=24,height=4,bg="#afd6de",font= ('Helvetica 25 bold'),command=play_music)
button.place(x=400,y=100)

button=Button(frame7,text="MAIN MENU",width=24,height=4,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_main_menu)
button.place(x=400,y=300)

l1=Label(frame7,text="SETTINGS",font=('Helvetica 35 bold'))
l1.place(x=510,y=30,height=37)

#result_AI frame or frame 3
button=Button(frame3,text="main menu -->",width=24,height=3,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_main_menu)
button.place(x=700,y=530)

button=Button(frame3,text="<-- play again",width=24,height=3,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_AImode)
button.place(x=100,y=530)

button=Button(frame3,text="clear score",width=14,height=2,bg="#afd6de",font= ('Helvetica 25 bold'),command=clear)
button.place(x=500,y=380)

l1=Label(frame3,text="PLAYER SCORE:",font=('Helvetica 25 bold'))
l1.place(x=100,y=150,height=35)

l3=Label(frame3,textvariable = countp,font=('Helvetica 25 bold'))
l3.place(x=380,y=150,height=35)

l4=Label(frame3,textvariable = countop,font=('Helvetica 25 bold'))
l4.place(x=280,y=250,height=35)

l2=Label(frame3,text="AI SCORE:",font=('Helvetica 25 bold'))
l2.place(x=100,y=250,height=35)

#result_2_player or frame 6

button=Button(frame6,text="main menu -->",width=24,height=3,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_main_menu)
button.place(x=700,y=530)

button=Button(frame6,text="<-- play again",width=24,height=3,bg="#afd6de",font= ('Helvetica 25 bold'),command=go_to_player1)
button.place(x=100,y=530)

button=Button(frame6,text="clear score",width=14,height=2,bg="#afd6de",font= ('Helvetica 25 bold'),command=clearo)
button.place(x=500,y=380)

l1=Label(frame6,text="PLAYER 1 SCORE:"+str(player1),font=('Helvetica 25 bold'))
l1.place(x=400,y=150,height=35)


l2=Label(frame6,text="PLAYER 2 SCORE:"+str(player2),font=('Helvetica 25 bold'))
l2.place(x=400,y=250,height=35)







