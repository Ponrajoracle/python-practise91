'''
for val in "Welcome to india":
    if val=="i":
      break
    print(val)
else:
    print("the end")

    #continue

'''
import os
import subprocess
import time

while True:
    print ("Welcome to monitoring services")
    time.sleep(10)
    #cmdString = "tasklist /fi "
    cmd = 'tasklist /fi "imagename eq {}"'.format("notepad++.exe")
    print(cmd)
    output = subprocess.check_output(cmd).decode()
    print (output)
    if "INFO: No tasks are running" in output:
        print ("Expected tasks are not running , please do have a check !!!")

    else:
        break
print("We are now out side of the while loop!!!")

