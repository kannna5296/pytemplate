def safe_division_f(
        numerator, #位置引数のみ. numerator=hogeで指定不可
        denominator,
        /,
        ndigits = 10, #位置引数でもkey引数でも両方いける
        *,
        ignore_overflow = False, #key引数のみ. Trueだけで指定不可
        ignore_zero_divition = False,
):
    try:
        fraction = numerator / denominator
        return round(fraction, ndigits)
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_divition:
            return float("inf")
        else:
            raise

print(safe_division_f(22,7))
print(safe_division_f(22,7,5))
print(safe_division_f(22,7, ndigits=2))
print(safe_division_f(numerator = 22,7,5))

print(safe_division_f(22,0, ignore_zero_divition=True))
print(safe_division_f(10**400,0.1, ignore_overflow=True))
