from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    shop = (By.LINK_TEXT, "Shop")
    # Diatas ini kayak dia ngasih tau shop dimana
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    passWord = (By.ID, "exampleInputPassword1")
    check = (By.ID, "exampleCheck1")
    dropGender = (By.ID, "exampleFormControlSelect1")
    successMsg = (By.CSS_SELECTOR, "div[class *='alert-success'")
    submitButton = (By.XPATH, "//input[@value='Submit']")


    def __init__(self, driver):
        self.driver = driver
    # Drivernya dimasukkin ke testcase dan dimasukkin kesini biar di share di local objek

    def shopButton(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage
        # nah disini tinggal dipanggil doang

    def fillName(self):
        return self.driver.find_element(*HomePage.name)

    def fillEmail(self):
        return self.driver.find_element(*HomePage.email)

    def fillPass(self):
        return self.driver.find_element(*HomePage.passWord)

    def doCheck(self):
        return self.driver.find_element(*HomePage.check)

    def pickGender(self):
        return self.driver.find_element(*HomePage.dropGender)

    def doSubmit(self):
        return self.driver.find_element(*HomePage.submitButton)

    def inspectSuccesMsg(self):
        return self.driver.find_element(*HomePage.successMsg)