from internal_page import InternalPage
from selenium.webdriver.common.by import By



class MainPage(InternalPage):

    @property
    def add_movie_button(self):
        return self.driver.find_element_by_css_selector("img[alt=\"Add movie\"]")


    def get_movie(self, title):
        str="div#results div[title='"+title+"']"
        return self.driver.find_element_by_css_selector(str)