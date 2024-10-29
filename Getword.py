def getMenuOption(debug = False):
    if debug: print("getMenuOption Function")
    
    goodInput = False 
    
    while not goodInput:
        option = input("Please select an option: ")
        option = option.lower()
        
        if (option == "q" 
        or option == "quit"
        or option == "exit" 
        or option == "credits"):
            option = "q"
            goodInput = True
            
            
         
        elif (option == "1" 
        or option == "one"
        or option == "story 1" 
        or option == "story1"):
            option = "1"
            goodInput = True
            
        elif (option == "2" 
        or option == "two"
        or option == "story 2" 
        or option == "story2"):
            option = "2"
            goodInput = True


        elif (option == "3" 
        or option == "three"
        or option == "story 3" 
        or option == "story3"):
            option = "3"
            goodInput = True
            
        elif (option == "4" 
        or option == "four"
        or option == "story 4" 
        or option == "story4"):
            option = "4"
            goodInput = True

        else:
            print("Please select a valid option")
            
    return option


def getWord(prompt, debug = False):
    if debug: print("getWord Function")
    
    goodInput = False 
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Please don't say that")
       
            
    return word
    
    
def getSport(prompt, debug = False):
    if debug: print("getSport Function")
    
    goodInput = False 
    
    sports = [ "soccer",
               "football",
               "hockey",
               "basketball",
               "baseball",
               "skiing",
               "vollyball"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Please don't say that")
        elif word.lower() not in sports:
            goodInput = False
            print ("Sorry that sport won't work")
       
            
    return word
    
def getAnmial(prompt, debug = False):
    if debug: print("getAnmial Function")
    
    goodInput = False 
    
    anmial = [ "cat",
               "dog",
               "rabbit",
               "pig",
               "horse",
               "donkey",
               "lizard",
               "rat",
               "mouse",
               "bird"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Please don't say that")
        elif word.lower() not in anmial:
            goodInput = False
            print ("Sorry that anmial won't work")
       
            
    return word
    
def getWeekday(prompt, debug = False):
    if debug: print("getWeekday Function")
    
    goodInput = False 
    
    weekday = [ "monday",
               "tuesday",
               "wednesday",
               "thursday",
               "friday",
               "saturday",
               "sunday"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Please don't say that")
        elif word.lower() not in weekday:
            goodInput = False
            print ("Sorry that won't work")
       
            
    return word
    
    
def getRestaurant(prompt, debug = False):
    if debug: print("getRestaurant Function")
    
    goodInput = False 
    
    restaurant = [ "mcdonalds",
               "mcdonald's",
               "subway",
               "wendys",
               "wendy's",
               "chic fil a",
               "dominoes",
               "dominos",
               "pizza hut",
               "dunkins",
               "dunkin donuts",
               "burger king",
               "five guys",
               "five guy's"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Please don't say that")
        elif word.lower() not in restaurant:
            goodInput = False
            print ("Sorry that restaurant won't work")
       
            
    return word
    
def getClass(prompt, debug = False):
    if debug: print("getClass Function")
    
    goodInput = False 
    
    class2 = ["english",
             "math",
             "programing",
             "scoical studies",
             "science",
             "art",
             "band",
             "hell"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Please don't say that")
        elif word.lower() == "programing":
            print ("that is an asome class")
        elif word.lower() == "hell":
            print ("Really?")
        elif word.lower() not in class2:
            goodInput = False
            print ("Sorry that class won't work")
       
            
    return word
    
    
def getConsole(prompt, debug = False):
    if debug: print("getConsole Function")
    
    goodInput = False 
    
    console1 = ["xbox",
             "playstation",
             "pc",
             "computer",
             "play station"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Please don't say that")
        elif word.lower() not in console1:
            goodInput = False
            print ("Sorry that console won't work")
       
            
    return word
    
    
def getDrink(prompt, debug = False):
    if debug: print("getDrink Function")
    
    goodInput = False 
    
    drink1 = ["water",
             "milk",
             "chocolate milk",
             "juice",
             "gatorade"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word, debug):
            goodInput = False
            print ("Please don't say that")
        elif word.lower() not in drink1:
            goodInput = False
            print ("Sorry that drink won't work")
       
            
    return word


def isSwear(word, debug = False):
     if debug: print("isSwear Function")
     if debug: print(word)
     if word.lower() in swearList:
         if debug: print("True")
         return True
     else:
         if debug: print("False")
         return False
    
swearList = [ "poop",
              "pee",
              "fuck",
              "fucker",
              "shit",
              "shitty",
              "crap",
              "motherfucker",
              "crappy",
              "pussy"
]
