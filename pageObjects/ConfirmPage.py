from selenium.webdriver.common.by import By

class ConfirmPage:

    searchCity = (By.CSS_SELECTOR, "input[class*='validate']")
    # input[class*='validate']

    litCities = (By.LINK_TEXT, "Indonesia")

    submitButton = (By.CSS_SELECTOR, "input[type='submit']")

    success = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def __init__(self, driver):
        self.driver = driver


    def doSearch(self):
        return self.driver.find_element(*ConfirmPage.searchCity)

    def selectCities(self):
        return self.driver.find_elements(*ConfirmPage.litCities)

    def doSubmit(self):
        return self.driver.find_element(*ConfirmPage.submitButton)

    def inspectSuccess(self):
        return self.driver.find_element(*ConfirmPage.success)

