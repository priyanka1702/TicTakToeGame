import random
def game():
    board=[0,1,2,3,4,5,6,7,8]
    wincomb=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    win=False
    def show():
        print(board[0],'|', board[1],'|', board[2])
        print("---------")
        print(board[3],'|', board[4],'|', board[5])
        print("---------")
        print(board[6],'|', board[7],'|', board[8])
        print()
    
    def computerselect():
        while True:
            random.seed()
            compselect=random.randint(0,8)
            if board[compselect] != "X" and board[compselect] !="O":
                board[compselect]="O"
                break                                
            else:
                tie=checktie()
                if tie==True:
                    break
                
	
    def userselect():
        print("choose a number")
        userinput=int(input())
        if board[userinput] == "X":
            print("you have already taken, try again")
        elif board[userinput] =="O":
            print("computer has chosen, try again")
        else:
            board[userinput]="X"
            computerselect()
        

    def checkwining():
        for a in wincomb:
                    if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                        print("----------You Win!----------\n")
                        print("-------Congratulations!--------\n")
                        return True

                    if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                        print("--------computer Wins!--------\n")
                        return True

    def checktie():
        count=0
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                return True
    
           
    while not win:
        show()
        userselect() 
        win=checkwining()
        if win==True:
                show()
                break
        tie=checktie()
        if tie==True:
            print("----------The game ends in a TIE----------")
            show()
            break
    if input("Play again (y/n)\n") == "y":
        game()
        
game()        
        
        
        
