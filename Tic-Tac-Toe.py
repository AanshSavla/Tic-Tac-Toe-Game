import sys
import os
import random
game=[" "," "," "," "," "," "," "," "," "]

print("The tic-tac-toe grid is:")
print("1 |2 |3 ")
print("__|__|__")
print("4 |5 |6 ")
print("__|__|__")
print("7 |8 |9 ")
print("__|__|__")


def begin():
    count=0
    n=2
    print("Press 1:Player1='x' and Player2='o'\n 2:Player1:'o' and Player2='x'")
    tr=int(input())
    if(tr==1):
        player1="x"
        player2="o"
    elif(tr==2):
        player1="o"
        player2="x"
    else:
        print("Invalid Option")
        begin()
    while(True):
        print("Player 1's turn")
        player(player1,"player",count)
        n=check_result(player1,player2)
        count=count+1
        if(count==9):
            print_game()
            print("Match Tied")
            break
        if(n==1):
            sys.exit()
        print("Player 2's turn")
        player(player2,"comp",count)
        n=check_result(player1,player2)
        count=count+1
        if(n==1):
            sys.exit()
        


def player(p,pl,count):
    if(count!=9):
        p3=p
        if(p=="o"):
            p2="x"
        elif(p=="x"):
            p2="o"
        
        if(pl=="player"):
            print("Select an empty space from 1-9")
            t=int(input())
            if(game[t-1]==" "):
                game[t-1]=p
                print_game()
            else:
                print("Space already occupied")
                player(p,pl,count)
        elif(pl=="comp"):
            
            flag=computer_player(p,p3)
          
            n=check_result(p2,p)
            print("n1=",n)
            if(n==1): 
                print_game()
                
            else:
                flag=computer_player(p,p2)
                      
                n=check_result(p2,p)
                
                if(n==1):
                    print_game()
                    
                else:
                    if(flag==2):
                        print_game()
                    elif(flag==1):
                        t=random.randint(0,8)
                        if(game[t-1]==" "):
                            
                            game[t-1]=p
                            print_game()
                        else:
                            print("Space already occupied")
                            player(p,pl,count)
        
                


def computer_player(pl,p):
    
    flag=1        
    for i in range(9):
        if(game[i]==" "):
            if(i==0 and ((game[1]==game[2]and  game[1]==p)or(game[4]==game[8]and  game[4]==p)or(game[3]==game[6]and game[3]==p))):
                game[i]=pl
                flag=2
            elif(i==1 and ((game[0]==game[2]and  game[0]==p)or(game[4]==game[7]and  game[4]==p))):
                game[i]=pl
                flag=2
            elif(i==2 and ((game[4]==game[6] and  game[4]==p)or(game[5]==game[8]and  game[5]==p))):
                game[i]=pl
                flag=2
            elif(i==3 and ((game[0]==game[6]and  game[0]==p)or(game[4]==game[5] and  game[4]==p))):
                game[i]=pl
                flag=2
            elif(i==4 and ((game[1]==game[7]and  game[1]==p)or(game[2]==game[6]and  game[2]==p)or(game[3]==game[5]and  game[3]==p))):
                game[i]=pl
                flag=2
            elif(i==5 and ((game[8]==game[2]and  game[8]==p)or(game[4]==game[3] and  game[4]==p))):
                game[i]=pl
                flag=2
            elif(i==6 and ((game[0]==game[3]and  game[0]==p)or(game[4]==game[2] and game[4]==p)or(game[7]==game[8] and game[7]==p))):
                game[i]=pl
                flag=2
            elif(i==7 and ((game[1]==game[4]and game[1]==p)or(game[6]==game[8]and game[6]==p))):
                game[i]=pl
                flag=2
            elif(i==8 and ((game[0]==game[4]and game[0]==p)or(game[5]==game[2] and game[5]==p)or(game[7]==game[6] and game[7]==p))):
                game[i]=pl
                flag=2
        if(flag==2):
            break
    return flag
    

    
    

               
                    
    
def print_game():
    print(game[0]+" |"+game[1]+" |"+game[2])
    print("__|__|__")
    print(game[3]+" |"+game[4]+" |"+game[5])
    print("__|__|__")
    print(game[6]+" |"+game[7]+" |"+game[8])
    
def check_result(p1,p2):
    value=2
    for i in range(8):
        if(game[i]==" "):
            game[i]=6
    solution1=list(set((game[0],game[1],game[2])))
    solution2=list(set((game[0],game[4],game[8])))
    solution3=list(set((game[0],game[3],game[6])))
    solution4=list(set((game[1],game[4],game[7])))
    solution5=list(set((game[2],game[4],game[6])))
    solution6=list(set((game[2],game[5],game[8])))
    solution7=list(set((game[3],game[4],game[5])))
    solution8=list(set((game[6],game[7],game[8])))
    result=[solution1,solution2,solution3,solution4,solution5,solution6,solution7,solution8]
    for i in range(8):
        if(len(result[i])==1 and result[i][0]!=6):
           
            if(result[i][0]==p1):
                print("Player1 Wins")
                value=1
            elif(result[i][0]==p2):
                print("Player 2 Wins")
                value=1
    for i in range(8):
        if(game[i]==6):
            game[i]=" "
    return value
            
begin()