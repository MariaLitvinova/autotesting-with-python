import pytest


class TestMainPage():
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_can_login(self, browser):
        print("1")
        assert True

    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket(self, browser):
        print("2")
        assert True


class TestBasket():
    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_guest_can_go_to_payment_page(self, browser):
        print("3")
        assert True

    @pytest.mark.smoke
    def test_guest_can_see_total_price(self, browser):
        print("4")
        assert True


@pytest.mark.skip
class TestBookPage():
    @pytest.mark.smoke
    def test_guest_can_add_book_to_basket(self, browser):
        print("5")
        assert True

    @pytest.mark.regression
    def test_guest_can_see_book_price(self, browser):
        print("6")
        assert True


@pytest.mark.beta_users
@pytest.mark.smoke
def test_guest_can_open_gadget_catalogue(browser):
    print("7")
    assert True