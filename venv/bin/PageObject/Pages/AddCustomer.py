from selenium.webdriver.common.alert import Alert

from selenium.webdriver.support.ui import Select

from Locators import MainPageLocators


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class ManagerPage(BasePage):

    def add_customer(self):
        element = self.driver.find_element(*MainPageLocators.add_customer_button)
        element.click()

    def add_username(self):
        element = self.driver.find_element(*MainPageLocators.first_name_textbox)
        element.clear()
        element.send_keys("Sebas")

    def add_last_name(self):
        element = self.driver.find_element(*MainPageLocators.last_name_textbox)
        element.clear()
        element.send_keys("Leal")

    def add_post_code(self):
        element = self.driver.find_element(*MainPageLocators.post_code_textbox)
        element.clear()
        element.send_keys("5555555")

    def submit(self):
        element = self.driver.find_element(*MainPageLocators.submit_button)
        element.click()

    def customer_added_alert(self):
        self.driver.switch_to.alert
        Alert(self.driver).accept()

    def open_account(self):
        element = self.driver.find_element(*MainPageLocators.customer_button)
        element.click()

    def select_user(self):
        select = Select(self.driver.find_element(*MainPageLocators.select_user))
        select.select_by_visible_text("Sebas Leal")

    def select_currency(self):
        select = Select(self.driver.find_element(*MainPageLocators.select_currency))
        select.select_by_visible_text("Dollar")

    def submit_button(self):
        element = self.driver.find_element(*MainPageLocators.open_account_submit_button)
        element.click()
