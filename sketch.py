from p5 import *


def setup():
  global colors,pianokey
  createCanvas(500,500)
  colors=["#f76565", "#f5985b", "#e8f255", "#69f56c", "#62caf0", "#549af0", "#d7a4f5", "#f797d2"]

def draw():
  
  background(0, 0, 0)
  
  layout ()
  
  drawTickAxes()



'''
Project Approach:
1. keyboard
2. keys
3. waves window - 2 screen window - (click to start -> sine wave)
4. instructions

jamboard: https://jamboard.google.com/d/1yxnIxx7NCFXerr-m0dkf7moA8S5tsVnfawk8N6HtNZ0/viewer?mtt=f12tzufamzjv&f=0

Major things:

try using dictionaries and lists majorly here

two dictionaries are must-keyboard, pianokeys

one for all key prop
second for the keyboard prop

'''
def layout ():
  noStroke ()
  #strokeWeight (0.5)

  
  
  global red, orange, yellow, green, blue, indigo, violet, pink
  fill ("#f76565") 
  red = rect (150, 350, 25, 100, 10)
  fill ("#f5985b")  
  orange = rect (175, 350, 25, 100, 10)
  fill ("#e8f255")
  yellow = rect (200, 350, 25, 100, 10)
  fill ("#69f56c")
  green = rect (225, 350, 25, 100, 10)
  fill ("#62caf0")
  blue = rect (250, 350, 25, 100, 10)
  fill ("#549af0")
  indigo = rect (275, 350, 25, 100, 10)
  fill ("#d7a4f5")
  violet = rect (300, 350, 25, 100, 10)
  fill ("#f797d2")
  pink = rect (325, 350, 25, 100, 10)
  
  
  
  
