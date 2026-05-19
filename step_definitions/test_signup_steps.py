from pytest_bdd import scenarios, given, when, then

import json
import random
import time

from selenium.webdriver.common.keys import Keys

from pages.signup_page import SignupPage


scenarios("../features/signup.feature")


@given("user is on homepage")
def open_website(driver):
    # driver fixture already opens the homepage in conftest
    pass


@when("user clicks signup menu")
def click_signup(driver):

    signup = SignupPage(driver)

    signup.click_signup_menu()


@when("user enters signup username")
def enter_signup_username(driver):

    signup = SignupPage(driver)

    username = "user" + str(random.randint(1000, 9999))

    # save generated credentials for later use
    with open("data/users.json", "w") as file:
        json.dump({"username": username}, file)

    signup.enter_username(username)


@when("user enters signup password")
def enter_signup_password(driver):

    signup = SignupPage(driver)

    password = "test@123"

    # append password to the saved file
    try:
        with open("data/users.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data["password"] = password

    with open("data/users.json", "w") as file:
        json.dump(data, file)

    signup.enter_password(password)


@when("user clicks signup button")
def click_signup_button(driver):

    signup = SignupPage(driver)

    signup.click_signup_button()


@then("signup should be successful")
def verify_signup(driver):

    signup = SignupPage(driver)

    alert_text = signup.wait_for_alert_and_accept()

    assert "Sign up successful." in alert_text

    time.sleep(1)

    # close the signup modal if it's still open
    try:
        driver.switch_to.active_element.send_keys(Keys.ESCAPE)
    except Exception:
        pass

    time.sleep(1)