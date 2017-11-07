import random

def mover(start_pos):
  current_pos=start_pos
  die_role=random.randint(1,6)
  print(die_role)
  current_pos=current_pos + die_role
  multiplier=random.randint(0,1) # if 1 then the ladder will be used
  if current_pos in [12,14,17,31,35] or (current_pos in [3,5,15,18,21] and multiplier==1):
    print ("snake/ladder")
    current_pos=sl[current_pos]
  return current_pos

def maingame(np):
  j=1
  position=[1]*np
  print(position)
  move_num=0
  while j<100:
    i=0
    winner=0
    while i < np:
      position[i]=mover(position[i])
      if position[i]>=36:
        winner=i+1
        print("the winner is %d" % winner)
        break
      i=i+1
    move_num=move_num+1
    print(position,move_num)
    if winner!=0:
      break
    j=j+1
  return winner,j
 
#calling the functions and printing results 
np=2#int(input("Enter number of players:"))
num_sim=10000#int(input("enter number of simulations "))
k=0
b=[0]*num_sim
c=[0]*num_sim #number of turns to win
#snake and ladder list
sl=[1]*36
#ladder assignments
sl[3]=16
sl[5]=7
sl[15]=25
sl[18]=20
sl[21]=32
# snake assignments
sl[12]=2
sl[14]=11
sl[17]=4
sl[31]=19
sl[35]=22 
while k<num_sim:
  [b[k],c[k]]=maingame(np)
  k=k+1
e=float(b.count(1))
f=float(b.count(2))
g=float(sum(c))
print("Summary is number of players = %d and average number of rolls needed to complete the game if only 50 percent of the time the players take a snake/ladder is %f" %(np,g/(e+f)))
