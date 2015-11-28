from internal_page import InternalPage
from selenium.webdriver.common.by import By



class MoviePage(InternalPage):

    @property
    def rem_btn(self):
        return self.driver.find_element_by_css_selector("img[alt=\"Remove\"]")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CSS_SELECTOR, "div#movie div[class='maininfo_full']"))

#        el=self.wait.until(self.driver.presence_of_element_located((By.CSS_SELECTOR, "div#movie div[class='maininfo_full']")))
#        return (el<>None)

 #       try:
 #           self.wait.until(self.is_element_visible((By.CSS_SELECTOR, "div#movie div[class='maininfo_full']")))
#            return True
 #       except WebDriverException:
 #           return False
 #       return