from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    bank_manager_login = (By.CSS_SELECTOR, 'div:last-child > .btn.btn-primary.btn-lg')


class AddCustomerLocators(object):
    add_customer_button = (By.CSS_SELECTOR, '.btn.btn-lg.tab:first-child')
    first_name_textbox = (By.CSS_SELECTOR, "input[ng-model='fName']")
    last_name_textbox = (By.CSS_SELECTOR, "input[ng-model='lName']")
    post_code_textbox = (By.CSS_SELECTOR, "input[ng-model='postCd']")
    submit_button = (By.CSS_SELECTOR, "button[type='submit']")
    customer_button = (By.CSS_SELECTOR, "button[ng-class='btnClass2']")
    select_user = (By.NAME, 'userSelect')
    select_currency = (By.NAME, 'currency')
    open_account_submit_button = (By.CSS_SELECTOR, "button[type='submit']")
