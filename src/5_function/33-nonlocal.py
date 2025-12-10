def sort_priority(numbers, group):
    found = False

    def helper(x):
        nonlocal found  # これがない場合、6行目のTrueはスコープ外になるので、変更されない
        if x in group:
            found = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return found


numbers = [8, 4, 1, 2, 5, 4, 7, 6]
group = [2, 3, 5, 7]

found = sort_priority(numbers, group)
print(found)
print(numbers)
