from pwn import *
context.update(arch='i386',os='linux')
LOAD_ADDRESS = "0804E0A0"
pwn = asm("mov di, 0").rstrip()
pwn += asm("mov rsi, 0x"+LOAD_ADDRESS).rstrip()
pwn += asm("mov dx, 0x100").rstrip()
# make write syscall
pwn += asm("movw ax, 5").rstrip()
pwn += asm("int 0x80").rstrip()
pwn += asm("ret").rstrip()
print(pwn.rstrip())
