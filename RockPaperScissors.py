from random import randint
while(True):
    t = ["Rock", "Paper", "Scissors"]
    computer=t[randint(0,2)].lower()
    print("Choice The Option:{}".format(t))
    player=False
    while player==False:
        player=input("write:")
        if player.lower()==computer:
            print("Tie")
        elif player=="rock":
            if computer=="paper":
                print("Computer is winner")
            else:
                print("You Are winner")
        elif player=="scissors":
            if computer=="rock":
                print("Computer is winner")
            else:
                print("You Are winner")
        elif player=="paper":
            if computer=="Scissors":
                print("Computer is winner")
            else:
                print("You Are winner")
        else:
            print("You Write the Wrong Spell: ")
            print("So please Write  rigth Spell ")
    print("Are You Want To play again:[Yes/No]")
    recive=input().lower()
    if recive=="no":
        break
    elif recive!="yes":
        print("Please enter valid option..")
        break
                