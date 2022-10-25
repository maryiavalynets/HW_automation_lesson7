from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    ORDER_BTN = (By.ID,'nav-orders')
    CART_ICON = (By.ID,'nav-cart')

    def open_main(self):
        self.driver.get('https://www.amazon.com/')

    def click_order_btn(self):
        self.driver.find_element(*self.ORDER_BTN).click()

    def click_cart_icon(self):
        self.driver.find_element(*self.CART_ICON).click()