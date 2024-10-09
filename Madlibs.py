from Screens import * 
from Getword import * 
from Story1 import * 

def Madlibs (debug = False):
    if debug: print("Welcome to debug")
    print (Titlescreen(debug))
    input("Press ENTER to continue")
    
    done = False
    
    while not done:
      print( Mainmenu(debug))
      choice = getMenuOption(debug)
      
      if choice == "q":
          exit()
          
      elif choice == "1":
         print(Story1())
         print("\n")
         input("Press ENTER to continue")

	elif choice == "2":
         print(Story2())
         print("\n")
         input("Press ENTER to continue")


Madlibs(False)
