from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium import common
from selenium.webdriver.common import keys

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time
import json
import pyautogui
import os

tweet_json = open("tweet.json")
tweet = json.load(tweet_json)["0"]
tweet_json.close()


driver = webdriver.Firefox()
driver.implicitly_wait(20)
driver.maximize_window()
driver.get("https://twitter.com/i/flow/login")

#Login
username = "TownesLona1"
password = "loXsf3583"
number = "565285099"
driver.find_element(By.XPATH, "//input[@autocomplete='username']").send_keys(username)
driver.find_element(By.XPATH, "//input[@autocomplete='username']").send_keys(Keys.RETURN)
driver.find_element(By.XPATH, "//input[@autocomplete='current-password']").send_keys(password)
driver.find_element(By.XPATH, "//input[@autocomplete='current-password']").send_keys(Keys.RETURN)
time.sleep(3)
if (driver.current_url == "https://twitter.com/i/flow/login"):
    driver.find_element(By.XPATH, "//input[@autocomplete='tel']").send_keys(number)
    driver.find_element(By.XPATH, "//input[@autocomplete='tel']").send_keys(Keys.RETURN)
time.sleep(2)

def main():
    def post_and_pin_tweet():

        def insert_tweet_text(tweet_text):
            driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys(tweet_text)
            time.sleep(2)
            
        def insert_media(media_paths):
            element = driver.find_element(By.XPATH, "//div[@aria-label='Add photos or video']")
            for media_path in media_paths:
                element.click()
                time.sleep(20)
                pyautogui.write(os.path.abspath(media_path))
                pyautogui.press("enter")
                time.sleep(30)
                driver.execute_script("arguments[0].scrollIntoView();", element)

        #Click on tweet button
        driver.find_element(By.XPATH, "//a[@data-testid='SideNav_NewTweet_Button']").click()
        time.sleep(5)

        try:
            #Click on 'Maybe Later' on Twitter Spaces popup
            driver.find_element(By.CSS_SELECTOR, "#layers > div.css-1dbjc4n.r-1p0dtai.r-1d2f490.r-105ug2t.r-u8s1d.r-zchlnj.r-ipm5af > div > div > div.css-1dbjc4n.r-u8s1d > div > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-eqz5dr.r-ymttw5.r-ttdzmv > div.css-18t94o4.css-1dbjc4n.r-1niwhzg.r-1ets6dv.r-sdzlij.r-1phboty.r-rs99b7.r-1ydw1k6.r-1r5su4o.r-19yznuf.r-64el8z.r-1ny4l3l.r-1dye5f7.r-o7ynqc.r-6416eg.r-lrvibr > div > span > span").click()
            time.sleep(4)
        except:
            pass
        finally:
            #Post tweet
            for tweet_text, media_paths in tweet.items():
                if (tweet_text and media_paths):
                    insert_tweet_text(tweet_text)
                    insert_media(media_paths)
                elif (tweet_text):
                    insert_tweet_text(tweet_text)
                elif (media_paths):
                    insert_media(media_paths)
                else:
                    print('Nothing to tweet.')
                driver.find_element(By.XPATH, "//div[@data-testid='tweetButton']").click()
                time.sleep(7)

        #Go to profile page
        driver.find_element(By.XPATH, "//a[@data-testid='AppTabBar_Profile_Link']").click()
        time.sleep(2)

        #Pin most recent tweet
        driver.find_element(By.CSS_SELECTOR, "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-jxzhtn.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div:nth-child(2) > div > div > section > div > div > div:nth-child(1) > div > div > div > article > div > div > div > div.css-1dbjc4n.r-18u37iz > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-kzbkwu > div:nth-child(1) > div > div > div.css-1dbjc4n.r-1joea0r > div > div > div > div").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@data-testid='pin']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@data-testid='confirmationSheetConfirm']").click()
        time.sleep(0.5)

        
    post_and_pin_tweet()

if __name__ == "__main__":
    main()
