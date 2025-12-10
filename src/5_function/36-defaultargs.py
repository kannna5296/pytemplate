from datetime import datetime
from time import sleep


def log(message, time=datetime.now()):
    print(f"{message}, {time}")


log("こんにちは！")
sleep(0.1)
log("こんにちは！！")  # 同じ値しか出ない。 関数定義時にnowが1回呼び出されるだけだから
# 引数がミュータブル（=関数内部で変わるとき）な場合はデフォルトを関数定義の中で使っちゃダメ！！！


def log_time(message: str, time: datetime | None = None):
    if time is None:
        time = datetime.now()
    print(f"{message}, {time}")


log_time("ちゃんとこんにちは！")
sleep(0.1)
log_time("ちゃんとこんにちは！！")  # 違う値が出る。意図どおり。
