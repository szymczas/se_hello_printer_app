#-*- coding: utf-8 -*-
# Import bibliotek
from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# ZMIENNE UŻYTE W PRZYPADKU TESTOWYM
valid_name="Natalia"
gender = "female"
Second_name = "Kowalska"
phone_number = "48798798798"
test_email = "testowymailgmail.com"
password = "Kwiatek-123"
test_country = "ploska"
wrong_password = "Kwiatekaaa"
right_email = "testowymail@gmail.com"
no_name = ""
#blad = u"Nieprawidłowy adres e-mail"

# Rejestracja nowego użytkownika na stronie wizzair.com
class WizzairRegistration(unittest.TestCase):
    def setUp(self):
        # Stworz nowy sterownik do Chrome
        self.driver = webdriver.Chrome()
        # Maksymalizuj okno
        self.driver.maximize_window()
        # Otworz strone wizzair
        self.driver.get("https://wizzair.com/pl-pl/main-page#/")

    # Instrukcje, które wykonają się po każdym teście
    ## WARUNKI KOŃCOWE - SPRZĄTANIE PO TEŚCIE##
    def tearDown(self):
        # Wylacz przegladarke
        self.driver.quit()

    # Testy zaczynają się od słowa 'test_'..
    ## PRZYPADKI TESTOWE ##

    # sprawdzam poprawny formularz, nie powinno byc bledow
    def test_correct_registration(self):
        ## KROKI ##
        driver = self.driver
        #zaloguj_btn = self.driver.find_element_by_css_selector(
        #"#app > header > div.header__inner > div > nav > ul > li:nth-child(7) > button"
        #//*[@id="app"]/header/div[1]/div/nav/ul/li[7]/button)
        #zaloguj_btn = self.driver.find_element_by_xpath(
        #"//button[@data-test='navigation-menu-signin']")
        # 1. Kliknij w prawym górnym rogu ZALOGUJ SIĘ
        zaloguj_btn = WebDriverWait(driver, 6).until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@data-test='navigation-menu-signin']")))
        zaloguj_btn.click()
        # 2. Wybierz rejestracja
        rejestracja_btn = self.driver.find_element_by_xpath(
        "//button[text()='Rejestracja']")
        rejestracja_btn.click()
        # 3. Wprowadź imię
        imie = self.driver.find_element_by_xpath( "//input[@name='firstName']")
        imie.send_keys(valid_name)
        # 4. Wprowadź nazwisko
        nazwisko = self.driver.find_element_by_xpath(
        "//input[@data-test='registrationmodal-last-name-input']"
        )
        nazwisko.send_keys(Second_name)
        # 5. Wybierz płeć
        if gender == "male":
            m = driver.find_element_by_xpath(
            "//label[@for='register-gender-male']")
            imie.click()
            m.click()
        else:
            f = m = driver.find_element_by_xpath(
            "//label[@for='register-gender-female']")
            f.click()
        # 6. Wprowadź nr tel
        telefon = driver.find_element_by_name("mobilePhone")
        telefon.send_keys(phone_number)
        # 7. Wprowadź błędny adres email - brak znaku @
        email = driver.find_element_by_xpath(
        "//input[@data-test='booking-register-email']")
        email.send_keys(right_email)
        # 8. Wprowadź hasło
        haslo = driver.find_element_by_xpath(
        "//input[@data-test='booking-register-password']")
        haslo.send_keys(password)
        # 9. Wybierz kraj
        narodowosc = driver.find_element_by_xpath(
        "//input[@data-test='booking-register-country']")
        #narodowosc.send_keys(test_country)
        narodowosc.click()
        narodowosc_wybierz = driver.find_element_by_xpath(
        "//label[@data-test='booking-register-country-label'][164]")
        narodowosc_wybierz.location_once_scrolled_into_view
        narodowosc_wybierz.click()
        # 10. Akceptuj politykę prywatności
        Regulamin = driver.find_element_by_xpath(
        '//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]'
        )
        Regulamin.click()
        # 11. Kliknij przycisk ZAREJESTRUJ SIĘ"
        Zarejestruj_btn = driver.find_element_by_xpath(
        '//button[@data-test="booking-register-submit"]')
        #Zarejestruj_btn.click()
        ###WYNIK OCZEKIWANY - SPRAWDZENIE###
        # 1. Przycisk "zarejestruj się" jest aktywny
        assert Zarejestruj_btn.is_enabled()
        # 2. Użytkownik dostaje informację, że wprowadzony e-mail jest niepoprawny
        # Znalezienie wszystkich błędów
        bledy = driver.find_elements_by_xpath('//span[@class="rf-input__error__message"]/span')
        assert len(bledy) == 14
        widoczne_bledy = []
        # Dodanie widocznych błędów do listy
        for blad in bledy:
            if blad.is_displayed():
                widoczne_bledy.append(blad)
        # Sprawdzenie czy jest widoczny tylko jeden błąd
        if len(widoczne_bledy) == 0:
            pass
        else:
            blad_text = widoczne_bledy[0].get_attribute("innerText")
            print (blad_text)
        #Sprawdzenie poprawności widocznego błędu
        #self.assertEqual(blad_text, u"Nieprawidłowy adres e-mail")
        time.sleep(1)


    # Rejestracja nowego użytkownika używając adresu
    # email - dane niepoprawne (niekompletny email brak @)
    def test_wrong_email(self):
        ## KROKI ##
        driver = self.driver
        #zaloguj_btn = self.driver.find_element_by_css_selector(
        #"#app > header > div.header__inner > div > nav > ul > li:nth-child(7) > button"
        #//*[@id="app"]/header/div[1]/div/nav/ul/li[7]/button)
        #zaloguj_btn = self.driver.find_element_by_xpath(
        #"//button[@data-test='navigation-menu-signin']")
        # 1. Kliknij w prawym górnym rogu ZALOGUJ SIĘ
        zaloguj_btn = WebDriverWait(driver, 6).until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@data-test='navigation-menu-signin']")))
        zaloguj_btn.click()
        # 2. Wybierz rejestracja
        rejestracja_btn = self.driver.find_element_by_xpath(
        "//button[text()='Rejestracja']")
        rejestracja_btn.click()
        # 3. Wprowadź imię
        imie = self.driver.find_element_by_xpath( "//input[@name='firstName']")
        imie.send_keys(valid_name)
        # 4. Wprowadź nazwisko
        nazwisko = self.driver.find_element_by_xpath(
        "//input[@data-test='registrationmodal-last-name-input']"
        )
        nazwisko.send_keys(Second_name)
        # 5. Wybierz płeć
        if gender == "male":
            m = driver.find_element_by_xpath(
            "//label[@for='register-gender-male']")
            imie.click()
            m.click()
        else:
            f = m = driver.find_element_by_xpath(
            "//label[@for='register-gender-female']")
            f.click()
        # 6. Wprowadź nr tel
        telefon = driver.find_element_by_name("mobilePhone")
        telefon.send_keys(phone_number)
        # 7. Wprowadź błędny adres email - brak znaku @
        email = driver.find_element_by_xpath(
        "//input[@data-test='booking-register-email']")
        email.send_keys(test_email)
        # 8. Wprowadź hasło
        haslo = driver.find_element_by_xpath(
        "//input[@data-test='booking-register-password']")
        haslo.send_keys(password)
        # 9. Wybierz kraj
        narodowosc = driver.find_element_by_xpath(
        "//input[@data-test='booking-register-country']")
        #narodowosc.send_keys(test_country)
        narodowosc.click()
        narodowosc_wybierz = driver.find_element_by_xpath(
        "//label[@data-test='booking-register-country-label'][164]")
        narodowosc_wybierz.location_once_scrolled_into_view
        narodowosc_wybierz.click()
        # 10. Akceptuj politykę prywatności
        Regulamin = driver.find_element_by_xpath(
        '//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]'
        )
        Regulamin.click()
        # 11. Kliknij przycisk ZAREJESTRUJ SIĘ"
        Zarejestruj_btn = driver.find_element_by_xpath(
        '//button[@data-test="booking-register-submit"]')
        Zarejestruj_btn.click()
        ###WYNIK OCZEKIWANY - SPRAWDZENIE###
        # 1. Przycisk "zarejestruj się" jest aktywny
        assert Zarejestruj_btn.is_enabled()
        # 2. Użytkownik dostaje informację, że wprowadzony e-mail jest niepoprawny
        # Znalezienie wszystkich błędów
        bledy = driver.find_elements_by_xpath('//span[@class="rf-input__error__message"]/span')
        assert len(bledy) == 14
        widoczne_bledy = []
        # Dodanie widocznych błędów do listy
        for blad in bledy:
            if blad.is_displayed():
                widoczne_bledy.append(blad)
        # Sprawdzenie czy jest widoczny tylko jeden błąd
        len(widoczne_bledy) == 1
        blad_text = widoczne_bledy[0].get_attribute("innerText")
        # print (blad_text)
        #Sprawdzenie poprawności widocznego błędu
        self.assertEqual(blad_text, u"Nieprawidłowy adres e-mail")
        time.sleep(1)

    # Rejestracja nowego użytkownika używając niepoprawnego hasła
    def test_wrong_password(self):
        ## KROKI ##
        driver = self.driver
        #zaloguj_btn = self.driver.find_element_by_css_selector(
        #"#app > header > div.header__inner > div > nav > ul > li:nth-child(7) > button"
        #//*[@id="app"]/header/div[1]/div/nav/ul/li[7]/button)
        #zaloguj_btn = self.driver.find_element_by_xpath(
        #"//button[@data-test='navigation-menu-signin']")
        # 1. Kliknij w prawym górnym rogu ZALOGUJ SIĘ
        zaloguj_btn = WebDriverWait(driver, 6).until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@data-test='navigation-menu-signin']")))
        zaloguj_btn.click()
        # 2. Wybierz rejestracja
        rejestracja_btn = self.driver.find_element_by_xpath(
        "//button[text()='Rejestracja']")
        rejestracja_btn.click()
        # 3. Wprowadź imię
        imie = self.driver.find_element_by_xpath( "//input[@name='firstName']")
        imie.send_keys(valid_name)
        # 4. Wprowadź nazwisko
        nazwisko = self.driver.find_element_by_xpath(
        "//input[@data-test='registrationmodal-last-name-input']"
        )
        nazwisko.send_keys(Second_name)
        # 5. Wybierz płeć
        if gender == "male":
            m = driver.find_element_by_xpath(
            "//label[@for='register-gender-male']")
            imie.click()
            m.click()
        else:
            f = m = driver.find_element_by_xpath(
            "//label[@for='register-gender-female']")
            f.click()
        # 6. Wprowadź nr tel
        telefon = driver.find_element_by_name("mobilePhone")
        telefon.send_keys(phone_number)
        # 7. Wprowadź adres email
        email = driver.find_element_by_xpath(
        "//input[@data-test='booking-register-email']")
        email.send_keys(right_email)
        # 8. Wprowadź nieprawidłowe hasło
        haslo = driver.find_element_by_xpath(
        "//input[@data-test='booking-register-password']")
        haslo.send_keys(wrong_password)
        # 9. Wybierz kraj
        narodowosc = driver.find_element_by_xpath(
        "//input[@data-test='booking-register-country']")
        #narodowosc.send_keys(test_country)
        narodowosc.click()
        narodowosc_wybierz = driver.find_element_by_xpath(
        "//label[@data-test='booking-register-country-label'][164]")
        narodowosc_wybierz.location_once_scrolled_into_view
        narodowosc_wybierz.click()
        # 10. Akceptuj politykę prywatności
        Regulamin = driver.find_element_by_xpath(
        '//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]'
        )
        Regulamin.click()
        # 11. Kliknij przycisk ZAREJESTRUJ SIĘ"
        Zarejestruj_btn = driver.find_element_by_xpath(
        '//button[@data-test="booking-register-submit"]')
        Zarejestruj_btn.click()
        ###WYNIK OCZEKIWANY - SPRAWDZENIE###
        # 1. Przycisk "zarejestruj się" jest aktywny
        assert Zarejestruj_btn.is_enabled()
        # 2. Użytkownik dostaje informację, że wprowadzony e-mail jest niepoprawny
        # Znalezienie wszystkich błędów
        bledy = driver.find_elements_by_xpath('//span[@class="rf-input__error__message"]/span')
        assert len(bledy) == 14
        widoczne_bledy = []
        # Dodanie widocznych błędów do listy
        for blad in bledy:
            if blad.is_displayed():
                widoczne_bledy.append(blad)
        # Sprawdzenie czy jest widoczny tylko jeden błąd
        len(widoczne_bledy) == 1
        blad_text = widoczne_bledy[0].get_attribute("innerText")
        # print (blad_text)
        #Sprawdzenie poprawności widocznego błędu
        self.assertEqual(blad_text, u"Wpisz hasło")
        time.sleep(1)

    # Rejestracja nowego użytkownika bez wpisanego imienia
    def test_no_name(self):
        ## KROKI ##
        driver = self.driver
        #zaloguj_btn = self.driver.find_element_by_css_selector(
        #"#app > header > div.header__inner > div > nav > ul > li:nth-child(7) > button"
        #//*[@id="app"]/header/div[1]/div/nav/ul/li[7]/button)
        #zaloguj_btn = self.driver.find_element_by_xpath(
        #"//button[@data-test='navigation-menu-signin']")
        # 1. Kliknij w prawym górnym rogu ZALOGUJ SIĘ
        zaloguj_btn = WebDriverWait(driver, 6).until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@data-test='navigation-menu-signin']")))
        zaloguj_btn.click()
        # 2. Wybierz rejestracja
        rejestracja_btn = self.driver.find_element_by_xpath(
        "//button[text()='Rejestracja']")
        rejestracja_btn.click()
        # 3. Nie wprowadzaj imienia
        imie = self.driver.find_element_by_xpath( "//input[@name='firstName']")
        imie.send_keys(no_name)
        # 4. Wprowadź nazwisko
        nazwisko = self.driver.find_element_by_xpath(
        "//input[@data-test='registrationmodal-last-name-input']"
        )
        nazwisko.send_keys(Second_name)
        # 5. Wybierz płeć
        if gender == "male":
            m = driver.find_element_by_xpath(
            "//label[@for='register-gender-male']")
            imie.click()
            m.click()
        else:
            f = m = driver.find_element_by_xpath(
            "//label[@for='register-gender-female']")
            f.click()
        # 6. Wprowadź nr tel
        telefon = driver.find_element_by_name("mobilePhone")
        telefon.send_keys(phone_number)
        # 7. Wprowadź adres email
        email = driver.find_element_by_xpath(
        "//input[@data-test='booking-register-email']")
        email.send_keys(right_email)
        # 8. Wprowadź prawidłowe hasło
        haslo = driver.find_element_by_xpath(
        "//input[@data-test='booking-register-password']")
        haslo.send_keys(password)
        # 9. Wybierz kraj
        narodowosc = driver.find_element_by_xpath(
        "//input[@data-test='booking-register-country']")
        #narodowosc.send_keys(test_country)
        narodowosc.click()
        narodowosc_wybierz = driver.find_element_by_xpath(
        "//label[@data-test='booking-register-country-label'][164]")
        narodowosc_wybierz.location_once_scrolled_into_view
        narodowosc_wybierz.click()
        # 10. Akceptuj politykę prywatności
        Regulamin = driver.find_element_by_xpath(
        '//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]'
        )
        Regulamin.click()
        # 11. Kliknij przycisk ZAREJESTRUJ SIĘ"
        Zarejestruj_btn = driver.find_element_by_xpath(
        '//button[@data-test="booking-register-submit"]')
        Zarejestruj_btn.click()
        ###WYNIK OCZEKIWANY - SPRAWDZENIE###
        # 1. Przycisk "zarejestruj się" jest aktywny
        assert Zarejestruj_btn.is_enabled()
        # 2. Użytkownik dostaje informację, że wprowadzony e-mail jest niepoprawny
        # Znalezienie wszystkich błędów
        bledy = driver.find_elements_by_xpath('//span[@class="rf-input__error__message"]/span')
        assert len(bledy) == 14
        widoczne_bledy = []
        # Dodanie widocznych błędów do listy
        for blad in bledy:
            if blad.is_displayed():
                widoczne_bledy.append(blad)
        # Sprawdzenie czy jest widoczny tylko jeden błąd
        len(widoczne_bledy) == 1
        blad_text = widoczne_bledy[0].get_attribute("innerText")
        #print (blad_text)
        #Sprawdzenie poprawności widocznego błędu
        self.assertEqual(
        blad_text,
        u"Wpisz imię!" + "\n" +
        u"Należy używać tylko liter alfabetu łacińskiego, bez znaków diakrytycznych i specjalnych!")
        time.sleep(1)

    # Rejestracja nowego użytkownika bez wybranego kraju
    def test_wrong_country(self):
        ## KROKI ##
        driver = self.driver
        #zaloguj_btn = self.driver.find_element_by_css_selector(
        #"#app > header > div.header__inner > div > nav > ul > li:nth-child(7) > button"
        #//*[@id="app"]/header/div[1]/div/nav/ul/li[7]/button)
        #zaloguj_btn = self.driver.find_element_by_xpath(
        #"//button[@data-test='navigation-menu-signin']")
        # 1. Kliknij w prawym górnym rogu ZALOGUJ SIĘ
        zaloguj_btn = WebDriverWait(driver, 6).until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@data-test='navigation-menu-signin']")))
        zaloguj_btn.click()
        # 2. Wybierz rejestracja
        rejestracja_btn = self.driver.find_element_by_xpath(
        "//button[text()='Rejestracja']")
        rejestracja_btn.click()
        # 3. Nie wprowadzaj imienia
        imie = self.driver.find_element_by_xpath( "//input[@name='firstName']")
        imie.send_keys(valid_name)
        # 4. Wprowadź nazwisko
        nazwisko = self.driver.find_element_by_xpath(
        "//input[@data-test='registrationmodal-last-name-input']"
        )
        nazwisko.send_keys(Second_name)
        # 5. Wybierz płeć
        if gender == "male":
            m = driver.find_element_by_xpath(
            "//label[@for='register-gender-male']")
            imie.click()
            m.click()
        else:
            f = m = driver.find_element_by_xpath(
            "//label[@for='register-gender-female']")
            f.click()
        # 6. Wprowadź nr tel
        telefon = driver.find_element_by_name("mobilePhone")
        telefon.send_keys(phone_number)
        # 7. Wprowadź adres email
        email = driver.find_element_by_xpath(
        "//input[@data-test='booking-register-email']")
        email.send_keys(right_email)
        # 8. Wprowadź prawidłowe hasło
        haslo = driver.find_element_by_xpath(
        "//input[@data-test='booking-register-password']")
        haslo.send_keys(password)
        # 9. Wybierz kraj
        narodowosc = driver.find_element_by_xpath(
        "//input[@data-test='booking-register-country']")
        narodowosc.send_keys(test_country)
        # 10. Akceptuj politykę prywatności
        Regulamin = driver.find_element_by_xpath(
        '//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]'
        )
        Regulamin.click()
        # 11. Kliknij przycisk ZAREJESTRUJ SIĘ"
        Zarejestruj_btn = driver.find_element_by_xpath(
        '//button[@data-test="booking-register-submit"]')
        Zarejestruj_btn.click()
        ###WYNIK OCZEKIWANY - SPRAWDZENIE###
        # 1. Przycisk "zarejestruj się" jest aktywny
        assert Zarejestruj_btn.is_enabled()
        # 2. Użytkownik dostaje informację, że wprowadzony e-mail jest niepoprawny
        # Znalezienie wszystkich błędów
        bledy = driver.find_elements_by_xpath('//span[@class="rf-input__error__message"]/span')
        assert len(bledy) == 14
        widoczne_bledy = []
        # Dodanie widocznych błędów do listy
        for blad in bledy:
            if blad.is_displayed():
                widoczne_bledy.append(blad)
        # Sprawdzenie czy jest widoczny tylko jeden błąd
        len(widoczne_bledy) == 1
        blad_text = widoczne_bledy[0].get_attribute("innerText")
        #print (blad_text)
        #Sprawdzenie poprawności widocznego błędu
        self.assertEqual(blad_text, u"Ten kraj nie istnieje.")
        time.sleep(3)

if __name__ == '__main__':
    unittest.main(verbosity=2)
