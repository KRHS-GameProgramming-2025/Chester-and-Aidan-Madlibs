from Getword import *

def Story2(debug = False):
    if debug: print("Story1 Function")
    
    print("\n")
    weekday = getWord("Enter a day of the week: ", debug)
   
    out = "\n"
    out += "One " + weekday + ", "
    
    return out

