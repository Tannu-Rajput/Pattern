for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="   ")
    print()  
# 1
# 1   2
# 1   2   3
# 1   2   3   4
# 1   2   3   4   5

# -----------------------------------------

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="   ")
    print()    

# 1   
# 2   2   
# 3   3   3   
# 4   4   4   4   
# 5   5   5   5   5   
# -----------------------------------------

for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end="   ")
    print()   

# 5   
# 5   4   
# 5   4   3   
# 5   4   3   2   
# 5   4   3   2   1

# -----------------------------------------

for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(i,end="   ")
    print()    

# 5   
# 4   4   
# 3   3   3   
# 2   2   2   2   
# 1   1   1   1   1  

# -----------------------------------------

for i in range(1,6):
    for j in range(i,(i*2)):
        print(j,end="   ")
    print()
# 1   
# 2   3   
# 3   4   5   
# 4   5   6   7   
# 5   6   7   8   9  

# -----------------------------------------

for i in range(1,6):
    for j in range((i*2)-1,i-1,-1):
        print(j,end="   ")
    print()    

# 1   
# 3   2   
# 5   4   3   
# 7   6   5   4   
# 9   8   7   6   5   

# -----------------------------------------

n=1
for i in range(1,6):
    for j in range(1,i+1):
        print(n,end="   ")
        n+=1
    print()    

# 1   
# 2     3   
# 4     5     6   
# 7     8     9    10   
# 11   12   13   14   15   

# -----------------------------------------

n=1
for i in range(1,6):
    for j in range(1,i+1):
        if(n%2==0):
           print("0",end="   ")
           n+=1
        else: 
            print("1",end="   ")
            n+=1
    print() 

# 1   
# 0   1   
# 0   1   0   
# 1   0   1   0   
# 1   0   1   0   1   

# -----------------------------------------



