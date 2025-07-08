from typing import Final

def main():
    print("##### 実行はできる。が、静的ツールに怒ってもらえる話 #####")
    final = Final()
    print("変更前 " +str(final.count))
    final.count = 10
    print("変更後 " +str(final.count))

class Final:
    count : Final = 1

if __name__ == "__main__":
    main()
