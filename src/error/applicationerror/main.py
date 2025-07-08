import json


def main():
    # 設定ファイル読み込み
    print(
        "############################## FileNotFoundErrorが起きる例 ###################################"
    )
    file_open(file_path="src/error/applicationerror/config.jso")

    print(
        "############################## JSONDecodeErrorが起きる例 ###################################"
    )
    file_open(file_path="src/error/applicationerror/ngconfig.json")


def file_open(file_path: str):
    try:
        with open(file_path) as f:
            config = json.load(f)
            print(config)
    except FileNotFoundError as e:
        print(e)
        print("設定ファイルが見つかりません")
        config = {}  # デフォルト設定で継続
    except json.JSONDecodeError as e:
        print(e)
        print("設定ファイルの形式が不正です")
        config = {}  # デフォルト設定で継続


if __name__ == "__main__":
    main()
