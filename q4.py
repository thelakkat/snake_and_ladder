import random
import operator

def mover(start_pos):
  current_pos=start_pos
  snake=0
  die_role=random.randint(1,6)
  print(die_role)
  current_pos=current_pos + die_role
  if current_pos in [3,5,15,18,21,12,14,17,31,35]:
    print ("snake/ladder")
    if  current_pos in [12,14,17,31,35]:
      snake=1
    current_pos=sl[current_pos]
  return current_pos,snake

def maingame(start2):
  j=1
  position=[1,start2]
  print(position)
  move_num=0
  snake_flag=0
  while j<100:
    i=0
    winner=0
    while i < 2:
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
  return winner,j,snake_flag
 
#calling the functions and printing results 
num_sim=10000#int(input("enter number of simulations "))
l=1
e=[0]*36
f=[0]*36
g=[0]*36
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
while l<=36:
    k=0
    b=[0]*num_sim
    c=[0]*num_sim
    s=[0]*num_sim 
    while k<num_sim:
      [b[k],c[k],s[k]]=maingame(l)
      k=k+1
    e[l-1]=float(b.count(1))
    f[l-1]=float(b.count(2))
    g[l-1]=float(sum(s))
    l=l+1
#print(s)
diff_wins= list(map(abs, list(map(operator.sub, e,f))))
print(diff_wins)
best_start=diff_wins.index(min(diff_wins))+1
print("Start position for the second player for the most fair game play is %d and probability of winning for the second player starting there is %f" %((best_start), f[best_start-1]/(e[best_start-1]+f[best_start-1])))
