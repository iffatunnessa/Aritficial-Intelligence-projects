threshold = 0
goal=[]
state =[]
iteration=0
def clear_database():
    global threshold 
    global  state 
    global iteration
    
    threshold = 0
    state = []
    iteration = 0

def execute_firstchoice_hc():
    global threshold 
    global  state
    global iteration
    
    s = input('Enter a state: ')
    threshold = int(input('Enter threshold value: '))
    state=list(s)
    print(state)
    firstchoice(state)
    
def display_states():
    global state
    print(state)
       
def save_states():
    global state
    f1=open("std.py", "w")
    print(state,file = f1)
    f1.close
    
def evaluate_nonattacking(s):
    count = 0
    for i in range(0,len(s),1):
        for j in range(i+1,len(s),1):
            if (s[i] == s[j]):
                count = count + 1

    for i in range(0,len(s),1):
        x = int(s[i])
        for j in range(i+1,len(s),1):
           
            x = x + 1
            if (x == int(s[j])):
                count = count + 1
                
    for i in range(0,len(s),1):
        x = int(s[i])
        for j in range(i+1,len(s),1):
            x = x - 1
            if (x == int(s[j])):
                count = count + 1
                
    #print(count)       
    return 28 - count

def firstchoice(state):
    global iteration
    i=0
    while i<8:
        temp = state[i]
        hval = 0
        current_hval = evaluate_nonattacking(state)
        better = False
        for j in range(1,9):
            if(state[i] == str(j)):
                continue
            state[i]=str(j)
            iteration+=1;
            hval=evaluate_nonattacking(state)
            if(hval == threshold):
                goal.append((iteration, state,hval))
                return
            if(hval>current_hval):
                iteration +=1
                i=0
                print('selected uphill move :',str(iteration)+str(state)+str(hval))
                better = True 
                break
        if not better:
            state[i] = temp
            i+=1
    if better == True:
        print("Goal:"+str(goal[0][0])+ 'state:'+str( goal[0][1])+ 'val:'+str(goal[0][2]))
        print()
    else: print("Stuck")

#Main
count = 1

while(count>=1 and count<5):
    print('1. Clear database')
    print('2. Execute hcls')
    print('3. Display states')
    print('4. Save states')
    print('5. Exit')
    cs = int(input('\n\nEnter your choice: '))
    if(cs == 1):
        clear_database()
    elif(cs == 2):
        execute_firstchoice_hc()
        #firstchoice(state)
    elif(cs == 3):
        display_states()
    elif(cs == 4):
        save_states()
    else:
        break
