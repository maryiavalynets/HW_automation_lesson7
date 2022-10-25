from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):

    CART_EMPTY_TEXT = (By.XPATH, "//*[contains(text(),'Your Amazon Cart is empty')]")

    def cart_is_empty(self):
        expected_text = "Your Amazon Cart is empty"
        actual_text = self.driver.find_element(*self.CART_EMPTY_TEXT).text

        assert expected_text == actual_text, f'Error! Expected {expected_text} but got {actual_text}.'
