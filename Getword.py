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
               "hockey"]
    
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
               "lizard"]
    
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
               "subway",
               "chic fil a",
               "dominoes",
               "dominos",
               "pizza hut",
               "dunkins",
               "dunkin donuts",
               "burger king"]
    
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
              "shit",
              "crap",
              "motherfucker"
]
