from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    cardTitle = (By.XPATH, "//h4[@class='card-title']/a")
    # driver.find_elements_by_xpath("//h4[@class='card-title']/a")

    # picButton = (By.XPATH, "parent::h4/parent::div/parent::div/div[2]/button")
    # parent::h4/parent::div/parent::div/div[2]/button

    listStruk = (By.XPATH, "//h4[@class='media-heading']/a")

    checkOutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    confirmButton = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    # def pickButtonClick(self):
    #     return self.driver.find_element(*CheckOutPage.picButton)
    # Gak digunain soalnya dia naik keatas parent

    def checkOutClick(self):
        return self.driver.find_element(*CheckOutPage.checkOutButton)

    def getListStruk(self):
        return self.driver.find_elements(*CheckOutPage.listStruk)

    def confirmClick(self):
        self.driver.find_element(*CheckOutPage.confirmButton).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage