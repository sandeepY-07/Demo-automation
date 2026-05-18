from pytest_bdd import scenarios, given, when, then, parsers

from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


scenarios("../features/checkout.feature")


@given("product is already added to cart")
def add_product_to_cart(driver):

    home = HomePage(driver)

    cart = CartPage(driver)

    home.click_laptops()

    home.click_product()

    cart.click_add_to_cart()

    cart.handle_cart_alert()

    cart.click_cart_menu()


@when("user clicks place order")
def click_place_order(driver):

    checkout = CheckoutPage(driver)

    checkout.click_place_order()


@when(parsers.parse('user enters name "{name}"'))
def enter_name(driver, name):

    checkout = CheckoutPage(driver)

    checkout.enter_name(name)


@when(parsers.parse('user enters country "{country}"'))
def enter_country(driver, country):

    checkout = CheckoutPage(driver)

    checkout.enter_country(country)


@when(parsers.parse('user enters city "{city}"'))
def enter_city(driver, city):

    checkout = CheckoutPage(driver)

    checkout.enter_city(city)


@when(parsers.parse('user enters card "{card}"'))
def enter_card(driver, card):

    checkout = CheckoutPage(driver)

    checkout.enter_card(card)


@when(parsers.parse('user enters month "{month}"'))
def enter_month(driver, month):

    checkout = CheckoutPage(driver)

    checkout.enter_month(month)


@when(parsers.parse('user enters year "{year}"'))
def enter_year(driver, year):

    checkout = CheckoutPage(driver)

    checkout.enter_year(year)


@when("user clicks purchase button")
def click_purchase(driver):

    checkout = CheckoutPage(driver)

    checkout.click_purchase()


@then("order should be placed successfully")
def verify_order(driver):

    checkout = CheckoutPage(driver)

    success_message = (
        checkout.get_success_message()
    )

    assert (
        "Thank you for your purchase!"
        == success_message
    )