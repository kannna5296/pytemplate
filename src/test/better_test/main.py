import contextlib
from datetime import datetime, timedelta
import io
from unittest.mock import patch
from test.better_test.feed import ZooDatabase, do_rounds


DATABASE = None

def get_database():
    global DATABASE
    if DATABASE is None:
        DATABASE = ZooDatabase(database = object())
    return DATABASE

def main(argv):
    db = get_database()
    species = argv[1]
    count = do_rounds(zoo_db=db, species=species)
    print(f"Fed {count} {species} (s)")
    return 0

# if __name__ == "__main__":
#     import sys
#     sys.exit(main(sys.argv))
with patch("__main__.DATABASE", spec=ZooDatabase):
    now = datetime.now()

    DATABASE.get_food_period.return_value = timedelta(days=1)
    DATABASE.get_animals.return_value = {
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
