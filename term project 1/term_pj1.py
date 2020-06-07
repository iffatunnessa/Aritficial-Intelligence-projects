def position(ti,tj):
    if(ti == 1 and tj == 1):
        posi = 0
    elif(ti == 2 and tj == 1):
        posi = 1
    elif(ti == 3 and tj == 1):
        posi = 2
    elif(ti == 4 and tj == 1):
        posi = 3
    elif(ti == 1 and tj == 2):
        posi = 4
    elif(ti == 2 and tj == 2):
        posi = 5
    elif(ti == 3 and tj == 2):
        posi = 6
    elif(ti == 4 and tj == 2):
        posi = 7
    elif(ti == 1 and tj == 3):
        posi = 8
    elif(ti == 2 and tj == 3):
        posi = 9
    elif(ti == 3 and tj == 3):
        posi = 10
    elif(ti == 4 and tj == 3):
        posi = 11
    elif(ti == 1 and tj == 4):
        posi = 12
    elif(ti == 2 and tj == 4):
        posi = 13
    elif(ti == 3 and tj == 4):
        posi = 14
    elif(ti == 4 and tj == 4):
        posi = 15
    return posi

board = [('Start','1','1'),('smell','2','1'),('clear','3','1'),('smell','4','1'),
         ('smell','1','2'),('monster','2','2'),('smell & glitter','3','2'),('clear','4','2'),
         ('clear','1','3'),('smell & glitter','2','3'),('gold','3','3'),('glitter','4','3'),
        ('smell','1','4'),('monster','2','4'),('smell & glitter','3','4'),('clear','4','4')]

i,j=1,1
ti,tj=1,1
pos=0
visited=[]

name= str(input("Enter your name: "))
print(name,", your moves are limited into 12 moves.\nThe agent is at (",i,j,":",pos,")")

k=12
while(k>0):
    print("Moves are left: ",--k)
    move = str(input("You can move[up,down,left,right].What's your move:"))
    if(move == 'up'):
        ti = i
        tj = tj+1
        if(tj>4):
            print("Can't go more up")
            tj = tj-1
            pos=position(ti,tj)
            continue
        pos=position(ti,tj)

    elif(move == 'down'):
        ti = i
        tj = tj-1
        if(tj<1):
            print("Can't go more down")
            tj = tj+1
            pos=position(ti,tj)
            continue
        pos=position(ti,tj)
        
    elif(move == 'right'):
        ti = ti+1
        tj = j
        if(ti>4):
            print("Can't go more right")
            ti = ti-1
            pos=position(ti,tj)
            continue
        pos=position(ti,tj)

    elif(move == 'left'):
        ti = ti-1
        tj = j
        if(ti<1):
            print("Can't go more left")
            ti = ti+1
            pos=position(ti,tj)
            continue
        pos=position(ti,tj)

    else:
        print("No moves.")

    
    if(board[pos][0] == 'smell'):
        i,j=ti,tj
        visited.append(pos)
        print("Monster is near!")
        print("Agent is at (",i,j,":",pos,")")
        
    elif(board[pos][0] == 'smell & glitter'):
        i,j=ti,tj
        visited.append(pos)
        print("Gold is gittering also Monster is near!")
        print("Agent is at (",i,j,":",pos,")")
        
    elif(board[pos][0] == 'clear'):
        i,j=ti,tj
        visited.append(pos)
        print("nothing is there!")
        print("Agent is at (",i,j,":",pos,")")

    elif(board[pos][0] == 'monster'):
        i,j=ti,tj
        visited.append(pos)
        score = -5
        print("You are killed by the monster!")
        print("Agent is at (",i,j,":",pos,")")
        break
    
    elif(board[pos][0] == 'glitter'):
        i,j=ti,tj
        visited.append(pos)
        print("Gold is gittering,it's near!")
        print("Agent is at (",i,j,":",pos,")")
    
    elif(board[pos][0] == 'gold'):
        i,j=ti,tj
        visited.append(pos)
        print("You find the Gold!!")
        score = 10
        print("Agent is at (",i,j,":",pos,")")
        break

    k-=1

f1=open('score.txt', "a+")
print("\n")
for i in range(1):
        visit=str(visited)
        std=name+"\t"+visit+"\t"+str(score)
        print(std, end="\n", file=f1)
        print("\n")
f1.close

f1=open('score.txt', "r")       
for l in f1:
        name, visited, score =l.split("\t")
        print(name, visited, float(score), end="\n")
f1.close




