from src.widget import get_date, mask_account_card


def test_mask_account_card_first(card_str):
    assert mask_account_card("Visa Platinum 7000792289606361") == card_str


def test_mask_account_card_second():
    assert mask_account_card("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"


def test_mask_account_card_third(check_str):
    assert mask_account_card("Счет 35383033474447895560") == check_str


def test_get_date():
    assert get_date("2018-07-11T02:26:18.671407") == "11.07.2018"
