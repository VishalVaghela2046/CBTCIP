import random

print("Welcome to Rock, Paper, Scissor Game")

user_score = 0
comp_score = 0
ties = 0

print("""
Winning Rules
1.Rock vs Paper >> Paper win
2.Rock vs Scissor >> Rock win
3.Paper vs Scissor >> Paper win
""")

print("""
Choose any one :
1.Rock 
2.Paper
3.Scissor
""")

while True:

    choice = int(input("Enter your choice : "))

    while choice>3 or choice<1:
        choice = int(input('enter valid input'))

    if choice == 1 :
        user_choice = "Rock"
    elif choice == 2:
        user_choice = "Paper"
    else:
        user_choice = "scissor"

    print("User's choice is : ",user_choice)

    com = random.randint(1,3)

    if com == 1 :
        comp_choice = "Rock"
    elif com == 2:
        comp_choice = "Paper"
    else:
        comp_choice = "scissor"

    print("Computer's choice is : ",comp_choice)

    if (user_choice == "Paper" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Paper"):
        print("Paper wins")
        result = "Paper"

    elif user_choice == comp_choice:
         print("it is a tie")
         result = "Tie"

    elif (user_choice == "Scissor" and comp_choice == "Rock") or (user_choice == "Scissor" and comp_choice == "Paper"):
        print("Rock wins")
        result = "Rock"

    else:
        print("Scissor win")
        result = "Scissor"

    if result == "Tie":
        ties +=1
    elif result == user_choice:

        print("User Win")
        user_score +=1
    else:
        print("Computer Win")
        comp_score +=1


    print("user's score is >> ",user_score)
    print("computer's score is >> ",comp_score)
    print("ties are>>",ties)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break