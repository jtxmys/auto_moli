import os
import time

from selenium.common.exceptions import StaleElementReferenceException


def insert_img(driver, file_name):
    base_dir = os.path.dirname(__file__)
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/auto_moli')[0]
    file_path = base + "/report/report_image/" + file_name + ".png"
    driver.get_screenshot_as_file(file_path)

def highlight_element(driver, web_element):
    # src = "{0}.style.border=\"5px solid red\"".format(element)
    try:
        driver.execute_script("arguments[0].setAttribute('style',\"border: 5px solid red;\");", web_element)
    except StaleElementReferenceException:
        print("请设置self.web_element的值")
    time.sleep(3)

