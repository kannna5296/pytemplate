from test.better_test.feed import ZooDatabase, do_rounds

DATABASE = None


def get_database():
    global DATABASE
    if DATABASE is None:
        DATABASE = ZooDatabase(database=object())
    return DATABASE


def main(argv):
    db = get_database()
    species = argv[1]
    count = do_rounds(zoo_db=db, species=species)
    print(f"Fed {count} {species} (s)")
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main(sys.argv))
