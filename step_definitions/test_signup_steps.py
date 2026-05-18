from pytest_bdd import scenarios, given, when, then

from faker import Faker
import random
import json

from pages.signup_page import SignupPage


fake = Faker()

scenarios("../features/signup.feature")


@given("user is on homepage")
def open_homepage(driver):
    pass


@when("user clicks signup menu")
def click_signup_menu(driver):

    signup = SignupPage(driver)

    signup.click_signup_menu()


@when("user enters signup username")
def enter_signup_username(driver):

    signup = SignupPage(driver)

    username = (
        fake.user_name() +
        str(random.randint(1000, 9999))
    )

    password = "test@123"

    # Store data in json
    user_data = {
        "username": username,
        "password": password
    }

    with open("data/users.json", "w") as file:
        json.dump(user_data, file, indent=4)

    signup.enter_username(username)


@when("user enters signup password")
def enter_signup_password(driver):

    signup = SignupPage(driver)

    with open("data/users.json") as file:
        data = json.load(file)

    signup.enter_password(data["password"])


@when("user clicks signup button")
def click_signup_button(driver):

    signup = SignupPage(driver)

    signup.click_signup_button()


@then("signup should be successful")
def verify_signup(driver):

    signup = SignupPage(driver)

    alert_text = signup.wait_for_alert_and_accept()

    assert "Sign up successful" in alert_text