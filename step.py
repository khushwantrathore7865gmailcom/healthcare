from splinter import Browser
from selenium import webdriver

# driver = webdriver.Chrome(executable_path=r'E:\chromedriver_win32\chromedriver.exe')

browser = Browser('chrome', executable_path=r'E:\chromedriver_win32 (1)\chromedriver.exe',)

browser.visit('http://127.0.0.1:8000/')
