https://dev.classmethod.jp/articles/black_block_string_auto_format/

- black(formatter)を使っている中で、formatをOffにしたいときは`#fmt: off`と`#fmt: on`で囲む
- ex
```
# fmt: off
df = pd.DataFrame(~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~長ーい文字列~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~)
# fmt: on
```
