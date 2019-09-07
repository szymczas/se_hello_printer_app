#-*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class HomePageLocators():
    ZALOGUJ_BTN = (By.XPATH, "//button[@data-test='navigation-menu-signin']")

class LoginPageLocators():
    REJESTRACJA_BTN = (By.XPATH, "//button[text()='Rejestracja']")

class RegistrationPageLocators():
    NAME_FIELD = (By.XPATH, "//input[@name='firstName']")
    SURNAME_FIELD = (By.XPATH, "//input[@data-test='registrationmodal-last-name-input']" )
    GENDER_MALE = (By.XPATH, "//label[@for='register-gender-male']")
    GENDER_FEMALE = (By.XPATH, "//label[@for='register-gender-female']")
