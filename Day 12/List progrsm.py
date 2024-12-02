searchList = [2000,2000,2003,2005,2006,'Python','Code',1,2,'three',4]
print (searchList)
print("Original List length:",len(searchList))
searchList.insert(4,"johnson") #insert an item into the list based on provided index
print (searchList)
print("After insert List length:",len(searchList))

print (searchList.index('Python'))#tell the index of the list
print (searchList.pop())
print (searchList)

print (searchList.pop(1))#Pop will remove the element as per the given index

print (searchList)
searchList.remove('Python') #Remove based on the given value
print (searchList)
#
'''
'''
searchList.reverse()
print (searchList)
searchList = [1000,234,121,12000,3456,37899]
searchList.sort()
print (searchList)
#
# print (min(searchList))
# print (max(searchList))
'''
#if 'Python' in searchList:
    #print "Sucess"
#'''
'''
salryList = [10000,3000,7000,20000,1000344]
salryList.sort()
print (salryList)
print (salryList[-2])

tempString = "python"
print max(tempString)
salryList = [10000,3000,7000,20000,1000344]
print max(salryList)
print min(salryList)
'''
