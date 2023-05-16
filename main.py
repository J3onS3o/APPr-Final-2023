import time

#main function of the quiz
def main(): 
  global attributes

  attributes = [] #holds girly pop attributes of the player
  
  print("Hey besties~") 
  time.sleep(3)
  print("Welcome to the GirlyPop Quiz. Answer a few questions to   see how GirlyPop you are !! :D")
  quesOne()
  quesTwo()
  quesThree()
  quesFour()
  quesFive()
  rank = ranking()
  result(rank)


time.sleep(3.5)

def quesOne():
  qO = str(input(print("have you ever felt any romantic attraction to a live, breathing, HUMAN being, that you didn't see through a screen? (Y/N)"))).lower()
  
  if qO == "y" or qO == "yes": 
    attributes.append("romantic")
  elif qO == "n" or qO == "no": 
    print(":(")
  else:
    print("Not a valid answer.")
    quesOne()

def quesTwo():
  qTw = str(input(print("(question HARD EDITION) will you ever touch grass??? (Y/N)"))).lower()
  if qTw == "y" or qTw == "yes": 
    attributes.append("grass-toucher")
  elif qTw == "n" or qTw == "no": 
    print(":(")
  else: 
    print("Not a valid answer.")
    quesTwo()

def quesThree():
  qTh = str(input(print("what trait describes you best? 'bubbly', 'quiet', 'chaotic'?"))).lower()
  if qTh == "bubbly":
    attributes.append("bubbly")
  elif qTh == "chaotic": 
    attributes.append("chaotic")
  elif qTh == "quiet": 
    print(":(")
  else: 
    print("Not a valid option")
    quesThree()

def quesFour(): 
  qFo = int(input(print("on a scale from 1-10 with 10 being the best, rate The Barbie Movie")))
  
  if qFo == 10: 
    attributes.append("Barbie Stan")
  elif qFo < 10 and qFo >= 5: 
    attributes.append("Barbie Watcher")
  elif qFo < 5: 
    print(":(")
  else:
    print("Not a valid input")
    quesFour()

def quesFive():
  qFi = str(input(print("Do you think you are girlypop?!? <3 (Y/N)"))).lower()
  if qFi == "y" or qFi == "yes": 
    attributes.append("ANOTHER DAY ANOTHER SLAYYY !!")
  elif qFi == "n" or qFi == "no": 
    print(":(")
  else: 
    print("Not a valid answer.")
    quesFive()

def ranking(): 
  attAmt = len(attributes)
  girlypop = False 
  
  if attAmt >= 4: 
    girlypop = True 
  elif attAmt >= 2 or attAmt == 3: 
    girlypop = True
  elif attAmt <= 1:
    girlypop = False
    
  return girlypop

def result(girlypop): 
  if girlypop == True:
    print("CONGRATS <3 YOU ARE GIRLY POP !!")
    for x in range(len(attributes)): 
      print("Girlypop Attribute: " + attributes[x])
  elif girlypop == False:
    print("Awww...not quite girlypop enough...")

main()
