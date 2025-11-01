import contextlib
import io
from datetime import datetime, timedelta
from unittest.mock import patch

from test.better_test.feed import ZooDatabase
from test.better_test.main import main


def test_main_feeds_animals():
    with patch("test.better_test.main.DATABASE", spec=ZooDatabase) as mock_database:

        mock_database.get_food_period.return_value = timedelta(days=1)
        mock_database.get_animals.return_value = {
            "dog": datetime(2024, 6, 3, 11, 15),
            "cat": datetime(2024, 6, 4, 12, 30),
            "bird": datetime(2024, 6, 5, 12, 45),
        }

        fake_stdout = io.StringIO()
        with contextlib.redirect_stdout(fake_stdout):
            main(["program_name", "dog"])

            found = fake_stdout.getvalue().strip()
            expected = "Fed 3 dog (s)"
            assert found == expected, f"Expected: '{expected}', but got: '{found}'"


if __name__ == "__main__":
    test_main_feeds_animals()
