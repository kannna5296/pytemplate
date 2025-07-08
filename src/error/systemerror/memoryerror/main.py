import json
import sys


def main():
    try:
        huge_data = [0] * (10**10)  # 大量メモリ使用
    except MemoryError as e:
        # プロセスがKilledしちゃうので以下のログは見れない。。
        print(e)
        print("メモリ不足です")
        sys.exit(1)  # プログラム終了


if __name__ == "__main__":
    main()
