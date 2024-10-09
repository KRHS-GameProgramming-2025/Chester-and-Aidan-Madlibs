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
def isSwear(word, debug = False):
     if debug: print("isSwear Function")
     if word.lower() in swearList:
         return True
     else:
         return False
    
swearList = [ "poop",
              "pee"
]
