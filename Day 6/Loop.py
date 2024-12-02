'''
val = int(input("Enter upto what number you need square"))

print (val)

for var in range(1,val): #Loop
    #print ("Square of value:",var, 'is',var*var)
    print ("Square of value:%d is %d"%(var,var*var))

    
for var in range(1,val,2):#Step option

loop example:
'''
startChNum=int(input("Enter the number:"))
stopChNum=int(input("Enter the number:"))

if startChNum < stopChNum:
    for chNum in range(startChNum,stopChNum):
        
        print ("Channel Number is:" + str(chNum))
        if chNum %7 ==0:
            print("Number belongs to A channel")
        elif chNum %2 ==0:
            print("Number belongs to Zee channel")
        else:
            print("Number belongs to Sony channel")

else:
    print ("Start number should be less than stop number!")

    
