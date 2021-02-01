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
 typew("this is little tommyboi")
 print("       |๏ ͜ʖ๏|")
 e=input("")
 cmd = 0
 while not cmd == "!feed":
  cls()
  typew("feed him with !𝙛𝙚𝙚𝙙")
  print("       |๏ ͜ʖ๏|")
  cmd = input("")
 while not cmd == "!bath":
 cls()
 typew("good, now give him a bath with !𝙗𝙖𝙩𝙝")
 cmd = input("")
 cls()
 typew("great, now you are ready to take care of tommyboi!")