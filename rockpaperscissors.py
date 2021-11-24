import random

decision = ['rock', 'paper', 'scissors']

print("Rock, Paper, Scissors!")
fail = 0
vic = 0

def loop(player,rounds,vic,fail):
    turn(player,rounds,vic,fail)

def win(choice,cpu,rounds,vic,fail):
    print("You WIN! You chose", choice, "and CPU chose", cpu)
    vic+= 1
    print("The current score is:")
    print(player, vic,"points!\nCPU", fail, "points!")
    rounds = rounds - 1
    print("There are ", rounds, " rounds left.")
    turn(player,rounds,vic,fail)

def lose(choice,cpu,rounds,vic,fail):
    print("You LOSE! You chose", choice, "and CPU chose", cpu)
    fail+= 1
    print("The current score is:")
    print(player, vic,"points!\nCPU", fail, "points!")
    rounds = rounds - 1
    print("There are ", rounds, " rounds left.")
    turn(player,rounds,vic,fail)


def turn(player,rounds,vic,fail):
    while rounds >0:
        cpu = random.choice(decision)
        choice = input("Rock, Paper, Scissors! ")
    
        if choice == cpu:
            print("A draw!",player, " and the CPU both chose", cpu)
            print("The current score is:")
            print(player,":", vic, "points!\nCPU:", fail, "points!")
            rounds = rounds-1
            print("There are ", rounds, " rounds left.")
            turn(player,rounds,vic,fail)

        elif choice == "rock":
            if cpu == "paper":
                lose(choice,cpu,rounds,vic,fail)
            else:
                win(choice,cpu,rounds,vic,fail)

        elif choice == "paper":
            if cpu == "rock":
                win(choice,cpu,rounds,vic,fail)
            else:
                lose(choice,cpu,rounds,vic,fail)
    
        elif choice == "scissors":
            if cpu == "rock":
                win(choice,cpu,rounds,vic,fail)
            else:
                lose(choice,cpu,rounds,vic,fail)

        else:
            print("Enter 'rock', 'paper' or 'scissors'! ")
            loop(player,rounds,vic,fail)
  
    print("FINAL POINTS:\n",player,":", vic, "\nCPU:", fail)
    if vic > fail:
        print("THE WINNER IS ",player)
    elif fail > vic:
        print("THE WINNER IS CPU!")
    else:
        print("It's a draw!")
    print("Thanks for playing!")
    exit()

        

player = str(input("ENTER NAME: "))

print("Welcome to Rock, Paper, Scissors,", player,"!")
print("To play this game, you pick one option out of: ")
print("ROCK\nPAPER\nSCISSORS")
print("... you can probably work it out.")

rounds = int(input("How many rounds do you want to play? "))
    
turn(player,rounds,vic,fail)
