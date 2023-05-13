import random

ans=str(input("Do You want to roll the Dice(Y/N) ?"))

while (ans=="Y" or ans=="y"):
    num=random.randint(1,6)
    if(num==1):
        print("[---]")
        print("[   ]")
        print("[ 0 ]")
        print("[---]")
        ans=0
        ans=str(input("Do You want to roll the Dice(Y/N) ?"))
    elif(num==2):
        print("[---]")
        print("[0  ]")
        print("[   ]")
        print("[  0]")
        print("[---]")
        ans=0
        ans=str(input("Do You want to roll the Dice(Y/N) ?"))
    elif(num==3):
        print("[---]")
        print("[0  ]")
        print("[ 0 ]")
        print("[  0]")
        print("[---]")
        ans=0
        ans=str(input("Do You want to roll the Dice(Y/N) ?"))
    elif(num==4):
        print("[---]")
        print("[0 0]")
        print("[   ]")
        print("[0 0]")
        print("[---]")
        ans=0
        ans=str(input("Do You want to roll the Dice(Y/N) ?"))
    elif(num==5):
        print("[---]")
        print("[0 0]")
        print("[ 0 ]")
        print("[0 0]")
        print("[---]")
        ans=0
        ans=str(input("Do You want to roll the Dice(Y/N) ?"))
    elif(num==6):
        print("[---]")
        print("[0 0]")
        print("[0 0]")
        print("[0 0]")
        print("[---]")
        ans=0
        ans=str(input("Do You want to roll the Dice(Y/N) ?"))

while (ans=="N" or ans=="n"):
    print("Thanks for playing")

