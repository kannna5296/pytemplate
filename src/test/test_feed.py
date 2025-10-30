from datetime import datetime, timedelta
from test.feed import do_rounds, feed_animal, get_animals, get_food_period
from unittest.mock import Mock, call

# Mock
database = object()
now_func = Mock(datetime.now)
now_func.return_value = datetime(2024, 6, 6, 12, 0)  # 1日以上経過後に変更

food_func = Mock(get_food_period)
food_func.return_value = timedelta(days=1)

animals_func = Mock(get_animals)
animals_func.return_value = {
    "dog": datetime(2024, 6, 3, 11, 15),
    "cat": datetime(2024, 6, 4, 12, 30),
    "bird": datetime(2024, 6, 5, 12, 45),
}

feed_func = Mock(feed_animal)

# Test

result = do_rounds(
    database=database,
    species="dog",
    now_func=now_func,
    food_func=food_func,
    animals_func=animals_func,
    feed_func=feed_func,
)
assert result == 2

food_func.assert_called_once_with(database, "dog")
animals_func.assert_called_once_with(database, "dog")
feed_func.assert_has_calls(
    [
        call(database, "dog", now_func.return_value),
        call(database, "cat", now_func.return_value),
    ],
    any_order=True,
)
