# Effective Python 項目43
# yieldを使って
# yieldは、関数を一時的に実行停止させることが出来る機能を持つ文です。
# メモリ消費量を抑えたりできるのが良いが、再利用は不可。

def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == " ":
            yield index + 1

address = "Four score and seven years ago..."
result = list(index_words_iter(address))
print(result[:20])
