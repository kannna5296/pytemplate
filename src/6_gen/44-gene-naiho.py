# 内包表記とジェネレータ式を双方使うこともできる！これもメモリ効率よし。
it = (len(x) for x in open("my_file.text"))
