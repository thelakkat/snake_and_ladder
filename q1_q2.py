import random

def mover(start_pos): # function to roll die and move the players
  current_pos=start_pos #using the start position to move along
  snake=0 # counting number of snakes in current roll
  die_role=random.randint(1,6) #rolling die
  print(die_role)
  current_pos=current_pos + die_role #intital move of player
  if current_pos in [3,5,15,18,21,12,14,17,31,35]:
      print ("snake/ladder")
      if  current_pos in [12,14,17,31,35]: #counting snakes
          snake=1 
      current_pos=sl[current_pos] # if position is snake or ladder, reassigning to new place
  return current_pos,snake

def maingame(np):
  j=1
  position=[1]*np
  print(position)
  move_num=0
  snake_flag=0
  while j<100: # limited number to ensure every game ends- possibility of grid lock 
    i=0
    winner=0 #player number who is the winner
    while i < np:
      temp=0
      [position[i],temp]=mover(position[i])
      snake_flag=snake_flag+temp
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
  return winner,j+1,snake_flag
 
#calling the functions and printing results 
np=2#int(input("Enter number of players:"))
num_sim=10000 #int(input("enter number of simulations "))
k=0
b=[0]*num_sim #winner's name i.e. player 1/2
c=[0]*num_sim #number of roles of die when 
s=[0]*num_sim # number of snakes landed in each game
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
  [b[k],c[k],s[k]]=maingame(np)
  k=k+1
e=float(b.count(1)) # #of times 1 won
f=float(b.count(2)) # #of times 2 won
g=float(sum(s))

print("Summary is number of players = %d and probability of the first player winning is %f and probability of the second player winning is %f and average number of snakes/game is %f" %(np,e/(e+f),f/(e+f),g/(e+f)))