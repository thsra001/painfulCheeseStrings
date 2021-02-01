import os
from time import sleep
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def typew(lmao):
 for i in range (len(lmao)):
  print (lmao[0:i+1])
  sleep(0.1)
  cls()
 print(lmao)

def tutorial():