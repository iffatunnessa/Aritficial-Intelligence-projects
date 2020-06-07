grid=[('Agent','1','1'),('Nothing','2','1'),('Nothing','3','1'),
            ('Smell', '1','2'),('Nothing','2','2'),('Glitter','3','2'),
            ('Monstar','1','3'),('Smell&Gitter','2','3'),('Gold','3','3')]

flag=[0,0,0,0,0,0,0,0,0]
current_i = 1
current_j = 1
temp_i=1
temp_j=1
pos=0
visited=[]

def find_position (num1,num2):
    if(num1==2 and num2==1):
        position=1
    elif(num1==3 and num2==1):
        position=2
    elif(num1==1 and num2==2):
        position=3
    elif(num1==2 and num2==2):
        position=4
    elif(num1==3 and num2==2):
        position=5
    elif(num1==1 and num2==3):
        position=6
    elif(num1==2 and num2==3):
        position=7
    elif(num1==3 and num2==3):
        position=8
    return  position

print('The agrnt is in grid(',current_i,current_j,')\n', end='')
i=0
while(i<=8):
    
    move=str(input("Give yor move(right,left,up,down):"))

    if(move=='right'): 
       temp_i=temp_i+1
       temp_j=current_j
       if(temp_j>3):
         print('Out of limit\n', end='')
         continue
       pos=find_position (temp_i,temp_j)

    elif(move=='left'): 
       temp_i=temp_i-1
       temp_j=current_j
       if(temp_i<1):
         print('Out of limit\n', end='')
         continue
       pos=find_position (temp_i,temp_j)

    elif(move=='up'): 
       temp_i=current_i
       temp_j=temp_j+1
       if(temp_j>3):
         print('Out of limit\n', end='')
         continue
       pos=find_position (temp_i,temp_j)

    elif(move=='down'):
       temp_i=current_i
       temp_j=temp_j-1
       if(temp_j<1):
         print('Out of limit\n', end='')
         continue
       pos=find_position (temp_i,temp_j)

    else:
       print('Not an exceptable move.\n', end='') 

       
    if(grid[pos][0]=='Nothing' and flag[pos]==0):
        current_i = temp_i
        current_j = temp_j
        visited.append(move)
        flag[pos]=1
        print('The agrnt is in grid(',current_i,current_j,')\n', end='')
        print('No gold or monster here...\n', end='')

    elif((grid[pos][0]=='Smell') and (flag[pos]==0)):
        current_i = temp_i
        current_j = temp_j
        visited.append(move)
        flag[pos]=1
        
        print('The agrnt is in grid(',current_i,current_j,')\n', end='')
        print('No gold but monster is near!!! Be carefull....\n', end='')

    elif(grid[pos][0]=='Glitter' and flag[pos]==0):
        current_i = temp_i
        current_j = temp_j
        visited.append(move)
        flag[pos]=1
        print('The agrnt is in grid(',current_i,current_j,')\n', end='')
        print('Gold is almost there. Its glittering....\n', end='')

    elif(grid[pos][0]=='Smell&Gitter' and flag[pos]==0):
        current_i = temp_i
        current_j = temp_j
        visited.append(move)
        flag[pos]=1
        print('The agrnt is in grid(',current_i,current_j,')\n', end='')
        print('Gold is almost there!!! But monster is also near!!!\n', end='')

    elif((grid[pos][0]=='Monstar') and flag[pos]==0):
        current_i = temp_i
        current_j = temp_j
        visited.append(move)
        flag[pos]=1
        print('The agrnt is in grid(',current_i,current_j,')\n', end='')
        print('Awwwwwh NO.... You are finished....\n', end='')
        print('Directions:',visited)
        break

    elif(grid[pos][0]=='Gold'and flag[pos]==0):
        current_i = temp_i
        current_j = temp_j
        visited.append(move)
        flag[pos]=1
        print('The agrnt is in grid(',current_i,current_j,')\n', end='')
        print('Hurrayh... Found the gold....\n', end='')
        print('Directions:',visited)
        break
    else:
       print('Its Visited already. cant go back\n', end='')
       print('The agrnt is still in grid(',current_i,current_j,')\n', end='')
    i=i+1
    print('Directions:',visited)

    
       


