# -*- coding: utf-8 -*-
from pages.base_page import BasePage
from locators import RegistrationPageLocators

class RegistrationPage(BasePage):
    """
    Klasa Strony Rejestracji
    """

    def fill_name_field(self,name):
        el = self.driver.find_element(*RegistrationPageLocators.NAME_FIELD)
        el.send_keys(name)

    def fill_surname_field(self, surname):
        el = self.driver.find_element(*RegistrationPageLocators.SURNAME_FIELD)
        el.send_keys(surname)


    def check_if_no_error_notice_is_presented(self):
        pass

    def choose_gender(self, gender):
        if gender == "male":
            el = self.driver.find_element(*RegistrationPageLocators.GENDER_MALE)
            el.click()
            el.click()
        else:
            f = el = self.driver.find_element(*RegistrationPageLocators.GENDER_FEMALE)
        f.click()


        #KKOLANSK github
