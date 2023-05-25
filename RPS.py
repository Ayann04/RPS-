import random
print()
print("---------------WELCOME TO ROCK PAPER SCISSORS----------------  -")
   
user_score =0
comp_score=0
ties=0

name=input('Enter your name here')

print("""
winning rules::
1.Paper vs Rock --> Paper
2.Rock vs Scissors --> Rock
3.Scissors vs Paper --> Scissors""")

print()


while True:
    print("""Choices are
    1.Rock
    2.Paper
    3.Scissors""")
          
    print()
    #user choice input
    choice=int(input("enter your choice from 1-3:"))
    print()

    #running loop if user enters wrong number:
    while choice > 3 or choice <1:
        choice=int(input("enter valid input"))
        
    #userchoice
    if choice==1:
        user_choice = 'Rock'        
    elif choice ==2:        
        user_choice = 'Paper'        
    else:
        user_choice = 'Scissors'
    print("The user's choice is",user_choice)
    print("Now its computer turn")

    
    #computerchoice
    computer =random.randint(1,3)
    if computer==1:
        comp_choice='Rock'    
    elif computer==2:
        comp_choice='Paper'    
    else:
        comp_choice='Scissors'
    print("computer choice is",comp_choice)

    #comparison::
    if (user_choice == 'Paper' and comp_choice == 'Rock') or  (user_choice == 'Rock' and comp_choice=='Paper'):
        print(" Paper Wins ")
        result=" Paper "

    elif (user_choice == 'Scissors' and comp_choice == 'Rock') or  (user_choice == 'Rock' and comp_choice=='Scissors'):
        print(" Rock Wins ")
        result= " Rock "
        
    elif user_choice == comp_choice:
        print("its a tie")
        result = "Tie"

    else:
        print( "Scissors wins ")
        result = "Scissors"
        
    if result == "Tie":
        ties+=1
        
    elif result == user_choice:
        user_score+=1
        print(" USER WINS ")
        
    else:
        print(" COMPUTER WINS " )
        comp_score+=1

    print("score are")
    print(name,"'s score is ",user_score)
    print("computer 's score is",comp_score)
    print("ties are",ties)

    #press yes if u want to play again
    repeat = input('do you want to play again? Yes/No ')
    if repeat == "No" or repeat == "no":
        break

print()    
print("---------------!!!GAME OVER!!!--------------- ")
print("---------------!!!THANKS FOR PLAYING CHEERS!!!--------------- ")
 
    





































    
            
      
