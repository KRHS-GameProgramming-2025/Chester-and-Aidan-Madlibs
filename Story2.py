from Getword import *

def Story2(debug = False):
    if debug: print("Story2 Function")
    
    print("\n")
    weekday = getWord("Enter a day of the week: ", debug)
    verb = getWord("Enter a verb ending in ing: ", debug)
    
   
    out = "\n"
    out += "One " + weekday + ", I was "
    out += verb
    
    return out

