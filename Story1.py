from Getword import *

def Story1(debug = False):
    if debug: print("Story1 Function")
    
    print("\n")
    friendName1 = getWord("Enter a name: ", debug)
    sport1 = getSport("Enter a Sport: ", debug)
   
    out = "\n"
    out += "One day my friend, " + friendName1 + ", and I"
    out += " were out playing " + sport1
    
    return out
