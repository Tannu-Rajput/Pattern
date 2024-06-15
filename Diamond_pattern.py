n=int(input("enter the number: "))
for i in range(1,n):
    for k in range(n-1,i,-1):
        print(end="  ")
    for j in range(1,i+1):
       print(j,end=" ")
    for j in range(i,1,-1):
        print(j-1,end=" ")    
    print()
for i in range(n-2,0,-1):
    for k in range(n-1,i,-1):
        print(end="  ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()

#       1 
#     1 2 1 
#   1 2 3 2 1 
# 1 2 3 4 3 2 1 
#   1 2 3 2 1 
#     1 2 1 
#       1 

# ------------------------------------------------------------------------

n=int(input("enter the number: "))
for i in range(1,n):
    for k in range(n-1,i,-1):
        print(end="  ")
    for j in range(1,i+1):
       print("*",end=" ")
    for j in range(i,1,-1):
        print("*",end=" ")    
    print()
for i in range(n-2,0,-1):
    for k in range(n-1,i,-1):
        print(end="  ")
    for j in range(1,i+1):
        print("*",end=" ")
    for j in range(i-1,0,-1):
        print("*",end=" ")
    print()

#       * 
#     * * * 
#   * * * * * 
# * * * * * * * 
#   * * * * * 
#     * * * 
#       * 

# ------------------------------------------------------------------------

for i in range (5,0,-1):
    for j in range (5,i-1,-1):
        print(j,end="  ")
    for j in range(i,1,-1):
        print(i,end="  ")
    for j in range(i,1,-1):
        print(i,end="  ")
    for j in range(i+1,6):
        print(j,end="  ")    
    print()    
for i in range(1,6):
    for j in range(5,i,-1):
        print(j,end="  ")
    for j in range(1,i+1):
        if i==5:
            break
        print(i+1,end="  ")
    for j in range(1,i+1):
        if i==5:
            break
        print(i+1,end="  ")  
    for j in range(i+2,6):
        print(j,end="  ")
        
    print()    

# 5  5  5  5  5  5  5  5  5  
# 5  4  4  4  4  4  4  4  5  
# 5  4  3  3  3  3  3  4  5  
# 5  4  3  2  2  2  3  4  5  
# 5  4  3  2  1  2  3  4  5  
# 5  4  3  2  2  2  3  4  5  
# 5  4  3  3  3  3  3  4  5  
# 5  4  4  4  4  4  4  4  5  
# 5  5  5  5  5  5  5  5  5  


# -------------------------------------------------------------------------------------------

n=int(input("enter the number: "))
for i in range (n,0,-1):
    for j in range (n,i-1,-1):
        print(j,end="  ")
    for j in range(i,1,-1):
        print(i,end="  ")
    for j in range(i,1,-1):
        print(i,end="  ")
    for j in range(i+1,n+1):
        print(j,end="  ")    
    print()    
for i in range(1,n):
    for j in range(n,i,-1):
        print(j,end="  ")
    for j in range(1,i+1):
        if i==n:
            break
        print(i+1,end="  ")
    for j in range(1,i+1):
        if i==n:
            break
        print(i+1,end="  ")  
    for j in range(i+2,n+1):
        print(j,end="  ")    
    print()  
# 9  9  9  9  9  9  9  9  9  9  9  9  9  9  9  9  9  
# 9  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  9  
# 9  8  7  7  7  7  7  7  7  7  7  7  7  7  7  8  9  
# 9  8  7  6  6  6  6  6  6  6  6  6  6  6  7  8  9  
# 9  8  7  6  5  5  5  5  5  5  5  5  5  6  7  8  9  
# 9  8  7  6  5  4  4  4  4  4  4  4  5  6  7  8  9  
# 9  8  7  6  5  4  3  3  3  3  3  4  5  6  7  8  9  
# 9  8  7  6  5  4  3  2  2  2  3  4  5  6  7  8  9  
# 9  8  7  6  5  4  3  2  1  2  3  4  5  6  7  8  9  
# 9  8  7  6  5  4  3  2  2  2  3  4  5  6  7  8  9  
# 9  8  7  6  5  4  3  3  3  3  3  4  5  6  7  8  9  
# 9  8  7  6  5  4  4  4  4  4  4  4  5  6  7  8  9  
# 9  8  7  6  5  5  5  5  5  5  5  5  5  6  7  8  9  
# 9  8  7  6  6  6  6  6  6  6  6  6  6  6  7  8  9  
# 9  8  7  7  7  7  7  7  7  7  7  7  7  7  7  8  9  
# 9  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  9  
# 9  9  9  9  9  9  9  9  9  9  9  9  9  9  9  9  9  