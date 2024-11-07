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
    
    
    out = "\n"
    out += "One day you were walking around the local park, when you saw a " + color1 + " " + animal1 + "."
    out += "You decide to let the " + animal1 +" into your arms, hugging me- er the "+ animal1 + " tightly." 
    out += "While walking you see people playing " + sport1 + " I don't like " + sport1 + "."
    out += "No matter, after a while you get " + drink1 + "and" + bakedGood1
    out += ", seeing how it was " + weekday + "," + restaurant + " was open, so we went there." 
 
    
    






#friendName1 = getWord("Enter a Name: ", debug)
#    pronoun1 = getWord("Enter a Pronoun: ", debug)
   
#  pronoun2 = getWord("Enter another version of Pronoun: ", debug)
 
#  verb = getWord("Enter a verb ending in ing: ", debug)
#    animal2 = getWord("Enter the plural version of the animal: ", debug)
#    game1 = getWord("Enter a video game: ", debug)
#    game2 = getWord("Enter a different video game: ", debug)
   
#    class1=getClass("Enter a Class: ", debug)
#    food1=getWord("Enter a Food Item: ", debug)
#    book1=getWord ("Enter a Book: ", debug)
#    money1=getWord("Enter a Money Amount: ", debug)
#    console1 = getConsole("Enter a gaming console: ", debug)
  
   
    
