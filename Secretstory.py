from Getword import *

def Secretstory(debug = False):
    if debug: print ("Secretstory Function")
    
    print("\n")
    print("----------------------------------------------------Secret Story--------------------------------------------------------")
    print("\n")
    print("Pick the things YOU would do")
    print("\n")
    
    
    color1=getWord("enter a color: ", debug)
    animal1=getAnimal("enter a animal: ", debug)
    sport1=getSport("enter a sport: ", debug)
    drink1 = getDrink("enter a drink: ", debug)
    bakedGood1 = getWord("enter a baked good: ", debug)
    weekday = getWeekday("enter a day of the week: ", debug)
    restaurant = getRestaurant("enter a fast food restuarant: ", debug)
    class1=getClass("enter a class: ", debug)
    friendName1 = getWord("enter a name: ", debug)
    verb = getWord("enter a verb ending in ing: ", debug)
    pronoun1 = getWord("enter a pronoun: ", debug)
    game1 = getWord("enter a video game: ", debug)
    console1 = getConsole("enter a gaming console: ", debug)
    game2 = getWord("enter a different video game: ", debug)
    pronoun2 = getWord("enter another version of pronoun: ", debug)
    money1=getWord("enter a money amount: ", debug)
    book1=getWord ("enter a book: ", debug)
    food1=getWord("enter a food item: ", debug)
    animal2 = getWord("enter the plural version of the animal: ", debug)
    
    
    out = "\n"
    out += "One day you were walking around the local park, when you saw a " + color1 + " " + animal1 + "."
    out += "You decide to let the " + animal1 +" into your arms, hugging me- er the "+ animal1 + " tightly." 
    out += "While walking you see people playing " + sport1 + " I don't like " + sport1 + "."
    out += "No matter, after a while you get " + drink1 + "and" + bakedGood1
    out += ", seeing how it was " + weekday + "," + restaurant + " was open, so we went there." 
    out += "After, you told the " + animal1 + " that you needed to head to " + class1 + " to meet your friend " + friendName1 + "."
    out += "I grummbled, but the " + animal1 + " agreed so we started " + verb + " to " + pronoun1 + "."
    out += "When you and your new friend arrived " + friendName1 + " was playing " + game1 + " on a " + console1 + "."
    out += "You then sat me down and started playing " + game2 + "."
    out += "Suddenly your friend disapered into a red cloud and in " + pronoun2 + " place was " + money1 + "$."
    out += " Your friend jumped up and said 'Now we can go to the book store and get " + book1 + "!' you said no and and was wondering where " + friendName1 + " was."
    out += " After some convining I was able to gte you to go to the book store and to get some " + food1 + " and when you and your friend was headed to get the food you saw other " + animal2 + "."
    out += " You went ot pet one of them but they also disapered into a red cloud."
    out += " Suddnly you where back at your house and everything seemed fine"
    out += " but the problem was that I wasnt inside with you, you kicked me out, how mean :( \n"
    out +=  friendName1 + " and the " + animal2 + " got in the way, I had to get rid of them, don't be mad friend.\n"
    out += " But if you are angry let me in, so you can join them :)\n"
    out += " Hit ENTER to join them ;)\n"
    out += " it's one little button :)\n"
    
    
    return out
