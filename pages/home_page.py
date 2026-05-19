import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):

    LAPTOPS = (
        By.XPATH,
        "//a[text()='Laptops']"
    )

    PRODUCT = (
        By.XPATH,
        "//a[text()='Sony vaio i5']"
    )

    def click_laptops(self):

        self.click_element(self.LAPTOPS)

        time.sleep(3)

    def click_product(self):

        time.sleep(2)

        self.click_element(self.PRODUCT)

    def get_product_text(self):

        return self.get_text(self.PRODUCT)