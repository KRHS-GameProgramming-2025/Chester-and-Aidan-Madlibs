from Getword import *

def Story4(debug = False):
    if debug: print("Story4 Function")
    
    print("\n")
    print("----------------------------------------------------Story 4-------------------------------------------------------------")
    print("\n")
    animal1 = getAnmial("Enter an animal: ", debug)
    animal2 = getAnmial("Enter a different animal: ", debug)
    verb1 = getWord("Enter a verb: ", debug)
    sport1 = getSport("Enter a sport: ", debug)
    console1 = getConsole("Enter a gaming console: ", debug)
    friend1 = getWord("Enter a name: ", debug)
    drink1 = getDrink("Enter a drink: ", debug)
    
    out = "\n"
    out += "I was walking my " + animal1 + ", when I saw someone walking a(n) " + animal2 + "."
    out += " The " + animal2 + " growled at my " + animal1 + "."
    out += " The two animals then started to " + verb1 + "."
    out += " I took both of them to go play " + sport1 + "."
    out += " My " + animal1 + " won against the " + animal2 + "."
    out += " My " + animal1 + " watches me playing on the " + console1 + "."
    out += " I have a friend named " + friend1 + " who my " + animal1 + " likes to play with."
    out += " The 3 of us like to drink " + drink1 + "."
    out += " One day the " + animal2 + " returned and wanted to play " + sport1 + " again."
    out += " This time the " + animal2 + " won."
    out += " They were having so much fun, my friend " + friend1 + " and I joined in."
    out += " " + friend1 + " loves to play " + sport1 + "."
        
    return out
