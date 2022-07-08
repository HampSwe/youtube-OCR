from pytube import YouTube
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import cv2


# Kolla specifikt try-not-to-laugh? Nja, vet ändå inte om den handlar om pengar... men kanske kan starta om manuellt annars


# Väntar tills 'channel' (i form av en URL till kananels startsida) har lagt upp en ny video
# och returnerar URL:en till den senaste videon
# Väntar 'wait' sekunder mellan varje uppdatering av kanalen
def check_upload_event(channel, wait=1):
    
    chrome_options = Options()
    chrome_options.headless = True
    driver = webdriver.Chrome(options=chrome_options, executable_path="C:\\Users\\Hampus\\Documents\\chromedriver_103\\chromedriver.exe")

    driver.get("https://vecka.nu")

    html_source = driver.page_source

    soup = BeautifulSoup(html_source, "html.parser")
    text = soup.get_text()

    print(text)


    #//*[@id="video-title"]


def main():
    channel_URL = "https://www.youtube.com/user/KSIOlajidebtHD"

    latest_video = check_upload_event(channel_URL)


if __name__ == "__main__":
    main()