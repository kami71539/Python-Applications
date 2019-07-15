from turtle import *
import random

#---------------------------------------
def Turtle():
  penup()
  def turtle_pos():
    shape('turtle')
    coordinates()
    
  def turtle_heading():
    d=random.randint(80,90)
    right(d)

  for i in range(10):
    turtle_colors()
    turtle_heading()
    turtle_pos()
    stamp()

#-------------------------------------
def rectangle():
  for j in range(10):
    penup()
    x=random.randint(-150,150)
    y=random.randint(-150,150)
    coordinates()
    begin_fill()
    for i in range(2):
      hideturtle()
      pendown()
      begin_fill()
      forward(x)
      right(90)
      forward(y)
      right(90)
    end_fill()
    turtle_colors()
#-------------------------------------
def turtle_dot():
  for i in range(10):
    turtle_colors()
    penup()
    radius=random.randint(-150,150)
    coordinates() 
    dot(radius)
#-------------------------------------
def star():
  for quantity in range(6):
    begin_fill()
    turtle_colors()
    penup()
    coordinates()
    for side in range(5):
      left(144)
      forward(50)
    end_fill()
#-------------------------------------

def turtle_colors():
      red=random.randint(0,255)
      blue=random.randint(0,255)
      green=random.randint(0,255)
      color(red,blue,green)  
  
def coordinates():
  x=random.randint(-150,150)
  y=random.randint(-150,150)
  goto(x,y)

print("Welcome to the modern art.")

pick=input("Take your pick \n")
pick=pick.lower()
speed()
penup()
if pick=='turtle':
  Turtle()
elif pick=='rectangle':
  rectangle()
elif (pick=='dot'):
  turtle_dot()
elif (pick=='star'):
  star()
else:
  star()
  turtle_dot()
  rectangle()
  Turtle()