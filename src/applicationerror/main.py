import json


def main():
    print("ハロワ")
    # 設定ファイル読み込み
    print("############################## FileNotFoundError ###################################")
    file_open(file_path="src/applicationerror/config.jso")

    print("############################## JSONDecodeError ###################################")
    file_open(file_path="src/applicationerror/ngconfig.json")

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
