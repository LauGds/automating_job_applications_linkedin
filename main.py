from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

POSITION_NAME = "Site Reliability Engineer"

service = Service(r"PATH\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3629279585&f_AL=true&f_JT=F&f_SB2=9&f_WT="
           "2&geoId=103644278&keywords=site%20reliability%20engineer&location=United%20States&refresh=true")

time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

time.sleep(3)
username = driver.find_element(by=By.NAME, value="session_key")
username.send_keys("EMAIL")

password = driver.find_element(by=By.ID, value="password")
password.send_keys("PASSWORD")

sign_in_button_two = driver.find_element(by=By.CLASS_NAME, value="btn__primary--large")
sign_in_button_two.send_keys(Keys.ENTER)

time.sleep(30)

all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    position_name = driver.find_element(by=By.PARTIAL_LINK_TEXT, value=POSITION_NAME)

    try:
        save_button = driver.find_element(by=By.CLASS_NAME, value="jobs-save-button")
        save_button.click()
        print("saved")
        time.sleep(3)

        follow_button = driver.find_element(by=By.CLASS_NAME, value="follow")
        time.sleep(3)

        if follow_button.get_attribute("aria-label") == "Following":
            print("following")
            time.sleep(3)
            continue
        elif follow_button.get_attribute("aria-label") == "Follow":
            follow_button.send_keys(Keys.ENTER)
            print("follow")
            time.sleep(3)
            continue
        else:
            pass

    except NoSuchElementException:
        print("No application button, skipped.")
        continue
