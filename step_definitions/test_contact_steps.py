from pytest_bdd import scenarios, given, when, then, parsers

from pages.contact_page import ContactPage


scenarios("../features/contact.feature")


@given("user clicks contact menu")
def click_contact(driver):

    contact = ContactPage(driver)

    contact.click_contact_menu()


@when(parsers.parse(
    'user enters contact email "{email}"'
))
def enter_email(driver, email):

    contact = ContactPage(driver)

    contact.enter_email(email)


@when(parsers.parse(
    'user enters contact name "{name}"'
))
def enter_name(driver, name):

    contact = ContactPage(driver)

    contact.enter_name(name)


@when(parsers.parse(
    'user enters message "{message}"'
))
def enter_message(driver, message):

    contact = ContactPage(driver)

    contact.enter_message(message)


@when("user clicks send message button")
def send_message(driver):

    contact = ContactPage(driver)

    contact.click_send_message()


@then("contact message should be sent successfully")
def verify_contact(driver):

    contact = ContactPage(driver)

    alert_text = (
        contact.wait_for_alert_and_accept()
    )

    assert "Thanks" in alert_text