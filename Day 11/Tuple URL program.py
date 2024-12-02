import os
import traceback

urlTuple = ('www.facebook.com','www.google.com','www.abc121312.com')

try:
    for eUrl in urlTuple:
        print (eUrl)
        pingCmd = 'ping %s'%eUrl
        print (pingCmd)
        var = os.popen(pingCmd).read()
        print (var)
        if 'Reply from' in var:
            print ("url %s is active"%eUrl)
        else:
            print ('url %s is not active'%eUrl)
        
except Exception as e:
    print (traceback.format_exc())
