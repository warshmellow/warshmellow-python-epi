def halve(x):
    return x >> 1


def is_odd(x: int) -> bool:
    return x & 1 == 1


def is_even(x: int) -> bool:
    return not is_odd(x)


def bin_gcd(u, v: int) -> int:
    if u == 0:
        return v

    if v == 0:
        return u

    if is_even(u) and is_even(v):
        return 2 * bin_gcd(halve(u), halve(v))

    if is_even(u) and is_odd(v):
        return bin_gcd(halve(u), v)

    if is_odd(u) and is_even(v):
        return bin_gcd(u, halve(v))

    # both odd
    if u >= v:
        return bin_gcd(halve(u - v), v)
    else:
        return bin_gcd(u, halve(v - u))
