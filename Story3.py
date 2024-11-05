from Getword import *

def Story3(debug = False):
    if debug: print("Story3 Function")
    
    print("\n")
    print("----------------------------------------------------Story 3-------------------------------------------------------------")
    print("\n")
    class1=getClass("Enter a Class: ", debug)
    color1=getWord("Enter a Color: ", debug)
    sport1=getSport("Enter a Sport: ", debug)
    food1=getWord("Enter a Food Item: ", debug)
    book1=getWord ("Enter a Book: ", debug)
    game1=getWord("Enetr a Video Game: ", debug)
    money1=getWord("Enter a Money Amount: ", debug)
    name1=getWord("Enter a Name: ", debug)
    
    out="\n"
    out += "I was going to my favorite class " + class1
    out += " when a small " + color1 + " thing apeared before me. "
    out += "He said that he waned to play with me, but i said that I have " + class1 + " to go to. "
    out += "He furrowed his brow and said 'I WANT TO PLAY " + sport1 + "'" 
    out += " as he yelled we were teleported to the park, I sighed and areeded to play with him only if he would bring me back to " + class1 
    out += " he was very happy so we started playing and then the little thing said 'lets get food I want " + food1 + "'"
    out += " as I was also getting hungary I agreed. After we got food the little guy said 'theres a book shop I want " + book1 + "'" 
    out += " I also wanted to see if the book shop had that book so we went in. After getting the book the little guy said 'I see a game shop i wnat to get " + game1 + "'"
    out += " I said 'I don't have any money left though', the little guy pondered for a second and then pulled out " + money1 + " dollars from his pocket."
    out += " After seeing that he had money, we went in and got the game."
    out += " After all the shopping that the little guy wanted was over he said 'thank you for such fun time, also my name is " + name1 + "'"
    out += " and then I was transproted back to school only to realise that I had missed class." 
    
    return out 
