from gtts import gTTS
import os

from tkinter import *
root = Tk()
t = 1
root.geometry('195x195')
root.config(bg="black")
p=0

def p1():

    root.config(bg="red")
    l1.config(text="PLAYER 1 WON!",bg="red",fg="yellow",font="bold")
    x=gTTS(text="player 1 wins",lang="en",slow=False)
    x.save("p1.mp3")
    os.system("start p1.mp3")
    global p
    p=1

def p2():

    root.config(bg="yellow")
    l1.config(text="PLAYER 2 WON!",bg="yellow",fg="red",font="bold")
    x=gTTS(text="player 2 wins",lang="en",slow=False)
    x.save("p1.mp3")
    os.system("start p1.mp3")
    global p
    p=1

def draw():
    root.config(bg="orange")
    l1.config(text="DRAW",bg="orange",fg="yellow")
    x=gTTS(text="DRAW",lang="en",slow=False)
    x.save("p1.mp3")
    os.system("start p1.mp3")

def check():
    a = b1["text"]
    b = b2["text"]
    c = b3["text"]
    d = b4["text"]
    e = b5["text"]
    f = b6["text"]
    g = b7["text"]
    h = b8["text"]
    i = b9["text"]
    count = 0

    if len(a)!=0 and len(b)!=0 and len(c)!=0:
        if a==b and a==c:
            if a=="X":
                p1()
            else:
                p2()
        count=count+1

    if len(d)!=0 and len(e)!=0 and len(f)!=0:
        if d==e and d==f:
            if d=="X":
                p1()
            else:
                p2()
        count=count+1

    if len(g)!=0 and len(h)!=0 and len(i)!=0:
        if g==h and g==i:
            if g=="X":
                p1()
            else:
                p2()
        count = count + 1

    if len(a)!=0 and len(d)!=0 and len(g)!=0:
        if a==d and d==g:
            if d=="X":
                p1()
            else:
                p2()
        count = count + 1

    if len(b)!=0 and len(e)!=0 and len(h)!=0:
        if b==e and b==h:
            if b=="X":
                p1()
            else:
                p2()
        count = count + 1

    if len(c)!=0 and len(f)!=0 and len(i)!=0:
        if c==f and c==i:
            if c=="X":
                p1()
            else:
                p2()
        count = count + 1

    if len(a)!=0 and len(e)!=0 and len(i)!=0:
        if a==e and a==i:
            if a=="X":
                p1()
            else:
                p2()
        count = count + 1

    if len(c)!=0 and len(e)!=0 and len(g)!=0:
        if c==e and c==g:
            if c=="X":
                p1()
            else:
                p2()
        count = count + 1

    if count==8 and p==0:
        draw()

def bt1():
  if len(b1["text"])==0:
    global t
    if t % 2 == 1:
        b1.config(text="X",bg="red",fg="yellow",font="bold")
        l1.config(text=" 2nd player's turn")
    else:
        b1.config(text="O",bg="yellow",fg="red",font="bold")
        l1.config(text=" 1st player's turn")

    t = t + 1
    check()

def bt2():
  if len(b2["text"])==0:
    global t
    if t % 2 == 1:
        b2.config(text="X",bg="red",fg="yellow",font="bold")
        l1.config(text=" 2nd player's turn")
    else:
        b2.config(text="O",bg="yellow",fg="red",font="bold")
        l1.config(text=" 1st player's turn")
    t = t + 1
    check()

def bt3():
  if len(b3["text"])==0:
    global t
    if t % 2 == 1:
        b3.config(text="X",bg="red",fg="yellow",font="bold")
        l1.config(text=" 2nd player's turn")
    else:
        b3.config(text="O",bg="yellow",fg="red",font="bold")
        l1.config(text=" 1st player's turn")
    t = t + 1
    check()

def bt4():
  if len(b4["text"])==0:
    global t
    if t % 2 == 1:
        b4.config(text="X",bg="red",fg="yellow",font="bold")
        l1.config(text=" 2nd player's turn")
    else:
        b4.config(text="O",bg="yellow",fg="red",font="bold")
        l1.config(text=" 1st player's turn")
    t = t + 1
    check()

def bt5():
  if len(b5["text"])==0:
    global t
    if t % 2 == 1:
        b5.config(text="X",bg="red",fg="yellow",font="bold")
        l1.config(text=" 2nd player's turn")
    else:
        b5.config(text="O",bg="yellow",fg="red",font="bold")
        l1.config(text=" 1st player's turn")
    t = t + 1
    check()

def bt6():
  if len(b6["text"])==0:
    global t
    if t % 2 == 1:
        b6.config(text="X",bg="red",fg="yellow",font="bold")
        l1.config(text=" 2nd player's turn")
    else:
        b6.config(text="O",bg="yellow",fg="red",font="bold")
        l1.config(text=" 1st player's turn")
    t = t + 1
    check()

def bt7():
  if len(b7["text"])==0:
    global t
    if t % 2 == 1:
        b7.config(text="X",bg="red",fg="yellow",font="bold")
        l1.config(text=" 2nd player's turn")
    else:
        b7.config(text="O",bg="yellow",fg="red",font="bold")
        l1.config(text=" 1st player's turn")
    t = t + 1
    check()

def bt8():
  if len(b8["text"])==0:
    global t
    if t % 2 == 1:
        b8.config(text="X",bg="red",fg="yellow",font="bold")
        l1.config(text=" 2nd player's turn")
    else:
        b8.config(text="O",bg="yellow",fg="red",font="bold")
        l1.config(text=" 1st player's turn")
    t = t + 1
    check()

def bt9():
  if len(b9["text"])==0:
    global t
    if t % 2 == 1:
        b9.config(text="X",bg="red",fg="yellow",font="bold")
        l1.config(text=" 2nd player's turn")
    else:
        b9.config(text="O",bg="yellow",fg="red",font="bold")
        l1.config(text=" 1st player's turn")
    t = t + 1
    check()
l1=Label(text="TIC TAC TOE",bg="black",fg="white",font="bold")
b1 = Button(text="",bg="white", command=bt1)
b2 = Button(text="",bg="white", command=bt2)
b3 = Button(text="",bg="white", command=bt3)
b4 = Button(text="",bg="white",command=bt4)
b5 = Button(text="",bg="white",command=bt5)
b6 = Button(text="",bg="white", command=bt6)
b7 = Button(text="",bg="white", command=bt7)
b8 = Button(text="",bg="white", command=bt8)
b9 = Button(text="",bg="white", command=bt9)

l1.place(x=0,y=0,height=50,width=200)
b1.place(x=50,y=50,height=30,width=30)
b2.place(x=80,y=50,height=30,width=30)
b3.place(x=110,y=50,height=30,width=30)
b4.place(x=50,y=80,height=30,width=30)
b5.place(x=80,y=80,height=30,width=30)
b6.place(x=110,y=80,height=30,width=30)
b7.place(x=50,y=110,height=30,width=30)
b8.place(x=80,y=110,height=30,width=30)
b9.place(x=110,y=110,height=30,width=30)

mainloop()