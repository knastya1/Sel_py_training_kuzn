from page_page import Page
from selenium.webdriver.common.by import By


class InternalPage(Page):

    @property
    def logout_button(self):
        return self.driver.find_element_by_link_text("Log out")


    @property
    def is_this_page(self):
        return self.is_element_visible((By.ID, "loginform"))
