# print("----------------Rock Paper Scissors -------------------")

import random
i=1
Player_A_Win_Count=0
Player_B_Win_Count=0
while i<=5:
    Game_condition=['1','2','3']
    print("Enter 1 for Scissor,Enter 2 for Paper,Enter 3 for Rock")
    print("-------------------------------------")
    Player_A=input("Enter 1 for Scissor,2 for Paper,3 for Rock")
    Player_B=random.choice(Game_condition)
    print("Player_A dO",Player_A)
    print("Player_B do",Player_B)
    
    if Player_A =='1' and Player_B == '2':
        print("Scissor_beat_paper\n Player A Win ")
        Player_A_Win_Count+=1
    elif Player_A =='1' and Player_B == '3':
        print("Rock_Beats_Scissor \n Player B Win ")
        Player_B_Win_Count+=1
    elif Player_A =='2' and Player_B == '1':
        print("Scissor_beat_paper\n Player B Win ")
        Player_B_Win_Count+=1
    elif Player_A =='2' and Player_B == '3':
        print("Paper_Beats_rock \n Player A Win ")
        Player_A_Win_Count+=1
    elif Player_A =='3' and Player_B == '2':
        print("Paper_beat_Rock \n Player B Win ")
        Player_B_Win_Count += 1
    elif Player_A =='3' and Player_B == '1':
        print("Rock_Beats_Scissor \n Player A Win ")
        Player_A_Win_Count += 1
    elif Player_A not in Game_condition:
        print("You Entered Wrong")
    else:
        print("you both do match, Draw ,Paly Again")
    i+=1

print(f"Player A Score { Player_A_Win_Count} Player B Score { Player_B_Win_Count}")
if Player_A_Win_Count > Player_B_Win_Count:
    print("Congratulation! Player A is Winner")
elif Player_A_Win_Count == Player_B_Win_Count:
    print("You both gain same score!")
else:
    print("Congratulation! Player B is Winner")

--------------------------------------------
#Second Code

### import random
i=1
Player_A_Win_Count=0
Player_B_Win_Count=0
while i<=5:
    Game_condition=['1','2','3']
    print("Enter 1 for Scissor,Enter 2 for Paper,Enter 3 for Rock")
    print("-------------------------------------")
    Player_A=input("Enter 1 for Scissor,2 for Paper,3 for Rock")
    Player_B=random.choice(Game_condition)
    P_A=int(Player_A)
    P_B=int(Player_B)
    print("Player_A dO",Player_A)
    print("Player_B do",Player_B)
    if P_A == P_B:
        print("Draw/Both Do same")
    elif ((P_B-P_A)% 3)==1:
        print("Player A is Winner")
        Player_A_Win_Count+=1
    elif Player_A not in Game_condition:
        print("You Entered Wrong")
    else:
        print("Player B is Winner")
        Player_B_Win_Count+=1
    i+=1
print(f"Player A Score { Player_A_Win_Count} Player B Score { Player_B_Win_Count}")
if Player_A_Win_Count > Player_B_Win_Count:
    print("Congratulation! Player A is Winner")
elif Player_A_Win_Count == Player_B_Win_Count:
    print("You both gain same score!")
else:
    print("Congratulation! Player B is Winner")
 
