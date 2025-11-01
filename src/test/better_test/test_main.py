import contextlib
from datetime import datetime
import io
from unittest.mock import patch

from test.better_test.feed import ZooDatabase

with patch("__main__.DATABASE", spec=ZooDatabase):
    now = datetime.now()

    DATABASE.get_food_period.return_value = datetime.timedelta(days=1)
    DATABASE.get_animals.return_value = {
        "dog": datetime(2024, 6, 3, 11, 15),
        "cat": datetime(2024, 6, 4, 12, 30),
        "bird": datetime(2024, 6, 5, 12, 45),
    }

    fake_stdout = io.StringIO()
    with contextlib.redirect_stdout(fake_stdout):
        main(["program_name", "dog"])

        found = fake_stdout.getvalue().strip()
        expeted = "Fed 2 dog (s)"
        assert found == expeted
