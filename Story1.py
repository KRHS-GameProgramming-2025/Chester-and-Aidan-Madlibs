from Getword import *

def Story1(debug = False):
    if debug: print("Story1 Function")
    
    print("\n")
    friendName1 = getWord("Enter a Name: ", debug)
    sport1 = getSport("Enter a Sport: ", debug)
    anmial1 = getAnmial("Enter a Anmial: ", debug)
    verb1 = getWored("Enter a Verb: ", debug)
   
    out = "\n"
    out += "One day my friend, " + friendName1 + ", and I"
    out += " were out playing " + sport1
    out += " and we saw someone walking an " + anmial1
    out += " it came over to us and " + verb1
    
    return out
