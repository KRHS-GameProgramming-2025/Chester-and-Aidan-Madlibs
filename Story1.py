from Getword import *

def Story1(debug = False):
    if debug: print("Story1 Function")
    
    print("\n")
    friendName1 = getWord("Enter a Name: ", debug)
    sport1 = getSport("Enter a Sport: ", debug)
    anmial1 = getAnmial("Enter a Anmial: ", debug)
    verb1 = getWord("Enter a Verb ending in 'ed': ", debug)
    pronoun1 = getWord("Enter a Pronoun: ", debug)
    color1 = getWord("Enter a Color: ", debug)
    bakedGood1 = getWord("Enter a Baked Good: ", debug)
    pronoun2 = getWord("Enter another version of Pronoun: ", debug)
   
    out = "\n"
    out += "One day my friend, " + friendName1 + ", and I"
    out += " were out playing " + sport1
    out += " and we saw someone walking a " + anmial1
    out += " it came over to us and " + verb1 + " us "
    out += friendName1 + " was scared of the " + anmial1 + " so " + pronoun1
    out += " went to the " + color1 + " house down the street"
    out += " I went after " + pronoun2 + " to be a friend, but when I got there " + pronoun1 + " was eating a " + bakedGood1 
    out += " I asked where " + pronoun1 + " got the " + bakedGood1 + " "
    out += pronoun1 + " explained that this was a good friend and the " + anmial1 + " was hers, after that we both started laughing, for " + pronoun1 +  " was scared for nothing" 
    
    return out
