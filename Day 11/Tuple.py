#Tuple
'''
tempVal = 12,'Hi','welcome',23.5
tempVal = (12,'Hi','welcome',23.5)
print (tempVal)
print (type(tempVal))

print (tempVal[0])

print (tempVal[:-2])

print (tempVal[-2:])
'''
#Tuple with list
tupleVal = ("a","b","mplig","z","example123",1,2,2.5,[12,13,45])
#print (tupleVal,type(tupleVal[-1]))

#'''
#tupleVal1 = 10,23,46,"welcome"
intCntr,strCntr,lCntr = 0,0,0
for eachItem in tupleVal:
    
    print (type(eachItem))
    if type(eachItem)== int:
        intCntr +=1
    elif type(eachItem) == str:
        strCntr +=1
    elif type(eachItem) == list:
        lCntr +=1

print (intCntr)
print (strCntr)
print (lCntr)
#'''
