# -*- coding: utf-8 -*-

class BasePage():
    """
    Klasa bazowa, z której będą
    korzystały wszystkie strony
    """
    # Konstruktor
    def __init__(self, driver):
        self.driver = driver
        self._verify_page()

    # Weryfikacja strony
    def _verify_page(self):
        return
