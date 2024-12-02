tempstring = """
0
I have the following code to ping my ddns hostname and return if
 the host is up or down. I then tried adding the socket.gethostbyname
 which works for my normal hostname www.iamsimonsmale.co.uk but not http://ssmale.ddns.net.
 I have the following code to ping my ddns hostname and return if the host is up or down. I then tried adding the socket.gethostbyname which works for my normal hostname www.iamsimonsmale.co.uk but not http://ssmale.ddns.net.

I have tried to remove the http:// from the start of the address and this fails too.

#!/usr/bin/env python
# This script checks to see if the server is up or down and prints the pinged IP

import requests
import socket
import time

while True:

    host = 'http://ssmale.ddns.net'

    ip = socket.gethostbyname(host)

    print ip

    response = requests.get(host)
    if response.status_code == requests.codes.ok:
        print('Server Up')
    else:
        print('Server Down')
    time.sleep(10)
the error message for http://ssmale.ddns.net is

Traceback (most recent call last):
File "PingTestIP.py", line 12, in <module>
ip = socket.gethostbyname('http://ssmale.ddns.net')
socket.gaierror: [Errno -2] Name or service not known
and for ssmale.ddns.net is

Traceback (most recent call last):
File "PingTestIP.py", line 16, in <module>
response = requests.get(host)
File "/usr/lib/python2.7/dist-packages/requests/api.py", line 60, in get
return request('get', url, **kwargs)
File "/usr/lib/python2.7/dist-packages/requests/api.py", line 49, in request
return session.request(method=method, url=url, **kwargs)
File "/usr/lib/python2.7/dist-packages/requests/sessions.py", line 443, in request
prep = self.prepare_request(req)
File "/usr/lib/python2.7/dist-packages/requests/sessions.py", line 374, in prepare_request
hooks=merge_hooks(request.hooks, self.hooks),
File "/usr/lib/python2.7/dist-packages/requests/models.py", line 304, in prepare
self.prepare_url(url, params)
File "/usr/lib/python2.7/dist-packages/requests/models.py", line 358, in prepare_url
"Perhaps you meant http://{0}?".format(url))
requests.exceptions.MissingSchema: Invalid URL u'ssmale.ddns.net': No schema supplied. Perhaps you meant http://ssmale.ddns.net?
and when done with `www.iamsimonsmale.co.uk it works and the print is

86.136.251.202
Server Up
I have also tried to use the code from How do I get the IP address from a http request using the requests library? without success.

Using this tool (http://mxtoolbox.com/SuperTool.aspx#) i confirmed that there is an A record in the DNS for ssmale.ddns.net

What is causing the issue and how would i fix it?
 """
 
print (tempstring.count('python2.7'))

print ('--'*40)
print (tempstring.index('I'))#Finding the index of the string
print ('--'*40)
print (tempstring.find('when'))#Find helps to find the required string from a group strings.
#if it not present then it returns -1
print ('--'*40)
