#List Example 
import os
#'''
monthList = ['January','Feb','March','April','May','June','July','August']
outputlist = []#empty list
#print (monthList[0],monthList[-1])
#tempVar = monthList[0:2]
#print (type(tempVar))
for eachItem in monthList:
    try:
        print (eachItem)
        if eachItem.startswith('J') or eachItem.startswith('A'):
            outputlist.append(eachItem)
    except Exception as e:
        print (e)

print ("Output list:",outputlist)
