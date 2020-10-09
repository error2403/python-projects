from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


# pastes bee movie script into discord chat

text_box = webdriver.find_element_by_css_selector('.slateTextArea-1Mkdgw > div:nth-child(1)')
text_box.click()

text_box.send_keys('test')
text_box.send_keys(Keys.ENTER)