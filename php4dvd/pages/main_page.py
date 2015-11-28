from internal_page import InternalPage
from selenium.webdriver.common.by import By



class MainPage(InternalPage):

    @property
    def add_movie_button(self):
        return self.driver.find_element_by_css_selector("img[alt=\"Add movie\"]")


    def get_movie(self, title):
        str="div#results div[title='"+title+"']"
        return self.driver.find_element_by_css_selector(str)

    @property
    def search_field(self):
        return self.driver.find_element_by_id("q")


    @property
    def is_no_movie(self):
        return self.is_element_visible((By.XPATH,"//div[@id='results']/div[.='No movies where found.']"))



    def is_movie(self,title):
        str="//div[.='"+title+"']"
        return self.is_element_visible((By.XPATH,str))
