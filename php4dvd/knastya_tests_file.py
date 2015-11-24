# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.common.exceptions import *
from knastya_selen_fixture import app
import time
from model.user import User
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.common.by import By





def do_login(driver, user):
        driver.get("http://localhost/php4dvd/")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(user.username)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(user.password)
        driver.find_element_by_name("submit").click()
        driver.find_element_by_css_selector("nav")

def test_login(app):
    do_login(app.driver, User.Admin())

def test_add_film_corr(app):
        do_login(app.driver, User.Admin())
        app.driver.get("http://localhost/php4dvd/#!/sort/name%20asc/")
        app.driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        app.driver.find_element_by_name("imdbid").clear()
        app.driver.find_element_by_name("imdbid").send_keys("1234567")
        app.driver.find_element_by_name("name").clear()
        app.driver.find_element_by_name("name").send_keys("Horrow Story")
        app.driver.find_element_by_name("year").clear()
        app.driver.find_element_by_name("year").send_keys("1988")
        app.driver.find_element_by_name("notes").clear()
        app.driver.find_element_by_name("notes").send_keys("!")
        app.driver.find_element_by_id("submit").click()
        app.driver.find_element_by_css_selector("div#movie div[class='maininfo_full']")

def test_add_film_not_corr(app):
        do_login(app.driver, User.Admin())
        app.driver.get("http://localhost/php4dvd/#!/sort/name%20asc/")
        app.driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        app.driver.find_element_by_id("imdbsearchform")
        app.driver.find_element_by_name("imdbid").clear()
        app.driver.find_element_by_name("imdbid").send_keys("12345678")
        app.driver.find_element_by_name("name").clear()
#        driver.find_element_by_name("name").send_keys("Horrow Story")
        app.driver.find_element_by_name("year").clear()
        app.driver.find_element_by_name("year").send_keys("1988")
        app.driver.find_element_by_id("submit").click()
        app.driver.find_element_by_name("name").is_selected()
        app.driver.find_element_by_css_selector("label.error").is_displayed()

def test_remove_film(app):
        do_login(app.driver, User.Admin())
        app.driver.get("http://localhost/php4dvd/#!/sort/name%20asc/")
        app.driver.find_element_by_css_selector("div#results div[title='Horrow Story']").click()
        app.driver.find_element_by_css_selector("img[alt=\"Remove\"]").click()
        assertRegexpMatches(close_alert_and_get_its_text(), r"^Are you sure you want to remove this[\s\S]$")
        app.driver.find_element_by_css_selector("nav")



def test_find_movies(app):
        do_login(app.driver, User.Admin())
        knwait = WebDriverWait(app.driver, 30)
        app.driver.find_element_by_id("q").clear()
        app.driver.find_element_by_id("q").send_keys("1234567890!@#$%^&*()_"+ Keys.RETURN)
        app.wait.until(presence_of_element_located((By.XPATH,"//div[@id='results']/div[.='No movies where found.']" )))
        app.driver.find_element_by_id("q").clear()
        app.driver.find_element_by_id("q").send_keys("Happy Story"+ Keys.RETURN)
        app.wait.until(presence_of_element_located((By.XPATH,"//div[.='Happy Story']")))

#        time.sleep(2)
#        assert len(driver.find_elements_by_css_selector("div#results a"))==0

