threshold = 0
max_val = 0
restart_count = 0
states = []
max_id = 0

def clear_database():
    global threshold 
    global max_val 
    global restart_count 
    global  states 
    global  max_id 
    
    threshold = 0
    max_val = 0
    restart_count = 0
    states = []
    max_id = 0

def execute_hcls():
    global threshold 
    global  states 
    
    state = input('enter a state: ')
    threshold = int(input('enter threshold value: '))
    L = list(state)
    genarate_successor(L)

def display_states():
    global states
    for j in range(len(states)):
       print(states[j])

def save_states():
    global states
    f1=open("std.py", "w")
    for j in range(len(states)):
       print(states[j],file = f1)
    f1.close

def eval(qList):
    count = 0
    #horizontal check
    for i in range(0,len(qList),1):
        for j in range(i+1,len(qList),1):
            if (qList[i] == qList[j]):
                count = count + 1

    #diagonal_up check
    for i in range(0,len(qList),1):
        x = int(qList[i])
        for j in range(i+1,len(qList),1):
           
            x = x + 1
            if (x == int(qList[j])):
                count = count + 1

    #diagonal_down check
    for i in range(0,len(qList),1):
        x = int(qList[i])
        for j in range(i+1,len(qList),1):
            x = x - 1
            if (x == int(qList[j])):
                count = count + 1

    return 28 - count

def genarate_successor(L):
    global threshold 
    global max_val 
    global restart_count 
    global  states 
    global  max_id 
    
    idcount=0
    i=1
    while i<9:
        better = False
        max_val = eval(L)
        hval= 0
        temp = L[i-1]
        for j in range(1,9):
            if(L[i-1] != str(j)):
                x=L[:]
                x[i-1] = str(j)
                hval = eval(x)
                idcount += 1
            # print("x:",x)
                y = [idcount,'s',x,hval]
                states.append(y)
                if(max_val < hval):
                    stuck = False
                    better = True
                    i=0                        
                    idcount += 1
                    break
        if not better:
            L[i-1]= temp
            i+=1 
    checkall(stuck,hval)
        
def checkall(stuck,hval):
    global threshold 
    global max_val 
    global restart_count 
    global  states 
    global  max_id
    
    if max_val >= threshold:
        print('found '+str(states[max_id - 1]))
    elif stuck == True:
        print('Stuckup!\n ')
    elif max_val < threshold :
        if(max_val < hval):
            print('New: '+str(states[max_id - 1]))
            genarate_successor(states[max_id - 1][2])

    
#Main
cs = 1

while(cs>=1 and cs<5):
    print('1. Clear database')
    print('2. Execute hcls')
    print('3. Display states')
    print('4. Save states')
    print('5. Exit')
    cs = int(input('\n\nEnter your choice: '))
    if(cs == 1):
        clear_database()
    elif(cs == 2):
        execute_hcls()
    elif(cs == 3):
        display_states()
    elif(cs == 4):
        save_states()
    else:
        break


