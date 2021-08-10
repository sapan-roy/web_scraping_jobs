import time
from selenium.common.exceptions import NoSuchElementException
from locators.naukri_jobs_locator import JobsLocator
from parsers.job_parser import JobParser


class PageParser:
    def __init__(self, browser):
        self.browser = browser

    @property
    def job(self):
        locator = JobsLocator.PAGE_LOCATOR
        job_tags = self.browser.find_elements_by_css_selector(locator)
        return [JobParser(e) for e in job_tags]

    # @property
    def next_page(self):
        locator = JobsLocator.NEXT_PAGE_LOCATOR
        elems = self.browser.find_elements_by_css_selector(locator + '[href]')
        next_page_url = [elem.get_attribute('href') for elem in elems]
        try:
            return next_page_url[0]
        except NoSuchElementException:
            return None

    # @classmethod
    # def force_wait(cls, wait_time):
    #     """this function is used to wait the program and let selenium to load"""
    #     count = 0
    #     while count < wait_time:
    #         #print("Page is loading.. ", count)
    #         count += 1
    #         time.sleep(1)

