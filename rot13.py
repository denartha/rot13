#!/usr/bin/env python
import sys
import string
import re


msg = sys.argv[1]
key1 = sys.argv[2]
key = int(key1)



pattern = re.compile('\W')
msg = re.sub(pattern, '', msg)

print "Using Rot-" + str(key)




for c in msg:
    if c.isalpha():
        num = ord(c)
        num += key
        if c.isupper():
            if num > ord('Z'):
                num -= 26
            elif num < ord('A'):
                num += 26
        elif c.islower():
            if num > ord('z'):
                num -= 26
            elif num < ord('a'):
                num += 26 
    sys.stdout.write(chr(num))
print ""
