from typing import Final


def main():
    # 設定ファイル読み込み
    print("##### 変更可能な話。ちゃんと切り替わる #####")
    mutable = Mutable()
    print("変更前 " + str(mutable.count))
    mutable.count = 1
    print("変更後 " + str(mutable.count))

    print()

    print("##### 変更不可能。実行時エラー #####")
    immutable = Immutable(10)
    print("変更前 " + str(immutable.count))
    immutable.count = (
        1  # AttributeError: property 'count' of 'Immutable' object has no setter
    )
    print("変更後 " + str(immutable.count))


class Mutable:
    count = 3.14


class Immutable:
    def __init__(self, count):
        self._count = count

    @property
    def count(self):
        return self._count


class Final:
    count: Final = 1


if __name__ == "__main__":
    main()
