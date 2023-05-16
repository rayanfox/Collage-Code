import os
from tkinter import messagebox

#if else

age = input("How old are you? ")
#age = int(age);
if int(age) < 0:
     print ("A valid age")
elif int(age) < 16:
  print ("Too young for RSC")
elif int(age) >=16 and int(age) <= 18:
  print("Concurrent enrollment")
elif int(age) == 21:
  print("Legal drinking age")
elif int(age) <25:
  print("Traditional enrollment")
elif int(age) <65:
  print("Workforce Development")
elif int(age) <135:
  print("Senior Citizen discount")

#os.system("pause")

# Nested if 

a = 80
b = 80
c = 70

if (a>b):
  if(a>c):
    print("a is biggest")
if (b>c):
  if (b>c):
    print("b is biggest") 
if (c>a):
  if(c>b):
    print("c is biggest")       

# message box



