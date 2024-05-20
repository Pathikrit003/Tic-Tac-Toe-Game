import random

def board():
 print("\t 0 | 1 | 2 ")
 print("\t---|---|---")
 print("\t 3 | 4 | 5 ")
 print("\t---|---|---")
 print("\t 6 | 7 | 8 ")

def singleplayer_pts_table(player_pt,computer_pt):
 print("\t  Points Table")
 print("\t  ------------")
 print(f"     You       |     Computer     ")
 print(f"---------------|------------------")
 print(f"               |                  ")
 print(f"      {player_pt}        |         {computer_pt}            ")
 print(f"               |                  ")
 print()
 
 


def multiplayer_pts_table(player1_pt,player2_pt):
 print("\t       Points Table")
 print("\t       ------------")
 print(f"     Player 1       |      Player 2      ")
 print(f"--------------------|--------------------")
 print(f"                    |                    ")
 print(f"         {player1_pt}          |         {player2_pt}            ")
 print(f"                    |                  ")
 print()
 

def print_board(xState,zState):
 zero  = 'X' if xState[0] else ( 'O' if zState[0] else " ")
 one   = 'X' if xState[1] else ( 'O' if zState[1] else " ")
 two   = 'X' if xState[2] else ( 'O' if zState[2] else " ")
 three = 'X' if xState[3] else ( 'O' if zState[3] else " ")
 four  = 'X' if xState[4] else ( 'O' if zState[4] else " ")
 five  = 'X' if xState[5] else ( 'O' if zState[5] else " ")
 six   = 'X' if xState[6] else ( 'O' if zState[6] else " ")
 seven = 'X' if xState[7] else ( 'O' if zState[7] else " ")
 eight = 'X' if xState[8] else ( 'O' if zState[8] else " ")


 print(f"\t {zero} | {one} | {two} ")
 print(f"\t---|---|---")
 print(f"\t {three} | {four} | {five} ")
 print(f"\t---|---|---")
 print(f"\t {six} | {seven} | {eight} ")

def checkWin(xState,zState):
 wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
 for win in wins:
  if xState[win[0]]+xState[win[1]]+xState[win[2]]==3:
   return 1
  elif zState[win[0]]+zState[win[1]]+zState[win[2]]==3:
   return 0
  
 return -1
  
def computer_turn(xState,zState):
 empty_boxes=[]
 for i in range(9):
  if xState[i]==0 and zState[i]==0:
   empty_boxes.append(i)
 if empty_boxes:
  value=random.choice(empty_boxes)
  zState[value]=1
  return value
 else:
  return -1

print()
print("---Welcome to Tic Tac Toe---")
print()

player_pt=0
computer_pt=0
player1_pt=0
player2_pt=0


while True:
  
 f=0
 choice=int(input("Single-player(1) or Multiplayer(2): "))
 print()
 xState=[0,0,0,0,0,0,0,0,0]
 zState=[0,0,0,0,0,0,0,0,0]
 
 if choice == 1:
  print("    --Single-player mode--")
  print()
  board()
  print()
  turn=int(input("Choose between X(1) or O(0): "))
  print()

 elif choice == 2:
  print("    --Multiplayer mode--")
  print()
  board()
  print()
  turn=1
  
 else:
  print("\tInvalid Input!")
  print()
  f=1
 moves = 0
 while(choice == 1 and f != 1): 
  

  if turn == 1:
   print("\tYour Turn:-")
   print()
   value = int(input("Enter a value: "))
   print()
   if value <= 8 and ( xState[value]==0 and zState[value]==0):
    xState[value]=1
    moves = moves + 1
   else:
    print("Invalid Input!")
    print()
  else :
   print("\tComputer's Turn:-")
   print()
   value=computer_turn(xState,zState)
   if value!=-1:
    moves = moves + 1
  print_board(xState,zState)
  print()
  
  cwin=checkWin(xState,zState)
  if cwin != -1:

   if cwin==1:
    print("\tMatch Over!")
    print()
    print("      You won the match!")
    player_pt=player_pt+1
   else:
    print("\tMatch Over!")
    print()
    print("      Computer won the match!") 
    computer_pt=computer_pt+1
   print()
   break
  if moves==9:

   print("\tMatch Over")
   print()
   print("\tIt's a draw!")
   print()
   player_pt=player_pt+0.5
   computer_pt=computer_pt+0.5
   break
 
  if value <= 8:
   turn = 1-turn

 while(choice == 2 and f != 1):
 

  if turn == 1:
   print("\tX's Turn:-")
   print()
   value = int(input("Enter a value: "))
   print()
   if value <= 8 and ( xState[value]==0 and zState[value]==0):
    xState[value]=1
    moves = moves + 1
   else:
    print("Invalid Input!")
    print()
  else :
   print("\tO's Turn:-")
   print()
   value = int(input("Enter a value: "))
   print()
   if value <= 8 and ( xState[value]==0 and zState[value]==0):
    zState[value]=1
    moves = moves + 1
   else:
    print("Invalid Input!")
    print()

  print_board(xState,zState)
  print()
  cwin=checkWin(xState,zState)
  if cwin != -1:

   if cwin==1:
    print("\tMatch Over!")
    print()
    print("      X won the match!")
    player1_pt=player1_pt+1
   else:
    print("\tMatch Over!")
    print()
    print("      O won the match!") 
    player2_pt=player2_pt+1
   print()
   break
  if moves==9:

   print("\tMatch Over")
   print("\tIt's a draw!")
   player1_pt=player1_pt+0.5
   player2_pt=player2_pt+0.5
   break
 
  if value <= 8:
   turn = 1-turn

 if (f!=1):
  if choice==1:
    singleplayer_pts_table(player_pt,computer_pt)
  elif choice==2:
    multiplayer_pts_table(player1_pt,player2_pt)

 
 if(f!=1):
  ch=input("Do you want to play again? Y/N : ")
  print()
  if ch.upper()=='Y':
   print("\t--New Game--")
   print()
   continue
  else:
   print("\tGame Closed!")
   print()
   break