import game
games=[]

# game.add_Games(games)
# game.display_Games(games)
while True: 
    choice = input("Choose from the menue: " + "\n"+ "1. Add Game" + "\n" + "2. Display Games" + "\n" + "3. Exit" + "\n" )
    if(choice=="1" or choice=="Add Game"):
        game.add_Games(games)
    elif(choice=="2" or choice=="Display Games"):
        game.display_Games(games)
    elif(choice=="3" or choice=="Exit"):
        break
    else:
        print("Invalid Choice")

