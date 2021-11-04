from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Test_case1(BaseClass):


    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)

        checkOutPage = homePage.shopButton()
        # self.driver.find_element_by_link_text("Shop").click()
        # checkOutPage = CheckOutPage(self.driver) Ini gak diperluin karena dah masuk ke method di hompage

        listHp = checkOutPage.getCardTitles()
        log.info("Mengambil semua card title")
        daftarBelanja = []

        for cari in listHp:
            # log.info(cari.text)
            if cari.text == "Blackberry":
                cari.find_element_by_xpath("parent::h4/parent::div/parent::div/div[2]/button").click()
                daftarBelanja.append(cari.text)
                break

        print(daftarBelanja)
        checkOutPage.checkOutClick().click()
        # self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()

        listStruk = []
        daftarStruk = []

        listStruk = checkOutPage.getListStruk()
        for struk in listStruk:
            daftarStruk.append(struk.text)

        print(daftarStruk)
        assert daftarStruk == daftarBelanja

        confirmPage = checkOutPage.confirmClick()


        eWait = WebDriverWait(self.driver, 3)
        eWait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[class*='validate']")))
        # self.driver.find_element_by_css_selector("input[class*='validate']").send_keys("Ind")
        log.info("Menginput nama negara")
        confirmPage.doSearch().send_keys("Ind")

        self.verivyLinkPresence("Indonesia")
        # Waitnya ditaro di baseclass
        listSuges = confirmPage.selectCities()

        for negara in listSuges:
            if negara.text == "Indonesia":
                negara.click()
                break

        confirmPage.doSubmit().click()
        Sukses = confirmPage.inspectSuccess().text
        log.info("teks yang keluar pada aplikasi adalah "+ Sukses)
        assert "Success" in Sukses

        self.driver.get_screenshot_as_file("coba.png")