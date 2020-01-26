import sys
#introduction message
print("Welcome to your new favorite game, the 100 percent accurate Magnet Simulator. We'll start in the Magnet building.")

def auditorium():
  '''first choice in the game'''
  print("You wake up in the MHS auditorium. Do you: ")
  aud = input("a) go back to sleep? b) get up and get back to the grind?  ")
  if aud.lower() == "a":
    print("you foolish fool. you fall back to sleep, and Bruce sees and puts a pillow behind your head, but he also locks you in and you can't make it to class.")
    sys.exit()
  elif aud.lower() == "b":
    class1()
  return aud

def class1():
  '''second choice after leaving auditorium'''
  print("Now that you're up, do you go to class?")
  onetwo = input("a) nope b) of course!  ")
  if onetwo.lower() == "a":
    print("how did you even get into this school?")
    sys.exit()
  elif onetwo.lower() == "b":
    participate()
  return onetwo


def participate():
  '''choice while in class1'''
  print("Will you participate in class?")
  part = input("a) no thanks b) sure  ")
  if part.lower == "a":
    print("you vibe for a while, but the teacher calls on you anyway. have fun with what comes next.")
  elif part.lower == "b":
    print("good for you, but have fun with what comes next.")
  ANXIETY()
  return part
  
def ANXIETY():
  '''anxiety fight'''
  print("You hear tense battle music from somebody's headphones. ANXIETY appears!")
  zozo = input("What do you do? a) FIGHT! b) aaa run!  ")
  if zozo == "a":
      print("good job, facing your fears was the right answer!")
      threefour()
  elif zozo == "b":
      print("you run away, making a screeching sound as you do so. This does nothing to help you at all and you fail.")
      sys.exit()
  return zozo

def threefour():
  '''second class of the day, after anxiety fight'''
  Luck = False
  class2 = input("next class. do you a) prepare for midterms? or b) look at memes?  ")
  if class2 == "a":
      print("you feel stressed, but this is better in the long run.")
      Luck == True
      Lunch()
  elif class2 == "b":
      print("you feel more relaxed, but this could be detrimental in the long run.  ")
      Luck == False
      Harsh()  
  return Luck

def Lunch():
  '''after 3/4. only a choice if Luck is True'''
  if threefour == True:
      lun = input("you can a) eat your lunch or b) wander around. what do you do?  ")
      if lun == "a":
          print("your hunger is sated.")
          Spanish()
      elif lun =="b":
          Harsh()
  elif threefour == False:
      print("you already ate your lunch, so you wander around.")
      Harsh()
  return lun

def Harsh():
  '''Hard to define, but here, he offers you a choice.'''
  epic = input("you run into Harsh, who has hacked the game and offers you a choice: a) skip to the final boss or b) be academically honest.  ")
  if epic == "a":
      print("Harsh pushes some buttons and sends you to the final boss. Get ready!!")
      Sans()
  elif epic == "b":
      print("Harsh respects your decision, but is secretly disappointed in you. You die of shame.")
      sys.exit()
  return epic

def Spanish():
  '''choice after going to lunch.'''
  esp = input("spanish class. do you speak a) english or b) spanish this period?  ")
  if esp.lower == "a":
      print("being monolingual? that's kinda cringe. try again.")
      sys.exit()
  elif esp.lower == "b":
      print("muy bien, you make it through spanish class.")
      Sans()
  return esp

def popquiz():
  '''Mr. Sanservino's pop quiz'''
  print("Mr. Sans laughs and gives you a pop quiz.")
  print("Quick! What college are you going to?")
  pop = input("a) Duke? b) literally anywhere else")
  if pop == "a":
    print("You get a 0 and you know why.")
    sys.exit()
  elif pop == "b":
    print("Even if it's not NC State, Mr. Sans respects your choice. He gives you some pretty dope college advice.")
    print("You win! You have achieved the rank: Master of Vibes.")
    sys.exit()
  return pop

def Sans():
  '''the final boss fight.'''
  print("You hear a familiar voice. Megalovania begins to play... Mr. Sans(ervino) appears!")
  print("Mr. Sans stands menacingly before you... What now?")
  #variable named after first four notes of megalovania, not just nonsense
  DDdA = input("a) Stand your ground. b) Beg for a good grade c) Konami Code")
  if DDdA.lower == "a":
      print("You t pose on the final boss. are you lucky enough for it to work?")
      if threefour == True:
          print("Mr. Sans recognizes what you are trying to do. it does not work, but he respects you enough to let you pass.")
          print("You win! You have achieved the rank: Responsible Badass")
          sys.exit()
      elif threefour == False:
        popquiz()
  elif DDdA.lower == "b":
    print("You beg for a good grade.")
    popquiz()
  elif DDdA.lower == "c":
    print("You input the Konami Code. Which one is correct?  ")
    konami = input("a) up up down down left right left right b a b a start or b) left left up down right a b  ")
    if konami.lower == "a":
      print("Correct. You get 30 lives and $69, both of which are irrelevant in this game.")
      print("You win? You have achieved the rank: Harsh-level Hacker")
  
auditorium()
