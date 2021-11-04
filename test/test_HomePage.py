import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass

class TestHomePage(BaseClass):

    def test_FormSubmission(self, getData):
        homePage = HomePage(self.driver)
        homePage.fillName().send_keys(getData["fristname"])
        homePage.fillEmail().send_keys(getData["email"])
        homePage.fillPass().send_keys("12345")
        homePage.doCheck().click()
        self.selectOptionByText(homePage.pickGender(),getData["gender"])
        homePage.doSubmit().click()
        message = homePage.inspectSuccesMsg().text
        assert "success" in message
        print(message)
        self.driver.refresh()
    #     kita refresh biar dara yang pertama hilang dulu


    @pytest.fixture(params=HomePageData.test_HomePage_Data)
    def getData(self, request):
        return request.param
#     Disini kita test 2x dengan 2 data yang berbeda

