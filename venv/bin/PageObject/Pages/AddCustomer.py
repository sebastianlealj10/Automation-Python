from Locators import AddCustomerLocators


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class AddCustomerPage(BasePage):

    def add_customer(self):
        element = self.driver.find_element(*AddCustomerLocators.add_customer_button)
        element.click()

    def add_username(self):
        element = self.driver.find_element(*AddCustomerLocators.first_name_textbox)
        element.clear()
        element.send_keys("Sebas")

    def add_last_name(self):
        element = self.driver.find_element(*AddCustomerLocators.last_name_textbox)
        element.clear()
        element.send_keys("Leal")

    def add_post_code(self):
        element = self.driver.find_element(*AddCustomerLocators.post_code_textbox)
        element.clear()
        element.send_keys("5555555")

    def submit(self):
        element = self.driver.find_element(*AddCustomerLocators.submit_button)
        element.click()
