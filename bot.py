
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

import schedule
import time
import password


print(password.number)
def setup_schedules():
    schedule.every().monday.at("20:00").do(run_bot)
    schedule.every().monday.at("21:00").do(run_bot)

    schedule.every().wednesday.at("20:00").do(run_bot)
    schedule.every().wednesday.at("21:00").do(run_bot)

    schedule.every().thursday.at("10:00").do(run_bot)
    schedule.every().thursday.at("11:00").do(run_bot)

def run_bot():
        try:
            browser = webdriver.Firefox(executable_path="./drivers/geckodriver")

            num_bookings = 31


            browser.get('https://ibooking.sit.no/webapp/timeplan/?type=groupclasses&id=13&gyms=540')

            page_loaded = False
            while(not page_loaded):
                try:
                    loginbanner = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/button[1]/i")
                    loginbanner.click()
                    
                    page_loaded = True
                except:
                    browser.get('https://ibooking.sit.no/webapp/timeplan/?type=groupclasses&id=13&gyms=540')


            browser.switch_to.frame("auth-frame")

            WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, "username-input")))
            username_popup = False
            mobileNumberField = browser.find_element_by_id("username-input")
            mobileNumberField.send_keys(password.number)

            passwordField = browser.find_element_by_id("password-input")
            passwordField.send_keys(password.passw)

            browser.find_element_by_xpath("/html/body/div/div/div[1]/div/form/button").click()


            browser.switch_to.default_content()
            slots = browser.find_elements_by_class_name("instance")
            clicked = False
            while(not clicked):
                try:
                    slots[num_bookings].click() #Has to click twice for some reason
                    slots[num_bookings].click()
                    clicked = True
                except:
                    pass

            booked = False
            while(not booked):
                try:
                    book_button = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[6]/div/div/div[3]/div[8]/button[1]").click()
                    booked = True
                except:
                    try:
                        wait_list_button = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[6]/div/div/div[3]/div[8]/button[1]").click()
                        booked = True
                    except:
                        pass


            print("Booking successfully made!")
            browser.quit()
        except Exception as e:
            print("Booking failed")
            print(e)
setup_schedules()
print("Bot has started :)")

while(True):
    schedule.run_pending()
    time.sleep(1)