#FOR EACH TWITTER ACCOUNT IN ACCOUNTS.JSON,
#MAKE SOME CHANGES IN THE ACCOUNT'S SETTINGS AS SPECIFIED IN SETTINGS.JSON
#POST AND PIN TWEET FROM TWEET.JSON

from selenium import webdriver
from selenium import common
from selenium.webdriver.common import keys

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import pyautogui

import time
import random
import json
import os



def execute(account, settings, tweet):
    """ For each account in dictionary, launch browser, update settings, post and pin tweet, and exit browser """

    def update_settings():

        #Unpack settings info
        profile_pic = random.choice(settings["profile_pics"])
        banner = settings["banner"]
        display_name = settings["display_name"]
        description = settings["description"]
        
        #Go to EditProfile
        driver.find_element(By.XPATH, "//a[@data-testid='AppTabBar_Profile_Link']").click()
        driver.find_element(By.XPATH, "//a[@data-testid='editProfileButton']").click()

        #Change profile picture
        driver.find_element(By.XPATH, "//div[@aria-label='Add avatar photo']").click()
        time.sleep(5)
        pyautogui.write(os.path.abspath(profile_pic))
        time.sleep(5)
        pyautogui.press("enter")
        time.sleep(5)
        driver.find_element(By.XPATH, "//div[@data-testid='applyButton']").click()

        #Change banner
        driver.find_element(By.XPATH, "//div[@aria-label='Add banner photo']").click()
        time.sleep(5)
        pyautogui.write(os.path.abspath(banner))
        time.sleep(5)
        pyautogui.press("enter")
        time.sleep(5)
        driver.find_element(By.XPATH, "//div[@data-testid='applyButton']").click()

        #Change display name
        driver.find_element(By.XPATH, "//input[@name='displayName']").clear()
        driver.find_element(By.XPATH, "//input[@name='displayName']").send_keys(display_name)
        time.sleep(0.5)

        #Change description
        driver.find_element(By.XPATH, "//textarea[@name='description']").clear()
        driver.find_element(By.XPATH, "//textarea[@name='description']").send_keys(description)

        #Save profile settings
        driver.find_element(By.XPATH, "//div[@data-testid='Profile_Save_Button']").click()
        time.sleep(5)

        #Go to DirectMessagesPrivacySettings
        driver.find_element(By.XPATH, "//div[@data-testid='AppTabBar_More_Menu']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@data-testid='settings']").click()
        driver.find_element(By.XPATH, "//a[@data-testid='privacyAndSafetyLink']").click()
        driver.find_element(By.XPATH, "//a[contains(@href,'/settings/direct')]").click()
        
        #Update privacy settings
        driver.find_element(By.XPATH, "//input[@aria-describedby='CHECKBOX_1_LABEL']").click()
        driver.find_element(By.XPATH, "//input[@aria-describedby='CHECKBOX_2_LABEL']").click()
        time.sleep(0.5)

        print(f"All settings for {username} has been successfully updated.")

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

        print(f"{username} has successfully posted and pinned the specified tweet.")

    err = 0
    err_max = 5
    updated = False
    
    #Login details
    username = account[0]
    password = account[1]
    number = account[2]

    while ((err < err_max) and (updated == False)):
        """Keep attempting to execute operations for each account until either all operations have been successfully executed or the maximum number of retries has been reached."""
        try:
            print(f"Attempting to log in {username}.")

            #Initialize and go to Twitter login page
            driver = webdriver.Firefox()
            driver.implicitly_wait(20)
            driver.maximize_window()
            driver.get("https://twitter.com/i/flow/login")

            #Login
            driver.find_element(By.XPATH, "//input[@autocomplete='username']").send_keys(username)
            driver.find_element(By.XPATH, "//input[@autocomplete='username']").send_keys(Keys.RETURN)
            driver.find_element(By.XPATH, "//input[@autocomplete='current-password']").send_keys(password)
            driver.find_element(By.XPATH, "//input[@autocomplete='current-password']").send_keys(Keys.RETURN)
            time.sleep(3)
            if (driver.current_url == "https://twitter.com/i/flow/login"):
                driver.find_element(By.XPATH, "//input[@autocomplete='tel']").send_keys(number)
                driver.find_element(By.XPATH, "//input[@autocomplete='tel']").send_keys(Keys.RETURN)
            time.sleep(2)

            #Accept all cookies; move on if popup does not exist
            try:
                time.sleep(2)
                driver.find_element(By.CSS_SELECTOR, "#layers > div > div > div > div > div > div.css-1dbjc4n.r-eqz5dr.r-1joea0r.r-1r5su4o > div:nth-child(1) > div").click()
                time.sleep(2)
            except:
                pass

            update_settings()

            post_and_pin_tweet()

            driver.quit()

            updated = True
        except:
            print(f"Something unexpected came up while working with {username}. But do not worry. The browser will be relaunched, hoping the problem does not persist.")
            print(f"{err_max - err} tries remaining before {username} is skipped.")
            driver.quit()
            err += 1

            #Save login information of each skipped account in 'skipped_accounts.json'
            if (err == err_max):
                with open("skipped_accounts.json", "r+") as skipped_accounts_json:
                    skipped_accounts = json.load(skipped_accounts_json)
                    skipped_accounts[len(skipped_accounts)+1] = account
                    skipped_accounts_json.seek(0)
                    json.dump(skipped_accounts, skipped_accounts_json)
                    print(f"Operations for {username} could not be completed due to a persistent anomaly.")
                    print(f"Login information for {username} has been added to the file 'skipped_accounts.json'. You can cut and paste the information into 'accounts.json' to try yet again.")


def main():

    print("Initializing...")

    #Load accounts' credentials into dictionary
    accounts_json = open("accounts.json")
    accounts = json.load(accounts_json)
    accounts_json.close()

    #Load settings info
    settings_json = open("settings.json")
    settings = json.load(settings_json)
    settings_json.close()

    #Load tweet
    tweet_json = open("tweet.json")
    tweet = json.load(tweet_json)["0"]
    tweet_json.close()

    for account in accounts.values():
        execute(account, settings, tweet)

        #Sleep for 10 seconds before switching account
        time.sleep(10)

    print("Settings for all Twitter accounts in 'accounts.json' have been successfully updated.")
    print("All accounts have successfully posted and pinned a tweet.")

if __name__ == "__main__":
    main()
