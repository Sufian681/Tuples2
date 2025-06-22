tup1 = (5,12,7,-2,10,20,11,15,-27,19,30,2,14)
tup2 = (3,8,-6,5,14,18,9,13,-21,17,25,20,-12)

tup = ()

for i in range(0,len(tup1)):
    a=tup1[i]*tup2[i]
    tup=tup* (a,)
    
    
print(f"The multiplication of the two tuples is: {tup}")    