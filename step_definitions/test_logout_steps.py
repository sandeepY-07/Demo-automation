from pytest_bdd import scenarios, when, then

from pages.logout_page import LogoutPage


scenarios("../features/logout.feature")


@when("user clicks logout button")
def logout(driver):

    logout = LogoutPage(driver)

    logout.click_logout()


@then("user should logout successfully")
def verify_logout(driver):

    logout = LogoutPage(driver)

    assert (
        "Log in"
        == logout.get_login_text()
    )