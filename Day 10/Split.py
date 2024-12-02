tempString = "module1_stringSlice.py"
print (tempString)

#'''
tempString = '  Subnet Mask . . . . . . . . . . . : 255.255.255.0    '
print(tempString.strip())#removes the spaces from left and right most sides
print(tempString.lstrip())
print(tempString.rstrip())

'''
#print (tempString.split(':')[-1])
print (tempString.split(':')[-1].lstrip())
print (tempString.split(':')[-1].rstrip())
print (tempString.split(':')[-1].strip())
if tempString.split(':')[-1].strip() == '255.255.255.0':
    print ("matching")
else:
    print ("Not matching")

tempString = tempString.strip('.py')
print ("Stripped string:",tempString)
'''
