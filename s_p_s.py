def game(player1="player 1",player2="player 2"):
    c1=0
    c2=0
    while True:
        print("enter choices acoording \n 1. stone \n 2. paper \n 3.scissor:")
        
        try:
            p1=int(input(f"enter choice({player1}) : "))
            p2=int(input(f"enter choice({player2}): "))
    
            if(p1>p2 or (p1==1 and p2==3)):
                    print(f"----------{player1} is won the match----------")
                    c1=c1+1   
            else:
                    print(f"---------{player2} is won the match----------")
                    c2=c2+1
            choice=int(input("do you to continue the game : "))
            if(choice==0):
                    print(f"total point of player 1 is : {c1} \n total point of player 2 is : {c2} ")
                    return False
        except:
              print("---->>>>>ERROR : YOU ENTER WRONG CHOICE ENTER BETWEEN 1 TO 3")



player1=input("player 1  name : ")
player2=input("player 2 name : ")
game(player1,player2)