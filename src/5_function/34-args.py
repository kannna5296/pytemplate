# 元々の可変長引数
def log(message, *values):
    if not values:
        print(message)
    else:
        print(type(values)) # tupleで受け取る
        values_str = ", ".join(str(x) for x in values)
        print(f"{message}: {values_str}")

# アプデした関数。可変長以外のところに変数を追加する
def log_seq(sequence, message, *values):
    if not values:
        print(f"{sequence} - {message}")
    else:
        values_str = ", ".join(str(x) for x in values)
        print(f"{sequence} - {message} : {values_str}")

log("私の数字は",1,2)
log("こんにちは引数なし")


log_seq(1, "私の数字は",1,2)
log_seq("私の数字は",1,2) #アプデした後は、微妙に表示が変わっちゃう（後方互換性が足りない）
