# -*- coding: utf-8 -*-
# @Time    : 2020-8-25 13:59
# @Author  : xjin
# @FileName: demo.py
# @Software: PyCharm
# @Blog    ：http://www.xjin.site/


from appium import webdriver
import subprocess
import pyautogui
from time import sleep

subprocess.Popen(
    [r"C:\Program Files\Bentley\OpenBuildings CONNECT Edition\OpenBuildingsDesigner\OpenBuildingsDesigner.exe",
     r"-wc C:\Program Files\ECIDI\ReStation\Launch_RSTN.cfg"])

sleep(10)
desired_caps = {'platformName': 'Windows', 'deviceName': 'pc180132', 'app': "Root"}

driver = webdriver.Remote('http://122.51.81.120:4723/wd/hub', desired_capabilities=desired_caps)

print("Appium Handles: ", driver.window_handles)

appWindow = driver.find_element_by_name("OpenBuildings Designer")

appWindowHandle = appWindow.get_attribute("NativeWindowHandle")
winHandle = format(int(appWindowHandle), 'x')
print(appWindowHandle)

desired_caps3 = {'platformName': 'Windows', 'appTopLevelWindow': winHandle}
driver3 = webdriver.Remote(command_executor='http://122.51.81.120:4723/wd/hub', desired_capabilities=desired_caps3)
driver3.switch_to.window(winHandle)
driver3.maximize_window()
driver3.implicitly_wait(30)

driver3.find_element_by_name("浏览").click()

# 清除文本框内容并输入要打开文件的完整路径，打开文件
driver3.find_element_by_class_name("Edit").clear()
driver3.find_element_by_class_name("Edit").send_keys(r"C:\Users\ecidi\Desktop\1-2.dgn")
driver3.find_element_by_name("打开(O)").click()


# 切换到Restation
driver3.find_element_by_class_name("RadComboBox").click()
driver3.find_element_by_name("ReStation").click()

# 新建配筋体
driver3.find_element_by_name("新建配筋体").click()
