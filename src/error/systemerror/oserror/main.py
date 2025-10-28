import sys


def main():
    try:
        # システムレベルの処理
        with open("a.txt") as f:
            print(f.read())
            pass
        # 実際にはOSErrorを実装したFileNotFoundErrorが出る
    except OSError as e:
        print(f"システムエラー: {e}")
        sys.exit(1)  # プログラム終了
