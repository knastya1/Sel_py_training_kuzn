# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *

import unittest, time, re

class KnastyaTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.wait = WebDriverWait(self.driver, 10)


    def do_login(self, login, passw):
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(login)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(passw)
        driver.find_element_by_name("submit").click()
        driver.find_element_by_css_selector("nav")

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True



    def test_login(self):
        self.do_login("admin", "admin")

    def test_add_film_corr(self):
        self.do_login("admin", "admin")
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/#!/sort/name%20asc/")
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_name("imdbid").clear()
        driver.find_element_by_name("imdbid").send_keys("1234567")
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("Horrow Story")
        driver.find_element_by_name("year").clear()
        driver.find_element_by_name("year").send_keys("1988")
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("!")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_css_selector("div#movie div[class='maininfo_full']")

    def test_add_film_not_corr(self):
        self.do_login("admin", "admin")
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/#!/sort/name%20asc/")
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_id("imdbsearchform")
        driver.find_element_by_name("imdbid").clear()
        driver.find_element_by_name("imdbid").send_keys("12345678")
        driver.find_element_by_name("name").clear()
#        driver.find_element_by_name("name").send_keys("Horrow Story")
        driver.find_element_by_name("year").clear()
        driver.find_element_by_name("year").send_keys("1988")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_name("name").is_selected()
        driver.find_element_by_css_selector("label.error").is_displayed()

    def test_remove_film(self):
        self.do_login("admin", "admin")
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/#!/sort/name%20asc/")
        driver.find_element_by_css_selector("div#results div[title='Horrow Story']").click()
        driver.find_element_by_css_selector("img[alt=\"Remove\"]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to remove this[\s\S]$")
        driver.find_element_by_css_selector("nav")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
    


if __name__ == "__main__":
    unittest.main()