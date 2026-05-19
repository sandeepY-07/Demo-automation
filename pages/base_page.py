import time

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):

        self.driver = driver

    def click_element(self, locator):

        element = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.element_to_be_clickable(locator)
        )

        time.sleep(1)

        element.click()

        time.sleep(1)

    def enter_text(self, locator, text):

        element = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()

        time.sleep(1)

        element.send_keys(text)

        time.sleep(1)

    def get_text(self, locator):

        return WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(locator)
        ).text

    def wait_for_alert_and_accept(self):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.alert_is_present()
        )

        alert = self.driver.switch_to.alert

        text = alert.text

        time.sleep(1)

        alert.accept()

        time.sleep(1)

        return text