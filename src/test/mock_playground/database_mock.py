from datetime import datetime
from test.mock_playground.database import get_annimals
from unittest.mock import ANY, Mock

# get_aninmalsをMockする
mock = Mock(spec=get_annimals)
expected = {
    "dog": datetime(2024, 6, 5, 11, 15),
    "cat": datetime(2024, 6, 6, 12, 30),
    "bird": datetime(2024, 6, 7, 9, 45),
}
mock.return_value = expected


# Mockの利用
database = object()
result = mock(database, "dog")
a = mock(database, "cat")
b = mock(database, "bird")
c = mock(database, "fish")
assert result == expected

# 特定の引数で かつ 1回だけ呼ばれた！みたいなやつはない

# assert_called_with: 直近の呼び出しをチェック
mock.assert_called_with(ANY, "fish")  # assert不要！メソッド自体が例外を出す
print("✅ 直近はfishで呼ばれている")

# assert_called_once_with: 全体で1回だけ呼ばれたかチェック（これは失敗する！複数回呼んでいるから）
try:
    mock.assert_called_once_with(ANY, "dog")  # これは失敗する
except AssertionError as e:
    print(f"❌ dogは複数回呼ばれている可能性: {e}")

# assert_any_call: 過去の呼び出し履歴から探す
mock.assert_any_call(ANY, "dog")
print("✅ 過去にdogで呼ばれたことがある")

# 呼び出し回数をチェック
assert mock.call_count == 4, f"期待: 4回, 実際: {mock.call_count}回"
print(f"✅ 合計{mock.call_count}回呼ばれた")
