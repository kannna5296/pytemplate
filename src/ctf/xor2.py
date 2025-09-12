"""
XOR暗号化のデモンストレーション

このスクリプトは、平文とキーを使用してXOR暗号化を実行し、
暗号化プロセスの詳細を表示します。

処理内容:
1. 平文 "abc" とキー "hog" を定義
2. 各文字をバイトに変換
3. 平文の各バイトとキーの対応するバイトでXOR演算を実行
4. 暗号化プロセスの詳細（バイナリ、16進数表示）を出力
5. 結果をBase64エンコードして表示

XOR暗号化の特徴:
- 同じキーで2回XOR演算を行うと元の平文に戻る
- キーが平文より長い場合、キーは繰り返し使用される
"""

import base64

plain = "abc"
key = "\x00xx"  # 最初の文字は暗号化しない（NULL文字）、残りは'x'
# "0xx"だと、ACSII変換すると48になっちゃうのでまた違う話になる

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

print("====== 余談 =======")

print('ASCII値0の文字の確認:')
# ordはユニコードに変換するやつ
print('ord(\"\\x00\"):', ord('\x00'))
print('ord(\"\\0\"):', ord('\0'))
print('chr(0):', repr(chr(0)))
print('chr(0) == \"\\x00\":', chr(0) == '\x00')
print('chr(0) == \"\\0\":', chr(0) == '\0')
