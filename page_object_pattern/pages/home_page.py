# -*- coding: utf-8 -*-
from base_page import BasePage
from locators import HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    """
    Klasa Strony Głównej
    """
    def _verify_page(self):
        """Weryfikacja strony"""
        # Weryfikcacj tytułu strony
        assert "Oficjalna strona Wizz Air" in self.driver.title
        # Czekam aż będzie można kliknąć przycisk ZALOGUJ
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(HomePageLocators.ZALOGUJ_BTN))



    def click_zaloguj_button(self):
        """Kliknięcie w przycisk ZALOGUJ"""
        el = self.driver.find_element(*HomePageLocators.ZALOGUJ_BTN)
        el.click()
