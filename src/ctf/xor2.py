import base64

plain = "abc"
key = "hoghoghoghoghoghogh"

b_plain = plain.encode()
print("b_plain: ", b_plain)

b_key = key.encode()
print("b_key: ", b_key)

result = []
print("暗号化開始!")
for i in range(len(b_plain)):
    print(i, "番目")
    print("plain", b_plain[i], bin(b_plain[i]), hex(b_plain[i]))
    print("key", b_key[i], bin(b_key[i]), hex(b_key[i]))
    b_encrypted = b_plain[i] ^ b_key[i]
    print("encrypted", b_encrypted, bin(b_encrypted), hex(b_encrypted))
    result.append(chr(b_encrypted))

print("result: ", result)
print("".join(result))
print(base64.b64encode("".join(result).encode()))
