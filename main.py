# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import turtle
import random

r=random.Random()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def gradientCircle():
    t.pensize(30)
    for i in range(150):
        if i<= 100:
            t.pencolor(((100-i), (100-i), (200-i)))
        else:
            t.pencolor((0, 0, (200 - i)))
        t.circle(5*i)
        t.sety(-i*5)


def dotsStar(n):
    t.pensize(3)
    for i in range(n):
        t.color((r.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
        t.penup()
        t.setposition(random.randint(-750, 750),random.randint(-750, 750))
        t.pendown()
        t.circle(1)


def gradientCircle2(tam):
    t.pensize(5)
    t.setpos(0,0)
    t.left(0)
    t.pendown()
    for i in range(tam):
        print(i)
        if i<= 50:
            t.pencolor(((50-i), (200-i), (250-i)))
        else:
            t.pencolor((0, (200-i), (250 - i)))
        #t.pencolor('black')
        t.circle(1*i)
        t.sety(-i*2)

def aneisUp(tam):
    t.pensize(1)
    px = t.xcor()
    py = t.ycor()
    t.color((255, 0, 255))
    #t.setposition(px+tam/2, py+tam/2)
    t.left(0)
    for i in range(20):
        t.penup()
        t.setposition(px + tam*2.2, py-i + tam*1.5)
        t.pencolor(((250-i*2), i*5, (250-i*3)))
        t.pendown()
        t.circle(tam*10+i*3, -25)
        t.left(25)
        t.penup()
        t.sety(-i)

def aneisDown(tam):
    t.pensize(1)
    px = t.xcor()
    py = t.ycor()
    t.color((255, 0, 255))
    #t.setposition(px+tam/2, py+tam/2)
    t.left(0)
    for i in range(20):
        t.penup()
        t.setposition(px - tam*2.2 - i*2, py-i + tam*1.5)
        t.pencolor(((250-i*5), i*12, (250-i*3)))
        t.pendown()
        t.circle(tam*10+i*10, 25)
        t.left(-25)
        t.penup()
        t.sety(-i)

def nada(x,y):
    print("ssssssss")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    t = turtle.Turtle()
    s=turtle.Screen()
    s.colormode(255)
    t.color((255, 255, 255))
    t.speed(50)

    gradientCircle()
    dotsStar(100)
    t.penup()
    t.setpos(-0,-100)
    t.pendown()
    #aneisUp(30)
    t.penup()
    t.setpos(0,0)
    t.pendown()
    gradientCircle2(50)
    aneisDown(30)
    #s.listen()
    s.onscreenclick(nada)
    #s.mainloop()
    turtle.done()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
