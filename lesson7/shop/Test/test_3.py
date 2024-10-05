from lesson7.shop.Pages.shopcontainer import ShopContainer
from lesson7.shop.Pages.shopmain import ShopmainPage


def test_shop(chrome_browser):
    expected_total = "58.29"

    shopmain = ShopmainPage(chrome_browser)
    shopmain.registration_fields()
    shopmain.by_issue()
    shopmain.click_issue()
    shopmain.into_container()

    container = ShopContainer(chrome_browser)
    container.checkout()
    container.info()
    container.price()

    assert expected_total in container.price()
    print(f"Итоговая сумма равна ${container.price()}")
