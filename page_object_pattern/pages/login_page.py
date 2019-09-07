# -*- coding: utf-8 -*-
from base_page import BasePage
from locators import LoginPageLocators

class LoginPage(BasePage):
    """
    Klasa Strony Logowania
    """
    def click_rejestracja_button(self):
        """ Kliknięcie w przycisk REJESTRACJA"""
        el = self.driver.find_element(*LoginPageLocators.REJESTRACJA_BTN)
        el.click()
