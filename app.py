import random
from selenium import webdriver
from parsers.page_parser import PageParser
import time

FILENAME = 'D:\Python_Projects\Analyzing_data_with_pandas\\naukri_scrapped_data3.csv'
NAUKRI_IT_JOBS_URL = "https://www.naukri.com/python-jobs?k=python"
WAIT_TIME = 5  # Time provided to load each web page
PAGE_COUNT_TO_SCRAP = 5  # Number of pages to scrap
FILE_HEADER = "job_id,job_title,company,experience,salary,location,job_age,skills"


def write_data(data_container, file_name):
    with open(file_name, 'a') as file:
        for line in data_container:
            file.write(line)
            file.write('\n')


def force_wait(wait_time):
    """this function is used to wait the program and let selenium to load"""
    count = 0
    while count < wait_time:
        # print("Page is loading.. ", count)
        count += 1
        time.sleep(1)


def main_func(url, wait_time, counter):
    chrome = webdriver.Chrome(executable_path="D:\\chromedriver")
    job_id = 1
    count = 0
    data_container = [FILE_HEADER]
    while count < counter:
        chrome.get(url)
        # PageParser.force_wait(wait_time)
        force_wait(wait_time)
        # naukri_jobs = PageParser(chrome).job
        page = PageParser(chrome)
        naukri_jobs = page.job

        for job in naukri_jobs:
            data_container.append(str(job_id) + "," + str(job))
            job_id += 1

        write_data(data_container, FILENAME)
        data_container.clear()

        if PageParser(chrome).next_page is None:
            break

        # url = PageParser(chrome).next_page
        url = page.next_page()

        count += 1

        random_wait_time = random.randint(30, 70)
        print("Page scrapped...")
        print("Waiting for {} seconds to load next page: ".format(random_wait_time))
        print("********************************************")
        # PageParser.force_wait(random_wait_time)
        force_wait(random_wait_time)


if __name__ == '__main__':
    main_func(NAUKRI_IT_JOBS_URL, WAIT_TIME, PAGE_COUNT_TO_SCRAP)

