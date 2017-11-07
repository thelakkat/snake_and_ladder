import random

def mover(start_pos,player,s_count):
  current_pos=start_pos
  die_role=random.randint(1,6)
  print(die_role)
  current_pos=current_pos + die_role
  if current_pos in [3,5,15,18,21,12,14,17,31,35]:
    print ("snake/ladder")
    if (current_pos in [12,14,17,31,35] and player==2 and s_count==0):
        s_count=s_count+1
    else:
        if (current_pos in [12,14,17,31,35] and player==2):
            s_count=s_count+1
        current_pos=sl[current_pos]
  return current_pos, s_count

def maingame(np,s_count):
  j=1
  position=[1]*np
  print(position)
  move_num=0
  while j<100:
    i=0
    winner=0
    while i < np:
      [position[i],s_count]=mover(position[i],i+1,s_count)
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
  return winner,j,s_count
 
#calling the functions and printing results 
np=2#int(input("Enter number of players:"))
num_sim=10000#int(input("enter number of simulations "))
k=0
b=[0]*num_sim
c=[0]*num_sim
s=[0]*num_sim
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
    s_count=0
    [b[k],c[k],s[k]]=maingame(np,s_count)
    k=k+1
e=float(b.count(1))
f=float(b.count(2))
g=float(sum(s))
print("Summary is number of players = %d and probability of the first player winning is %f and probability of the second player winning is (while getting immunity from 1st snake) %f and average number of snakes encountered by 2 is %f" %(np,e/(e+f),f/(e+f),g/(e+f)))
