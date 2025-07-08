from dataclasses import dataclass


def main() -> None:
    print("##### dataclassにより実行時エラーとなる #####")
    u = User("Taro", 20)
    print("変更前 " + str(u.age))
    u.age = 30  # FrozenInstanceError!
    print("変更後 " + str(u.age))


@dataclass(frozen=True)
class User:
    name: str
    age: int


if __name__ == "__main__":
    main()
