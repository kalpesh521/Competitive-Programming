import turtle
from turtle import *
ws =Screen()
ws.bgcolor('white')
t =turtle.Turtle
ht()
speed(0)

penup()
rt(90)
bk(120)
pendown()
color("orange")
pensize(4)
lt(100)
for up in range(20):
    fd(6)
    rt(8)
lt(22)
fd(50)

for down in range(20):
    fd(8)
    lt(10)

penup()
pencolor("purple")
home()
lt(90)
fd(122)
pendown()
pensize(3)
rt(90)
for up in range(10):
    fd(4)
    lt(25)
for down in range(10):
    fd(4)
    rt(6)

pensize(3)
penup()
st()
home()
lt(90)
fd(122)
rt(90)
fd(25)
lt(12)
pendown()
lt(45)
for up in range(10):
    fd(9)
    lt(23)
lt(200)
for up in range(10):
    fd(6)
    lt(23)
penup()
home()
lt(90)
fd(160)
pendown()
lt(90)
for up in range(5):
    fd(4)
    rt(15)
for down in range(5):
    fd(4)
    lt(16)
lt(120)
for up in range(5):
    fd(4)
    rt(15)
for down in range(5):
    fd(4)
    lt(16)

#Ear
penup()
rt(40)
fd(36)
lt(27)
pendown()
pencolor("orange")
for up in range(5):
    fd(14)
    rt(15)
rt(45)
penup()

fd(7)
rt(100)
pendown()
for up in range(10):
    fd(2)
    lt(8)
for up in range(10):
    fd(3)
    rt(13)
for up in range(10):
    fd(3)
    lt(8)
penup()
rt(17)
bk(50)
pendown()
pensize(3)
rt(10)
for up in range(10):
    fd(1)
    lt(8)
for up in range(10):
    fd(2)
    rt(16)
penup()
fd(50)
lt(90)
fd(40)
lt(90)
pendown()
pensize(4)
for up in range(10):
    fd(4)
    lt(4)
penup()
lt(100)
fd(43)
pencolor("black")
pensize(2)
pendown()
rt(10)
for up in range(10):
    fd(1)
    lt(6)
for down in range(10):
    fd(1)
    rt(6)
penup()
pensize(3)
bk(5)
rt(90)
fd(5)
pendown()
for up in range(10):
    fd(1)
    rt(30)
penup()
lt(40)
fd(5)
rt(100)
pendown()
pensize(1)
for up in range(10):
    fd(2)
    rt(15)
penup()
lt(125)
bk(47)
pendown()
pensize(3)
pencolor("red")
rt(30)
for up in range(10):
    fd(1)
    rt(5)
for up in range(10):
    fd(1)
    lt(3)
penup()
rt(15)
bk(23)
pendown()
lt(35)
for up in range(10):
    fd(1)
    rt(3)
for up in range(10):
    fd(2)
    rt(3)
pencolor('orange')
penup()
lt(125)
fd(90)
pendown()

lt(40)
for up in range(10):
    fd(3)
    lt(8)
rt(170)
for up in range(10):
    fd(3)
    rt(8)
penup()
lt(30)
bk(18)
lt(120)
pendown()
pensize(3)
for up in range(15):
    fd(4)
    lt(2)
for up in range(15):
    fd(3)
    lt(3)
for up in range(15):
    fd(3)
    lt(3)
pensize(2)
for up in range(15):
    fd(4)
    lt(5)
ht()
mainloop()



