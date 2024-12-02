tempStr = "Welcome To Elegant 123 !#!"
#print (dir(tempStr))#Attributes of a class
lCnt,uCnt,dCnt,sCnt,Ocnt = 0,0,0,0,0
for eChar in tempStr:
   if eChar.islower():
      lCnt +=1
   elif eChar.isupper():
      uCnt +=1
   elif eChar.isdigit():
      dCnt +=1
   elif eChar.isspace():
      sCnt +=1
   else:
      Ocnt +=1
print (lCnt,uCnt,dCnt,sCnt,Ocnt)
