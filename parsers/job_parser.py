from selenium.common.exceptions import NoSuchElementException
from locators.naukri_jobs_locator import JobsLocator


class JobParser:
    def __init__(self, parent):
        self.parent = parent

    def __str__(self):
        return "{title},{company}," \
               "{exp},{salary}," \
               "{location},{age}," \
               "{skill}".format(title=self.job_title, company=self.company_name,
                                exp=self.experience, salary=self.salary,
                                location=self.location, age=self.age,
                                skill=self.skill)

    @property
    def job_title(self):
        locator = JobsLocator.JOB_TITLE
        return self.parent.find_element_by_css_selector(locator).text.replace(',', '')

    @property
    def company_name(self):
        locator = JobsLocator.COMPANY_NAME
        return self.parent.find_element_by_css_selector(locator).text.replace(',', '')

    @property
    def experience(self):
        locator = JobsLocator.EXPERIENCE
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def salary(self):
        locator = JobsLocator.SALARY
        return self.parent.find_element_by_css_selector(locator).text.replace(',', '')

    @property
    def location(self):
        locator = JobsLocator.LOCATION
        return self.parent.find_element_by_css_selector(locator).text.replace(',', '|')

    @property
    def skill(self):
        locator = JobsLocator.SKILL
        try:
            return self.parent.find_element_by_css_selector(locator).text.replace('\n', '|')
        except NoSuchElementException:
            return 'N/A'

    @property
    def age(self):
        locator1 = JobsLocator.JOB_AGE
        locator2 = JobsLocator.JOB_POSTED_TODAY
        locator3 = JobsLocator.JOB_POSTED_FOR_FUTURE
        try:
            return self.parent.find_element_by_css_selector(locator1).text
        except NoSuchElementException:
            try:
                return self.parent.find_element_by_css_selector(locator2).text
            except NoSuchElementException:
                return self.parent.find_element_by_css_selector(locator3).text

