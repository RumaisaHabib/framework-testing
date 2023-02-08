from appium import webdriver
from webdriver_manager.opera import OperaDriverManager
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.chrome.service import Service
import os
import time

options = UiAutomator2Options()
desired_caps = options.to_capabilities()
options.binary_location = '/usr/bin/operadriver'
desired_caps['app'] = os.path.abspath('/home/rumi/Downloads/Research/AWFA/RBR/opera_mini/opera-browser.apk')
desired_caps['appPackage'] = 'com.opera.browser'
desired_caps['androidDeviceSocket'] = desired_caps['appPackage'] + '.devtools'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_caps)
driver.get("https://www.bbc.com")
time.sleep(100)
print("great sucess")