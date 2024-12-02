try:
    tempString = "welcome To Elegant"
    print (tempString.capitalize())#Makes first letter as capital in a sentence 
    print (tempString.lower())#Converts everything to lower
    print (tempString.upper())#converts entire string to upper
    print (tempString.count('e'))#number of occurance of that character
    print (tempString.lower().count('e'))
    
    '''
    cnt = 0
    for echar in tempString:
        if echar.lower()=='e':
            cnt +=1 #cnt = cnt+1
            print ("string %s contains %d times e"%(tempString,cnt))
            '''
except Exception as e:
    print (e)
