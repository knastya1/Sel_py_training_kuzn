from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
#from php4dvd.pages.internal_page import InternalPage
from php4dvd.pages.login_page import LoginPage
from php4dvd.pages.main_page import MainPage
from php4dvd.pages.add_movie_page import AddMoviePage
from php4dvd.pages.movie_page import MoviePage
from selenium.webdriver.common.keys import Keys




class Application(object):

    def __init__(self, driver, wait,base_url):
        self.driver = driver
        self.wait=wait
        self.base_url=base_url
        self.login_page = LoginPage(driver, base_url)
        self.main_page = MainPage(driver, base_url)
        self.add_movie_page=AddMoviePage(driver, base_url)
        self.movie_page=MoviePage(driver, base_url)


    def go_to_home_page(self):
        self.driver.get(self.base_url)

    def go_to_main_page(self):
        self.driver.get(self.base_url+"#!/sort/name%20asc/")


    def do_login(self, user):
        lp = self.login_page
        lp.username_field.clear()
        lp.username_field.send_keys(user.username)
        lp.password_field.clear()
        lp.password_field.send_keys(user.password)
        lp.submit_button.click()
#        driver.find_element_by_css_selector("nav")

    def do_logout(self):
        self.internal_page.logout_button.click()
        self.wait.until(alert_is_present()).accept()



    def is_logged_in(self):
        return self.login_page.is_this_page

    def is_not_logged_in(self):
        return self.internal_page.is_this_page

    def is_addmovie_page(self):
        return self.add_movie_page.is_this_page

    def confirm_alert(self):
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            alert.accept()

    def click_add_movie_btn(self):
        self.main_page.add_movie_button.click()


    def fill_movie_data_and_submit(self, movie):
        ap=self.add_movie_page
        ap.imbnum_field.clear()
        ap.imbnum_field.send_keys(movie.imbnum)
        ap.title_field.clear()
        ap.title_field.send_keys(movie.title)
        ap.year_field.clear()
        ap.year_field.send_keys(movie.year)
        ap.notes_field.clear()
        ap.notes_field.send_keys(movie.notes)
        ap.submit_btn.click()

    def movie_is_shown(self):
        return self.movie_page.is_this_page


    def movie_is_not_added(self):
        if not (self.add_movie_page.is_this_page):
            return False
        if not (self.driver.find_element_by_css_selector("label.error").is_displayed()):
            return False
#        if  not (self.driver.find_element_by_name("name").is_selected()):
 #           return False
        return True

#        try:
#            self.wait.until(self.add_movie_page.is_this_page)
#            self.driver.find_element_by_name("name").is_selected()
#            self.driver.find_element_by_css_selector("label.error").is_displayed()
#            return True
#        except WebDriverException:
#            return False


    def movie_is_removed(self):
        return self.login_page.is_this_page


    def go_edit_movie(self, movie_title):
        self.main_page.get_movie(movie_title).click()


    def remove_movie(self):
        btn=self.movie_page.rem_btn
        btn.click()
        self.confirm_alert()


    def search_not_exist_movie(self):
        mp=self.main_page
        mp.search_field.clear()
        mp.search_field.send_keys("1234567890!@#$%^&*()_"+ Keys.RETURN)
        app.driver.find_element_by_id("q").clear()
        app.driver.find_element_by_id("q").send_keys("1234567890!@#$%^&*()_"+ Keys.RETURN)
        self.wait.until(presence_of_element_located((By.XPATH,"//div[@id='results']/div[.='No movies where found.']" )))