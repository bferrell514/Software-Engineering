from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from typing import Set

# makes chrome headless
chrome_options = Options()
chrome_options.headless = True

class Section: 
    def __init__(self, time, instructor, status, id):
        self.id = id
        self.time = time
        self.instructor = instructor
        self.status = status


class Course:
    def __init__(self): 
        self.sections = dict()
    
    def add_section(self, section):
        self.sections[section.id] = section



class CourseSearch:
    def __init__(self, courses: Set[str]):
        PATH = r"D:\Selenium_webDriver\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
        self.driver.get("https://appcsprod.uri.edu:9516/psc/sa_crse_cat/EMPLOYEE/SA/c/COMMUNITY_ACCESS.CLASS_SEARCH.GBL")
        self.search_results = {course: self.search(course) for course in courses }

    def search(self, course: str):
        # Fill out the form
        subject, number = course.split(" ")
        subject_path = self.driver.find_element_by_xpath('//*[@id="SSR_CLSRCH_WRK_SUBJECT_SRCH$1"]')
        subject_path.send_keys(subject)
        number_path = self.driver.find_element_by_xpath('//*[@id="SSR_CLSRCH_WRK_CATALOG_NBR$2"]')
        number_path.send_keys(number)
        subject_path.send_keys(Keys.RETURN)
        
        # Holds a set of all possible sections
        course = Course()
        line_item = "0"
        
        while(True):
            try:
                section_time = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="MTG_DAYTIME$' + line_item + '"]'))
                )
                section_instructor = WebDriverWait(self.driver, 3).until(     
                    EC.presence_of_element_located((By.XPATH, '//*[@id="MTG_INSTR$' + line_item + '"]'))
                )
                section_status = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="win0divDERIVED_CLSRCH_SSR_STATUS_LONG$' + line_item + '"]/div/img'))
                    # EC.presence_of_element_located((By.XPATH, '//*[@id="win0divDERIVED_CLSRCH_SSR_STATUS_LONG$999"]/div/img'))
                )

                section_status = section_status.get_attribute('src')

                if section_status == "https://appcsprod.uri.edu:9516/cs/sa_crse_cat/cache/PS_CS_STATUS_OPEN_ICN_1.gif":
                    section_status = True
                else :
                    section_status = False
                course.add_section(Section(section_time.text, section_instructor.text, section_status, int(line_item)))
                line_item = int(line_item) + 1
                line_item = str(line_item)

            except:
                self.driver.get("https://appcsprod.uri.edu:9516/psc/sa_crse_cat/EMPLOYEE/SA/c/COMMUNITY_ACCESS.CLASS_SEARCH.GBL")
                # new_search = self.driver.find_element_by_xpath('//*[@id="CLASS_SRCH_WRK2_SSR_PB_NEW_SEARCH$3$"]')
                # #new_search.implicitly_wait(5)
                # new_search.click()
                # self.driver.get("https://appcsprod.uri.edu:9516/psc/sa_crse_cat/EMPLOYEE/SA/c/COMMUNITY_ACCESS.CLASS_SEARCH.GBL")
               
                return course
        
semester_search = CourseSearch({"CSC 305", "CSC 301"})
for section in semester_search.search_results["CSC 305"].sections.values():
    print(section.id, " ", section.time, " ", section.instructor, " ", section.status)

for section in semester_search.search_results["CSC 301"].sections.values():
    print(section.id, " ", section.time, " ", section.instructor, " ", section.status)

