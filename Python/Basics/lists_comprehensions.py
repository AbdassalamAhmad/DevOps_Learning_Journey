x=1
y=1
z=2
n=2

list1 = []

for i in range (0,x+1):
    for j in range(0,y+1):
        for k in range (0,z+1):
            #if not (i+j+k ==n):
            list1.append([i,j,k])

newlist = [b for b in list1 if b[0]+b[1]+b[2] != n]
#print (list1)
print ("new: " + str(newlist))