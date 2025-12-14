def index_words(text):
    """文字列内の単語ごとにインデックスを付与する。その際、リストを返す"""
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == " ":
            result.append(index + 1)
    return result

# 「リストをそのまま出すのでメモリ不足の恐れあ理、可読性が低いので...⇩のようにジェネレータを返し、呼び出されたごとに処理を進めるようにする


def index_words_iter(text):
    """文字列内の単語ごとにインデックスを付与する。その際、ジェネレータを返す"""
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == " ":
            yield index + 1

address = "Four score and seven years ago... a i u e o"

it = index_words_iter(address)
print(next(it))
print(next(it))
print(next(it))

# ジェネレータ→リストに与えて変換も可能
result = list(index_words_iter(address))
print(result)

# Pythonには、関数の中で値を一度に全て返すのではなく、1つずつ「遅延して」返すためのキーワードとしてyieldがあります。
# https://qiita.com/shun_sakamoto/items/5f13fa96701ba3727dc0


# 内包表記とジェネレータ式を双方使うこともできる！これもメモリ効率よし。
#it = (len(x) for x in open("my_file.text"))
