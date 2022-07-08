from selenium import webdriver
from lxml import html
import time


username = "012213"
password = ""




driver = webdriver.Chrome(executable_path=r'C:\Users\Hampus\Downloads\chromedriver_win32\chromedriver.exe')
driver.get("https://auth.vklass.se/grandid/initiate?id=27")

username_box = driver.find_element_by_id("userNameInput")
username_box.send_keys(username)

password = input("Lösenord: ")

password_box = driver.find_element_by_id("passwordInput")
password_box.send_keys(password)

login_box = driver.find_element_by_id("submitButton")
login_box.click()

# Är nu inne på Vklass

message = input("Meddelande: ")

driver.get("https://www.vklass.se/Messaging/MessageRead.aspx?id=11621102&created=False&backPage=%2fMessaging%2fMessages.aspx%3ffolder%3d-1")


driver.execute_script("toggleToolsDrawer()")

message_box = driver.find_element_by_id("ctl00_ContentPlaceHolder2_newPostTextBox")
message_box.send_keys(message)


sendMessage_box = driver.find_element_by_id("ctl00_ContentPlaceHolder2_sendButton")
sendMessage_box.click()


html_source = driver.page_source
tree = html.fromstring(html_source)

#someElement = tree.xpath('//*[@id="ctl00_ContentPlaceHolder2_postRepeater_ctl02_textLabel"]/text()')

#print(someElement)
