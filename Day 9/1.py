import traceback

try:    
    tempStr = "Welcome to Elegant"
    print (id(tempStr))

    #tempStr = tempStr[0:6]
    #print (id(tempStr))
    #print (tempStr)
    #'''
    print (len(tempStr))
    print (tempStr[0])#W
    print (tempStr[-1])#t
    print (tempStr[0:3])#wel
    print (tempStr[3:])#
    print (tempStr[:3])
    print (tempStr[:-2])
    print (tempStr[-2:])#prints only last two charchacters
    #tempStr[0] = 'L'
    #print (tempStr)
    del tempStr
    print (tempStr)
    #'''
    

except Exception as e:    
    print (traceback.format_exc())
    
