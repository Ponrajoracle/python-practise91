import traceback

#Exception handling approach
#'''
while True:
    try:
        tempVal = input("Enter a number:")
        print (int(tempVal))
    except Exception as eobj:
        print (traceback.format_exc())
        print ("Retry !!!!")
#'''
#Normal approach
'''
while True:
    tempVal = input("Enter a number:")
    print (int(tempVal))
'''
