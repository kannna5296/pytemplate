import base64

# Given inputs
encrypted = "VllRAlMDBAEAAlJbVQAABwULAABTX1IAVFldWQsBVg1TBAUA"  # 暗号化後のやつ
plain = b"e852b4f2-37c0-4403-8df1-faea8805d41b"  # 認証トークン

# base64でデコード(bytesに変換)
encrypted_raw = base64.b64decode(encrypted)
print("encrypted_raw: ", encrypted_raw)

# for i in range(len(encrypted_raw)):
#     print("encrypted_raw[i]: ", encrypted_raw[i], hex(encrypted_raw[i]))

print("plain: ", plain)

print("len(plain): ", len(plain))
print("len(encrypted_raw): ", len(encrypted_raw))


dec_chars = []
for i in range(len(plain)):
    dec = encrypted_raw[i] ^ plain[i]  # 2進数変換してXORをして暗号鍵を取得
    print(i, encrypted_raw[i], plain[i], dec, hex(dec), chr(dec))
    dec_char = chr(dec)  # 暗号鍵は印字可能文字なのでASCIIに変換
    dec_chars.append(dec_char)  # 最後にまとめて表示するためにリストに格納

print("".join(dec_chars))
