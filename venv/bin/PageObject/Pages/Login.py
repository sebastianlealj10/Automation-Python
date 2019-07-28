from Locators import MainPageLocators


##
# class SearchTextElement(BasePageElement):
#  """This class gets the search text from the specified locator"""
#
#    #The locator for search box where search string is entered
#    locator = 'q'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class Login(BasePage):

    def bank_manager_login(self):
        element = self.driver.find_element(*MainPageLocators.bank_manager_login)
        element.click()
