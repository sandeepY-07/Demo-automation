from pytest_bdd import scenarios, given, when, then

import time


scenarios("../features/home.feature")


@given("user is on homepage")
def open_homepage(driver):
    pass


@when("user scrolls homepage")
def scroll_homepage(driver):

    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )

    time.sleep(2)

    driver.execute_script(
        "window.scrollTo(0, 0);"
    )


@then("homepage should load successfully")
def verify_homepage(driver):

    assert "STORE" in driver.page_source