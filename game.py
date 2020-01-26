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

def class1():
  '''second choice after leaving auditorium'''
  onetwo = input("Now that you're up, do you go to class? a) nope b) of course!  ")
  if onetwo.lower() == "a":
    print("how did you even get into this school?")
    sys.exit()
  elif onetwo.lower() == "b":
    participate()


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
  print("You hear tense battle music from somebody's headphones. ANXIETY appears!")
  zozo = input("What do you do? a) FIGHT! b) aaa run!")
  if zozo == "a":
      print("good job, facing your fears was the right answer!")
      threefour()
  elif zozo == "b":
      print("you run away, making a screeching sound as you do so. This does nothing to help you at all and you fail.")
      sys.exit()

def threefour():
  '''second class of the day, after anxiety fight'''
  Luck = False
  class2 = input("next class. do you a) prepare for midterms? or b) look at memes?  ")
  if class2 == "a":
      print("you feel stressed, but this is better in the long run.")
      Luck == True
  elif class2 == "b":
      print("you feel more relaxed, but this could be detrimental in the long run.  ")
      Luck == False  

def Lunch():
  '''after 3/4. only a choice if Luck is True'''
  if Luck == True:
      lun = input("you can a) eat your lunch or b) wander around. what do you do?  ")
      if lun == "a":
          print("your hunger is sated.")
          Spanish()
      elif lun =="b":
          Harsh()
  elif Luck == False:
      print("you already ate your lunch, so you wander around.")
      Harsh()

def Harsh():
  '''Hard to define, but here, he offers you a choice.'''
  epic = input("you run into Harsh, who has hacked the game and offers you a choice: a) skip to the final boss or b) be academically honest.  ")
  if epic == "a":
      print("Harsh pushes some buttons and sends you to the final boss. Get ready!!")
      Sans()
  elif epic == "b":
      print("Harsh respects your decision, but is secretly disappointed in you. You die of shame.")
      sys.exit()

def Spanish():
  '''choice after going to lunch.'''
  esp = input("spanish class. do you speak a) english or b) spanish this period?  ")
  if esp == "a":
      print("being monolingual? that's kinda cringe. try again.")
      sys.exit()
  elif esp == "b":
      print("muy bien, you make it through spanish class.")
      Sans()
  else:
      esp = input("please choose a or b.  ")

def intimidate():
  '''choice one of the final fight''' 

def popquiz():
  '''choice two of the final fight'''

def Sans():
  '''the final boss fight.'''
  print("You hear a familiar voice. Megalovania begins to play... Mr. Sans(ervino) appears!")
  print("Mr. Sans stands menacingly before you... What now?")
  ddda = input("a) stand your ground. b) beg for a good grade c) up up down down left right left right b a b a start.  ")
  if ddda == "a":
      print("you t pose on the final boss. are you lucky enough for it to work?")
      if Luck == True:
          print("Mr. Sans recognizes what you are trying to do. it does not work, but he respects you enough to let you pass. You win!")
          
  
auditorium()
#NTS return your functions before you wonder why they don't work