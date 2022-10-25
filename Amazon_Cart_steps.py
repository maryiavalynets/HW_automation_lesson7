from selenium.webdriver.common.by import By
from behave import given, when, then

PRODUCT_NAME = (By.CSS_SELECTOR, "#sc-active-cart li")
PRODUCT_QUANTITY = (By.CSS_SELECTOR, "span[class='a-dropdown-prompt']")

@then('The Amazon Cart is empty')
def cart_is_empty(context):

    #expected_result = "Your Amazon Cart is empty"
    #actual_result = context.driver.find_element(By.XPATH, "//*[contains(text(),'Your Amazon Cart is empty')]").text
    #assert expected_result == actual_result, f'Error! Expected {expected_result} but got {actual_result}.'
    context.app.cart_page.cart_is_empty()



@then('The Amazon Cart has the {search_result} in quantity 2')
def cart_has_product(context, search_result):

    actual_name = context.driver.find_element(*PRODUCT_NAME).text
    actual_quantity = context.driver.find_element(*PRODUCT_QUANTITY).text

    assert context.product_name[30] in actual_name, f'Error! The cart does not have the {context.product_name}.'
    assert "2" == actual_quantity, f'Error! Expected quantity "2", but got {actual_quantity}.'

