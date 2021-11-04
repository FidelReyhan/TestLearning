import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:


    def verivyLinkPresence(self, text):
        eWait2 = WebDriverWait(self.driver, 10)
        eWait2.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)  # Disini kita select dropdown dari text yang terlihat

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger =logging.getLogger(loggerName)
        # logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        format = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        # disini kita formatnya pertama nampilin waktu runtime
        # kedua itu nampilin level apakah warning, critical, dll
        # Ketiga nampilin nama file yang error
        # terakhir nampilin messagenya

        fileHandler.setFormatter(format)
        # ini memasukkan format ke fileHandler

        logger.addHandler(fileHandler)  # Objek filehandler

        logger.setLevel(logging.INFO)
        return logger
