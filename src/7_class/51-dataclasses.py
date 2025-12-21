from dataclasses import asdict, astuple, dataclass, field


@dataclass(kw_only=True)
class RGB:
    red: int
    green: int
    blue: int
    default1: float = 3.14
    default2: list = field(
        default_factory=lambda: [1, 2, 3]
    )  # default_factoryは関数的に書かないといけない


rgb = RGB(red=1, green=2, blue=3)
rgb_alt = RGB(red=1, green=2, blue=3)
rgb_alt2 = RGB(red=1, green=2, blue=4)
print(rgb)  # __repr__の実装が省ける
print(f"astuple, {astuple(rgb)}")  # astupleが自動で生えてくる
print(f"asdict, {asdict(rgb)}")  # asdictが自動で生えてくる
print(f"eq, {rgb == rgb_alt}")
print(f"eq, {rgb == rgb_alt2}")


@dataclass(order=True)
class Version:
    major: int
    minor: int
    patch: int


# 大小比較ができる:
ver_x = Version(3, 10, 12)
ver_y = Version(3, 9, 18)
print(ver_x > ver_y)

# majorを比較→一緒なので次へ
# minorを比較→xがかってるのでxの勝ち
# patchは見ない
