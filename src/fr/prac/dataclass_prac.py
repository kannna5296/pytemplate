from dataclasses import dataclass, field
import uuid


@dataclass
class MyClass:
    name: str = "default"  # 型アノテーションを付けるとdataclassのフィールドになる
    price: int = 100

    # 型アノテーションがないと、ただのクラス変数になってprint(obj)で表示されない
    # dataclassは型アノテーションがある属性だけをフィールドとして扱います。
    # name = "default" → クラス変数（print(obj)で表示されない）
    # name: str = "default" → dataclassのフィールド（print(obj)で表示される）

    # fieldをつけるといろんなことができる. dataclassのフィールドを色々カスタマイズできる
    id: int = field(
        compare=False, default_factory=lambda: str(uuid.uuid4())
    )  # compare=Falseとすると、==や!=で比較するときに無視される
    items: list = field(default_factory=list)  # 毎回新しいlistを作成.
    # share_items: list = {}
    password: int = field(
        default="secret", repr=False
    )  # repr=Falseとすると、print(obj)したときにhiddenが表示されなくなる
    readonly: int = field(default=1, init=False)  # __init__ではなく、__post_init__で初期化される

    def __post_init__(self):
        self.readonly = 2


# main関数
def main():
    obj = MyClass()
    obj2 = MyClass()

    obj.name = "new"

    # obj.share_items.append(1)
    print(obj)
    print(obj2)


if __name__ == "__main__":
    main()


# property使いたい時
# /そのフィールドにset時バリデーションをつけたい時（property + setter)
# /参照時に計算を含めた計算にしたい時（関数でもできるけど、()がいらなくなったりより簡潔に呼び出せる）
# /読み取り参照にしたい時 propertyをつけて、setterをつけない
# /広報互換性を保ちたい時
# 昔: self.name = "太郎"
# 今: バリデーション追加したいけど既存コードは変えたくない
# @property
# def name(self):
#     return self._name

# @name.setter
# def name(self, value):
#     if not value:
#         raise ValueError("空はダメ")
#     self._name = value
