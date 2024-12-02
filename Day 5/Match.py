#Author:Ponraj
#Date:16/09/2024
#Purpose:Match paramemter
#CopyRight :

num=int(input("enter a number between 1 and 3:"))

match num:
    
    case 1:
        print("one condition is met")
    case 2:
        print("two condition met")
    case 3:
        print("third condition met")
    case 4:
        print("Fourth condition met")
    case _:
        print("number not between 1 and 3")
        '''
# match case to check a character in a string
def runMatch(): #Defining a function
    myStr = "Hello World"
    # match case
    match (myStr[6]):
        case "w":
            print("Case 1 matches")
        case "W":
            print("Case 2 matches")
        case _:
            print("Character not in the string")
           
runMatch()#calling a function
'''
                  
