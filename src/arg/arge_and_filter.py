import pandas as pd
import argparse
from pathlib import Path



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'files',
        nargs='+', #1個以上
        help='処理するファイルの相対パス（複数指定可能）'
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--tom', action='store_true', help='tomが含まれるフォルダだけ処理する')
    group.add_argument('--jerry', action='store_true', help='jerryが含まれるフォルダだけ処理する')

    if parser.parse_args().tom:
        path = [p for p in parser.parse_args().files if 'tom' in p]
    elif parser.parse_args().jerry:
        path = [p for p in parser.parse_args().files if 'jerry' in p]

    print(path)

if __name__ == '__main__':
    main()
