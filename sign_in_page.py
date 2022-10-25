from selenium.webdriver.common.by import By

from pages.base_page import Page

class SignInPage(Page):

    SIGN_IN = (By.XPATH, "//*[contains(text(),'Sign in')]")
    AP_EMAIL = (By.ID, 'ap_email')

    def verify_sign_in_shows(self):
        expected_text = "Sign in"
        actual_text = self.driver.find_element(*self.SIGN_IN).text
        assert expected_text == actual_text, f'Error! Expected {expected_text} , but got {actual_text}.'
        assert self.driver.find_element(*self.AP_EMAIL).is_displayed(), f'Error.Email field is not show.'

