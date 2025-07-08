from typing import Final

def main():
    # 設定ファイル読み込み
    print("##### 変更可能な話 #####")
    mutable = Mutable()
    print("変更前 " +str(mutable.count))
    mutable.count = 1
    print("変更後 " +str(mutable.count))

    print()

    print("##### 変更不可能な話 #####")
    immutable = Immutable(10)
    print("変更前 " +str(immutable.count))
    immutable.count = 1 #AttributeError: property 'count' of 'Immutable' object has no setter
    print("変更後 " +str(immutable.count))

    print()

    print("##### 変更不可能な話 #####")
    final = Final()
    print("変更前 " +str(final.count))
    final.count = 1
    print("変更後 " +str(final.count))

class Mutable:
    count = 3.14

class Immutable:
    def __init__(self, count):
        self._count = count

    @property
    def count(self):
        return self._count

class Final:
    count : Final = 1

if __name__ == "__main__":
    main()
