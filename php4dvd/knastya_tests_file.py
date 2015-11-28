# -*- coding: utf-8 -*-

from conftest import app
from model.user import User
from model.movie import Movie
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *



def test_login(app):
        app.go_to_home_page()
        app.do_login(User.Admin())
        assert app.is_logged_in()

def test_add_film_corr(app):
        app.go_to_home_page()
        app.do_login(User.Admin())
        assert app.is_logged_in()
#        app.go_to_main_page()
        app.click_add_movie_btn()
        assert app.is_addmovie_page()
        app.fill_movie_data_and_submit(Movie.CorrectData())
        assert app.movie_is_shown()

def test_add_film_not_corr(app):
        app.go_to_home_page()
        app.do_login(User.Admin())
        assert app.is_logged_in()
#        app.go_to_main_page()
        app.click_add_movie_btn()
        assert app.is_addmovie_page()
        app.fill_movie_data_and_submit(Movie.UncorrectData())
        assert app.movie_is_not_added()

def test_remove_movie(app):
        test_add_film_corr(app)
        app.go_to_main_page()
        app.go_edit_movie(Movie.CorrectData().title)
        assert app.movie_is_shown()
        app.remove_movie()
        assert app.movie_is_removed()



def test_find_movies(app):
        app.go_to_home_page()
        app.do_login( User.Admin())
        assert app.is_logged_in()

        app.driver.find_element_by_id("q").clear()
        app.driver.find_element_by_id("q").send_keys("Happy Story"+ Keys.RETURN)
        app.wait.until(presence_of_element_located((By.XPATH,"//div[.='Happy Story']")))




