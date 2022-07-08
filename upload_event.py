from pytube import YouTube
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import cv2
import time


chrome_driver_path = "C:\\Users\\Hampus\\Documents\\chromedriver_103\\chromedriver.exe"
accept_cookies_xpath = '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button'


# Kolla specifikt try-not-to-laugh? Nja, vet ändå inte om den handlar om pengar... men kanske kan starta om manuellt annars


# Väntar tills 'channel' (i form av en URL till kananels startsida) har lagt upp en ny video
# och returnerar URL:en till den senaste videon
def check_upload_event(channel):
    
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_argument('log-level=3')
    driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver_path)

    driver.get(channel)

    accept_cookies = driver.find_element(By.XPATH, accept_cookies_xpath)
    accept_cookies.click()

    loop = True
    first_loop = True

    last = time.time()

    while loop:

        titles = []
        videos_found = False

        while not videos_found:
            titles = driver.find_elements(By.ID, "video-title")

            if titles == []:
                time.sleep(0.25)
            else:
                videos_found = True

        latest_video_name = titles[0].text
        

        if first_loop:
            last_video_name = latest_video_name
            first_loop = False

        elif latest_video_name != last_video_name:
            loop = False
            latest_video_url = titles[0].get_attribute("href")

            print("NEW VIDEO")
            print(latest_video_name)
            print(latest_video_url)

            return latest_video_url

        print(latest_video_name)
        time_diff = str(round(time.time() - last, 2))
        last = time.time()

        print("Updated - " + time_diff + " seconds elapsed")

        driver.refresh()

        #time.sleep(1)



def main():
    channel_URL = "https://www.youtube.com/user/KSIOlajidebtHD" # KSI

    channel_URL = "https://www.youtube.com/channel/UCt-PBc48GgrNP57gZLMXtuw" # min kanal

    latest_video = check_upload_event(channel_URL)


if __name__ == "__main__":
    main()