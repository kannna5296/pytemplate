

from datetime import datetime, timedelta
from unittest.mock import Mock, call

from test.better_test.feed import ZooDatabase, do_rounds



now_func = Mock(datetime.now)
now_func.return_value = datetime(2024, 6, 6, 12, 0)  # 1日以上経過後に変更

# Mock化する対象オブジェクトがDatabaseクラsスに集約されたので、 =Mock(xxx)がへっててすとが簡便になった!

database = Mock(spec=ZooDatabase)
database.get_food_period.return_value = timedelta(days=1)
database.get_animals.return_value = {
    "dog": datetime(2024, 6, 3, 11, 15),
    "cat": datetime(2024, 6, 4, 12, 30),
    "bird": datetime(2024, 6, 5, 12, 45),
}

result = do_rounds(
    zoo_db=database,
    species="dog",
    now_func=now_func,
)
assert result == 2

database.get_food_period.assert_called_once_with("dog")
database.get_animals.assert_called_once_with("dog")
database.feed_animal.assert_has_calls(
    [
        call("dog", now_func.return_value),
        call("cat", now_func.return_value),
    ],
    any_order=True,
)
