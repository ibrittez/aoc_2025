from lobby import find_max, get_jotage, calc_total_joltage


def test_0():
    assert find_max("123") == 2
    assert find_max("321") == 0
    assert find_max("111") == 0
    assert find_max("000") == 0
    assert find_max("9123123123123854534685") == 0
    assert find_max("0123123123193854534685") == 11


def test_1():
    assert get_jotage("123", 2) == 23
    assert get_jotage("123\n", 2) == 23
    assert get_jotage("987654321111111", 2) == 98
    assert get_jotage("92312312312811111", 2) == 98


def test_2():
    f = open("./test")
    assert calc_total_joltage(f.readlines(), 2) == 357


def test_3():
    assert get_jotage("987654321111111", 12) == 987654321111
