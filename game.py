import sys
#introduction message
print("Welcome to your new favorite game, the 100 percent accurate Magnet Simulator. Get ready to start! ")

def auditorium():
  '''first choice in the game'''
  aud = input("You wake up in the MHS auditorium. do you: a) go back to sleep? b) get up and get back to the grind?  ")
  if aud.lower() == "a":
    print("you foolish fool. you fall back to sleep, and Bruce sees and puts a pillow behind your head, but he also locks you in and you can't make it to class.")
    sys.exit()
  elif aud.lower() == "b":
    class1()
  else:
    aud = input("please choose a or b.")

def class1():
  '''second choice after leaving auditorium'''
  onetwo = input("Now that you're up, do you go to class? a) nope b) of course!  ")
  if onetwo.lower() == "a":
    print("how did you even get into this school?")
    sys.exit
  elif onetwo.lower() == "b":
    participate()
  else:
    onetwo = input ("please choose a or b")

def participate():
  '''choice while in class1'''
  part = input("will you participate in class? a) no thanks b) sure")
  if part.lower == "a":
    print("you vibe for a while, but the teacher calls on you anyway. have fun with what comes next.")
  elif part.lower == "b":
    print("good for you. have fun with what comes next.")
  ANXIETY()
  
def ANXIETY():
  '''anxiety fight'''

def threefour():
  '''second class of the day, after anxiety fight'''

def Lunch():
  '''after 3/4. only a choice if Luck is True'''

def Harsh():
  '''Hard to define, but here, he offers you a choice.'''

def Spanish():
  '''choice after going to lunch.'''

def intimidate():
  '''choice one of the final fight''' 

def popquiz():
  '''choice two of the final fight'''

def Sans():
  '''the final boss fight.'''
  print("You hear a familiar voice. Megalovania begins to play... Mr. Sans(ervino) appears!")

auditorium()