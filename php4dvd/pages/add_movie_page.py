from internal_page import InternalPage
from selenium.webdriver.common.by import By


class AddMoviePage(InternalPage):



    @property
    def is_this_page(self):
        return self.is_element_visible((By.ID, "imdbsearchform"))

    @property
    def imbnum_field(self):
        return self.driver.find_element_by_name("imdbid")

    @property
    def title_field(self):
        return self.driver.find_element_by_name("name")

    @property
    def year_field(self):
        return self.driver.find_element_by_name("year")

    @property
    def notes_field(self):
        return self.driver.find_element_by_name("notes")

    @property
    def label_err(self):
        return self.is_element_visible((By.CSS_SELECTOR, "label.error"))

    @property
    def submit_btn(self):
        return self.driver.find_element_by_id("submit")