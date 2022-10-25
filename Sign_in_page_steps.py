from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Sign in page shows')
def verify_sign_in_shows(context):
    #expected_resul = "Sign in"
    #actual_result = context.driver.find_element(By.XPATH, "//*[contains(text(),'Sign in')]").text
    #assert expected_resul == actual_result, f'Error! Expected {expected_resul} , but got {actual_result}.'
    #assert context.driver.find_element(By.ID, 'ap_email').is_displayed(), f'Error.Email field is not show.'
    context.app.sign_in_page.verify_sign_in_shows()
