from turtle import*
import random
speed(0)
a=1
penup()
goto(-180,0)
right(90)
for i in range(11,1,-1):
  pendown()
  write(a,align='center')
  for j in range(30):
    forward(5)
    penup()
    forward(5)
    pendown()
  penup()
  goto(-15*i,0)
  penup()
  a+=1
  
red=Turtle()
red.penup()
red.color('red')
red.shape('turtle')
#for a in range(1,5):
red.goto(-180,-40)
red.right(360)
red.pendown()

blue=Turtle()
blue.color('blue')
blue.shape('turtle')
blue.penup()
blue.goto(-180,-80)
blue.left(360)
blue.pendown()

green=Turtle()
green.color('green')
green.shape('turtle')
green.penup()
green.goto(-180,-120)
green.pendown()

yellow=Turtle()
yellow.color('yellow')
yellow.shape('turtle')
yellow.penup()
yellow.goto(-180,-160)
yellow.left(180)
yellow.right(180)
yellow.pendown()


magenta=Turtle()
magenta.color('magenta')
magenta.shape('turtle')
magenta.penup()
magenta.goto(-180,-190)
magenta.right(180)
magenta.left(180)
magenta.pendown()

for i in range(15):
  red.speed(random.randint(0,10))
  blue.speed(random.randint(0,10))
  green.speed(random.randint(0,10))
  yellow.speed(random.randint(0,10))
  magenta.speed(random.randint(0,10))
  red.forward(10)
  blue.forward(10)
  green.forward(10)
  yellow.forward(10)
  magenta.forward(10)