from typing import Final


def main() -> None:
    print("##### 実行はできる。が、静的ツールに怒ってもらえる話 #####")
    final = FinalClass()
    print("変更前 " + str(final.count))
    final.count = 10
    # mypy main.pyをすると、error: Cannot assign to final attribute "count"  [misc]
    # 実行はできちゃう
    print("変更後 " + str(final.count))


class FinalClass:
    count: Final[int] = 1


if __name__ == "__main__":
    main()
