# Python `builtins.pyi` を完全に読みたい時のガイド

## 1. IDE のスタブは "一部だけ" なのが普通

VSCode や PyCharm が生成する `builtins.pyi` は必要な部分だけを抜き出したスタブです。完全版ではありません。完全な定義は **typeshed** にあります。

### ✔ 完全版スタブ

* [https://github.com/python/typeshed/blob/main/stdlib/builtins.pyi](https://github.com/python/typeshed/blob/main/stdlib/builtins.pyi)

---

## 2. 実際の実装は C コードにある

`int` / `dict` / `str` などの内部処理は CPython の C コードに書かれているため、`.pyi` の時点で“途中までしかない”のは仕様です。

### ✔ CPython の実装

* [https://github.com/python/cpython/tree/main/Objects](https://github.com/python/cpython/tree/main/Objects)

---

## 3. VSCode のスタブは複数ファイルに分割されている

VSCode の Python 拡張が利用するスタブは以下のように分かれています：

* `builtins.pyi`（一部）
* `_typeshed/*.pyi`
* `typing.pyi`
* `collections.abc` に移動した共通メソッド

そのため、一つのファイルだけ見ると“途中で終わってる”ように見える状態になりやすいです。

---

## 4. 手元で完全版スタブを読む方法

`typeshed` をそのままインストールできます：

```bash
pip install typeshed
```

インストール後、次にアクセス：

```
site-packages/typeshed/stdlib/builtins.pyi
```

---

## 5. `builtins.pyi` が短く見える理由まとめ

| 原因           | 説明                              |
| ------------ | ------------------------------- |
| IDE が部分的に生成  | 必要部分だけ抽出している                    |
| `.pyi` は宣言だけ | 内部実装までは書かない仕様                   |
| ファイル分割       | `_typeshed` や `typing` 側へ移動している |
| 非公開APIは書かれない | オフィシャルスタブの方針                    |

---

## 6. どれを読むべきか

**型定義が知りたい → typeshed**

**内部挙動まで理解したい → CPython の C 実装**
