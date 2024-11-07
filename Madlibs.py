from Screens import * 
from Getword import * 
from Story1 import * 
from Story2 import *
from Story3 import *
from Story4 import *
from Secretstory import *


def Madlibs (debug = False):
    if debug: print("Welcome to debug")
   
    print (Titlescreen(debug))
    input("Press ENTER to continue")

    done = False

    while not done:
        print(Mainmenu(debug))
        choice = getMenuOption(debug)

        if choice == "q":
            print(Creditscreen(debug))
            exit()

        elif choice == "1":
            print(Story1(debug))
            print("\n")
            input("Press ENTER to continue")

        elif choice == "2":
            print(Story2(debug))
            print("\n") 
            input("Press ENTER to continue")
            
        elif choice == "3":
            print(Story3(debug))
            print("\n")
            input("Press ENTER to continue")
            
        elif choice == "4":
            print(Story4(debug))
            print("\n")
            input("Press ENTER to continue")
            
        elif choice == "happy":
            print(Happyscreen(debug))
            print("\n")
            input("Press ENTER to continue")
            exit()
            
            
        elif choice == "h":
            print(HelpScreen(debug))
            print("\n")
            input("Press ENTER to continue")
            



        else: print("Make a valid input")


Madlibs(False)
