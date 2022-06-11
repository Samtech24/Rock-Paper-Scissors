# import random module
import random

 # Game rules
print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")

# Game requirements
while True:
    print("Enter choice \n R for Rock, \n P for paper, and \n S for scissor \n")
     
    # take the input from user
    choice = (input("User turn: "))     
    while choice:    
        if choice == 'R' or choice == 'r':
            choice_name = 'rock'
            break
        elif choice == 'P' or choice == 'p':
            choice_name = 'paper'
            break
        elif choice == 'S' or choice == 's':
            choice_name = 'scissors'
            break
        else:
             choice = (input("Please enter valid input: ")) 
             
         
    # user choice
    print("user choice is: " + choice_name)
    print("\nNow its computer turn.......")
    
    # computer choice
    comp_choice = random.randint(1, 3)
     
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
 
    if comp_choice == 1:
        comp_choice_name = 'rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissors'

    # game choices and result     
    print("Computer choice is: " + comp_choice_name)
 
    print(choice_name + " V/s " + comp_choice_name)

    if((choice == 'R' and comp_choice == 2) or
      (choice == 'P' and comp_choice ==1 )):
        print("paper wins => ", end = "")
        result = "paper"
         
    elif((choice == 'R' and comp_choice == 3) or
        (choice == 'S' and comp_choice == 1)):
        print("Rock wins => \n", end = "")
        result = "rock"
        
    elif((choice == 'P' and comp_choice == 3) or
        (choice == 'S' and comp_choice == 2)):
        print("Scissors wins => \n", end = "")
        result = "scissors"
        
    else:
        print(" Tie => \n", end = "")
        result = "Tie" 
        
 
    if result == choice_name:
        print("\n<== User wins ==>")
    elif result == "Tie":
        print("\n<== It is a tie ==>")
    else:
        print("\n<== Computer wins ==>")
         
    print("\nPress N to end or any other key to play again")
    ans = input()
 
    if ans == 'n' or ans == 'N':
        break
     
print("\nThanks for playing")