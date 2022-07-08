from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.headless = True

driver = webdriver.Chrome(options=chrome_options, executable_path="C:\\Users\\Hampus\\Documents\\chromedriver_103\\chromedriver.exe")

driver.get("https://vecka.nu")

html_source = driver.page_source

soup = BeautifulSoup(html_source, "html.parser")
text = soup.get_text()

print(text)