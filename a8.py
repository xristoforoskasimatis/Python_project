import random
ari8moi=[]
for k in range(30):
    number=random.randint(-30,30)
    ari8moi.append(number)
a = 0
for x in range(30):
    for y in range(x+1,30):
        for z in range(y+1,30):
            if ari8moi[x]+ari8moi[y]+ari8moi[z]==0:
                print(ari8moi[x],ari8moi[y],ari8moi[z])
                a+=1
if a==0 :
    print('den iparxei')
ari8moi.sort
print "oi ari8moi tis listas apo to mikrotero pros to megalitero einai : ",ari8moi
