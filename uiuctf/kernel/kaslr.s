
start:
  mov $0, %ebx
  mov $0x0804e0a0, %ecx
  mov $0x20, %edx

  mov $5, %eax
  int $0x80
  ret
