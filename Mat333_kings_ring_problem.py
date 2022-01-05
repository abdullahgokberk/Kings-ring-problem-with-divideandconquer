import random
def divide(rings):
    #Divide
    if len(rings)>1:
        mid= len(rings) // 2
        left=rings[:mid]
        right=rings[mid:]
        divide(left)
        divide(right)
        conquer(rings, left, right)
def conquer(rings,left,right):
    #conquer
    a=0
    b=0
    c=0
    while a<len(left) and b<len(right):
        if left[a]<right[b]:
            rings[c]=left[a]
            a=a+1
        else:
            rings[c]=right[b]
            b=b+1
        c=c+1
    while a<len(left):
        rings[c]=left[a]
        a=a+1
        c=c+1
    while b<len(right):
        rings[c]=right[b]
        b=b+1
        c=c+1    
        
# array initialization
rings = [];
for x in range(10000):
    rings.append(10)
i=random.randint(1,10000);
rings[i]=11;
divide(rings)
print(rings)















        
