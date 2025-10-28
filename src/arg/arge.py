import pandas as pd
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="複数のCSVファイルを処理し、id列の存在をチェックします")
    parser.add_argument("files", nargs="+", help="処理するファイルの相対パス（複数指定可能）")  # 1個以上

    args = parser.parse_args()
    print(args.files)


if __name__ == "__main__":
    main()
