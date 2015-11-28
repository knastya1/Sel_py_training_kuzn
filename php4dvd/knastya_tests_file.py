# -*- coding: utf-8 -*-

from conftest import app
from model.user import User
from model.movie import Movie
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *

def do_add_corr_movie(app):
        app.go_to_home_page()
        app.do_login(User.Admin())
        assert app.is_logged_in()
#        app.go_to_main_page()
        app.click_add_movie_btn()
        assert app.is_addmovie_page()
        app.fill_movie_data_and_submit(Movie.CorrectData())
        assert app.movie_is_shown()



def test_login(app):
        app.go_to_home_page()
        app.do_login(User.Admin())
        assert app.is_logged_in()

def test_add_movie_corr(app):
        do_add_corr_movie(app)

def test_add_movie_not_corr(app):
        app.go_to_home_page()
        app.do_login(User.Admin())
        assert app.is_logged_in()
        app.click_add_movie_btn()
        assert app.is_addmovie_page()
        app.fill_movie_data_and_submit(Movie.UncorrectData())
        assert app.movie_is_not_added()

def test_remove_movie(app):
        do_add_corr_movie(app)
        app.go_to_main_page()
        app.go_edit_movie(Movie.CorrectData().title)
        assert app.movie_is_shown()
        app.remove_movie()
        assert app.movie_is_removed()



def test_find_movies(app):
        app.go_to_home_page()
        app.do_login( User.Admin())
        assert app.is_logged_in()
        app.search_movie_by_title("1234567890!@#$%^&*()_")
        assert app.no_movie()
        app.search_movie_by_title(Movie.CorrectData().title)
        assert app.is_movie(Movie.CorrectData().title)






