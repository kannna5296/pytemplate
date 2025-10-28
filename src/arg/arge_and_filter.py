import pandas as pd
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", help="処理するファイルの相対パス（複数指定可能）")  # 1個以上

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--tom", action="store_true", help="tomが含まれるフォルダだけ処理する")
    group.add_argument("--jerry", action="store_true", help="jerryが含まれるフォルダだけ処理する")

    args = parser.parse_args()

    if args.tom:
        path = [p for p in args.files if "tom" in p]
    elif args.jerry:
        path = [p for p in args.files if "jerry" in p]

    # これと一緒
    # path = []
    # if args.tom:
    #     for p in args.files:
    #         if 'tom' in p:
    #             path.append(p)
    # elif args.jerry:
    #     for p in args.files:
    #         if 'jerry' in p:
    #             path.append(p)

    print(path)


if __name__ == "__main__":
    main()
