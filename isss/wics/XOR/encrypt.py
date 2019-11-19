import base64
from secret import flag, key

# KEY is 1 byte

def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]

encrypted = []
for c in flag:
    encrypted.append(c ^ key)

x = bytes(encrypted)
print(x)
print(base64.b64encode(x).decode())
