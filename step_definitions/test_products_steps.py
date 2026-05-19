from pytest_bdd import scenarios, given, when, then

import time

from selenium.webdriver.common.by import By


scenarios("../features/products.feature")


@given("user is on homepage")
def open_homepage(driver):
    pass


@when("user explores mobile products")
def mobiles(driver):

    driver.find_element(
        By.XPATH,
        "//a[text()='Phones']"
    ).click()

    time.sleep(2)


@when("user explores laptop products")
def laptops(driver):

    driver.find_element(
        By.XPATH,
        "//a[text()='Laptops']"
    ).click()

    time.sleep(2)


@when("user explores monitor products")
def monitors(driver):

    driver.find_element(
        By.XPATH,
        "//a[text()='Monitors']"
    ).click()

    time.sleep(2)


@then("products should display successfully")
def verify_products(driver):

    assert "Apple monitor 24" in driver.page_source