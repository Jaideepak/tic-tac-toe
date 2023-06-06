#list
board=['-','-','-','-','-','-','-','-','-']
#display board
def dis():
    print("|"+board[0]+"|"+board[1]+"|"+board[2]+"|")
    print("|"+board[3]+"|"+board[4]+"|"+board[5]+"|")
    print("|"+board[6]+"|"+board[7]+"|"+board[8]+"|")

#checking win 
def check(board):
    p1='x'
    p2='o'
    # all rows or column or diagnols have same element then it is true
    if board[0]==board[1]==board[2]==p1 or board[0]==board[1]==board[2]==p2:
     return True
    elif board[3]==board[4]==board[5]==p1 or board[3]==board[4]==board[5]==p2:
     return True
    elif board[6]==board[7]==board[8]==p1 or board[6]==board[7]==board[8]==p2:
     return True
    
    elif board[0]==board[3]==board[6]==p1 or board[0]==board[3]==board[6]==p2:
     return True
    elif board[1]==board[4]==board[7]==p1 or board[1]==board[4]==board[7]==p2:
     return True
    elif board[2]==board[5]==board[8]==p1 or board[2]==board[5]==board[8]==p2:
     return True
    
    elif board[0]==board[4]==board[8]==p1 or board[0]==board[4]==board[8]==p2:
     return True
    elif board[2]==board[4]==board[6]==p1 or board[2]==board[4]==board[6]==p2:
     return True
    else:
      return False
#returning position and error at value already exists
def inp(board):
 while True:
   try:
    x= int(input("enter position:"))
   except ValueError:
    print("please enter correct value")
    continue
   else:
    break
    
 if board[x-1]!='-':
    print("value already exist please enter new value")
    return inp(board)
 elif x==0:
    print("error")
    return inp(board)  
 else:     
    return x
  
  
player1=input("player name 1:")
player2=input("player name 2:")
dis()
#if i=0 x=0
#
for i in range(9):
  if i%2==0:
    x=inp(board)
    board[x-1]='x'
    dis()
    if check(board):
      print("player 1 wins")
      break
  else:
    x=inp(board)
    board[x-1]='o'
    dis()
    if check(board):
      print("player 2 wins")
      break

print('over')
