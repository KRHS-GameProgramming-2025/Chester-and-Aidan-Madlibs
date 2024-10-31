from Getword import *

def Story2(debug = False):
    if debug: print("Story2 Function")
    
    print("\n")
    print("----------------------------------------------------Story 2-------------------------------------------------------------")
    print("\n")
    weekday = getWeekday("Enter a day of the week: ", debug)
    verb = getWord("Enter a verb ending in ing: ", debug)
    color1 = getWord("Enter a color: ", debug)
    animal1 = getAnmial("Enter an animal: ", debug)
    animal2 = getWord("Enter the plural version of the animal: ", debug)
    game1 = getWord("Enter a video game: ", debug)
    game2 = getWord("Enter a different video game: ", debug)
    restaurant = getRestaurant("Enter a fast food restuarant: ", debug)
    
    out = "\n"
    out += "One " + weekday + ", I was "
    out += verb + " in a field. Then I suddenly saw a " + color1 + " alien " + verb + " with me!"
    out += " After that I went home and saw the alien again. It transformed into a " + animal1 + "."
    out += " It saw me playing " + game1 + ", and wanted to play too. I love " + animal2 + ", so I let him play. "
    out += "The alien wanted to play " + game2 + " instead, so we did. "
    out += "After a while, we got hungry and got food at " + restaurant + ". "
    out += "When we returned, the " + animal1 + " and I had a fun rest of the night"
    out += "That was a good " + weekday + "."
        
    return out

