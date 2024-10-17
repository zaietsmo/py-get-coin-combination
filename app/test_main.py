from app.main import get_coin_combination


def test_get_coin_combination_zero():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_get_coin_combination_penny():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_coin_combination_nickel():
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_get_coin_combination_dime():
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_get_coin_combination_quarter():
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_get_coin_combination_mixed_41():
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_get_coin_combination_mixed_99():
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_get_coin_combination_large_value():
    assert get_coin_combination(100) == [0, 0, 0, 4]
