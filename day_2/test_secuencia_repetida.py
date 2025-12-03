import gift_shop as day2


def test_0():
    assert day2.fraccionar_cadena("123456", 2) == ["123", "456"]


def test_1():
    assert day2.fraccionar_cadena("123456", 3) == ["12", "34", "56"]


def test_2():
    assert day2.fraccionar_cadena("123456", 6) == [
        "1", "2", "3", "4", "5", "6"]


def test_if_module_not_zero_reurn_none():
    assert day2.fraccionar_cadena("123456", 4) == None


def test_gift_shop_part_2():
    day2.gift_shop_part_1("./test") == 1227775554


def test_encontrar_repeticiones_0():
    assert day2.encontrar_repeticiones("11-22") == 11 + 22
    assert day2.encontrar_repeticiones("95-115") == 99 + 111
    assert day2.encontrar_repeticiones("998-1012") == 999 + 1010


def test_encontrar_repeticiones_no_repetir():
    assert day2.encontrar_repeticiones("222220-222224") == 222222


def test_gift_shop_part_2():
    day2.gift_shop_part_2("./test") == 4174379265
