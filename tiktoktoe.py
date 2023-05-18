#    1   2   3      4   5   6   7   8   9    
a=[[" "," "," "],[" "," "," "],[" "," "," "]]
#   0,0 0,1 0,2    1,1  1,2 1,3  2,1  2,2 2,3
player1='x'
player2='o'
used=[]
while(1):
    print("enter the plyer 1 choice 1:")
    x,y=map(int,input().split())
    if a[x][y]==' ':
        a[x][y]=player1
        break
    else:
        print('enter valid choice')
for i in a:
    print(i)
while(2):
    print("enter the plyer 2 choice 1:")
    m,n=map(int,input().split())
    if a[m][n]==' ':
        a[m][n]=player2
        break
    else:
        print('enter valid choice')
for i in a:
    print(i)
while(3):
    print("enter the plyer 1 choice 2:")
    x,y=map(int,input().split())
    if a[x][y]==' ':
        a[x][y]=player1
        break
    else:
        print('enter valid choice')
for i in a:
    print(i)
while(4):
    print("enter the plyer 2 choice 2:")
    m,n=map(int,input().split())
    if a[m][n]==' ':
        a[m][n]=player2
        break
    else:
        print('enter valid choice')
for i in a:
    print(i)
while(5):
    print("enter the plyer 1 choice 3:")
    x,y=map(int,input().split())
    if a[x][y]==' ':
        a[x][y]=player1
        break
    else:
        print('enter valid choice')
for i in a:
    print(i)
if (a[0][0]==a[0][1] and a[0][1]==a[0][2] and a[0][0]==player1) or (a[1][0]==a[1][1] and a[1][1]==a[1][2] and a[1][0]==player1) or (a[2][0]==a[2][1] and a[2][1]==a[2][2] and a[2][0]==player1) or (a[0][0]==a[1][1] and a[1][1]==a[2][2] and a[0][0]==player1) or (a[2][0]==a[1][1] and a[1][1]==a[0][2] and a[2][0]==player1) or (a[0][0]==a[1][0] and a[1][0]==a[2][0] and a[2][0]==player1) or (a[0][1]==a[1][1] and a[1][1]==a[2][1] and a[2][1]==player1) or (a[0][2]==a[1][2] and a[1][2]==a[2][2] and a[2][2]==player1):
    print("player 1 won")
else:
    while(6):
        print("enter the player 2 choice 3:")
        x,y=map(int,input().split())
        if a[x][y]==' ':
            a[x][y]=player2
            break
        else:
            print('enter valid choice')
    for i in a:
        print(i)
    if (a[0][0]==a[0][1] and a[0][1]==a[0][2] and a[0][0]==player2) or (a[1][0]==a[1][1] and a[1][1]==a[1][2] and a[1][0]==player2) or (a[2][0]==a[2][1] and a[2][1]==a[2][2] and a[2][0]==player2) or (a[0][0]==a[1][1] and a[1][1]==a[2][2] and a[0][0]==player2) or (a[2][0]==a[1][1] and a[1][1]==a[0][2] and a[2][0]==player2) or (a[0][0]==a[1][0] and a[1][0]==a[2][0] and a[2][0]==player2) or (a[0][1]==a[1][1] and a[1][1]==a[2][1] and a[2][1]==player2) or (a[0][2]==a[1][2] and a[1][2]==a[2][2] and a[2][2]==player2):
        print("player 2 won")
    else:
        while(7):
            print("enter the plyer 1 choice 4:")
            x,y=map(int,input().split())
            if a[x][y]==' ':
                a[x][y]=player1
                break
            else:
                print('enter valid choice')
        for i in a:
            print(i)
        if (a[0][0]==a[0][1] and a[0][1]==a[0][2] and a[0][0]==player1) or (a[1][0]==a[1][1] and a[1][1]==a[1][2] and a[1][0]==player1) or (a[2][0]==a[2][1] and a[2][1]==a[2][2] and a[2][0]==player1) or (a[0][0]==a[1][1] and a[1][1]==a[2][2] and a[0][0]==player1) or (a[2][0]==a[1][1] and a[1][1]==a[0][2] and a[2][0]==player1) or (a[0][0]==a[1][0] and a[1][0]==a[2][0] and a[2][0]==player1) or (a[0][1]==a[1][1] and a[1][1]==a[2][1] and a[2][1]==player1) or (a[0][2]==a[1][2] and a[1][2]==a[2][2] and a[2][2]==player1):
            print("player 1 won")
        else:
            while(8):
                print("enter the player 2 choice 4:")
                x,y=map(int,input().split())
                if a[x][y]==' ':
                    a[x][y]=player2
                    break
                else:
                    print('enter valid choice')
            for i in a:
                print(i)
            if (a[0][0]==a[0][1] and a[0][1]==a[0][2] and a[0][0]==player2) or (a[1][0]==a[1][1] and a[1][1]==a[1][2] and a[1][0]==player2) or (a[2][0]==a[2][1] and a[2][1]==a[2][2] and a[2][0]==player2) or (a[0][0]==a[1][1] and a[1][1]==a[2][2] and a[0][0]==player2) or (a[2][0]==a[1][1] and a[1][1]==a[0][2] and a[2][0]==player2) or (a[0][0]==a[1][0] and a[1][0]==a[2][0] and a[2][0]==player2) or (a[0][1]==a[1][1] and a[1][1]==a[2][1] and a[2][1]==player2) or (a[0][2]==a[1][2] and a[1][2]==a[2][2] and a[2][2]==player2):
                print("player 2 won")
            else:
                while(7):
                    print("enter the plyer 1 choice 5:")
                    x,y=map(int,input().split())
                    if a[x][y]==' ':
                        a[x][y]=player1
                        break
                    else:
                        print('enter valid choice')
                for i in a:
                    print(i)
                if (a[0][0]==a[0][1] and a[0][1]==a[0][2] and a[0][0]==player1) or (a[1][0]==a[1][1] and a[1][1]==a[1][2] and a[1][0]==player1) or (a[2][0]==a[2][1] and a[2][1]==a[2][2] and a[2][0]==player1) or (a[0][0]==a[1][1] and a[1][1]==a[2][2] and a[0][0]==player1) or (a[2][0]==a[1][1] and a[1][1]==a[0][2] and a[2][0]==player1) or (a[0][0]==a[1][0] and a[1][0]==a[2][0] and a[2][0]==player1) or (a[0][1]==a[1][1] and a[1][1]==a[2][1] and a[2][1]==player1) or (a[0][2]==a[1][2] and a[1][2]==a[2][2] and a[2][2]==player1):
                    print("player 1 won")
                elif(a[0][0]==a[0][1] and a[0][1]==a[0][2] and a[0][0]==player2) or (a[1][0]==a[1][1] and a[1][1]==a[1][2] and a[1][0]==player2) or (a[2][0]==a[2][1] and a[2][1]==a[2][2] and a[2][0]==player2) or (a[0][0]==a[1][1] and a[1][1]==a[2][2] and a[0][0]==player2) or (a[2][0]==a[1][1] and a[1][1]==a[0][2] and a[2][0]==player2) or (a[0][0]==a[1][0] and a[1][0]==a[2][0] and a[2][0]==player2) or (a[0][1]==a[1][1] and a[1][1]==a[2][1] and a[2][1]==player2) or (a[0][2]==a[1][2] and a[1][2]==a[2][2] and a[2][2]==player2):
                    print("player 2 won")
                else:
                    print("draw")