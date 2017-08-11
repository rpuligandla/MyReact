from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.errorhandler import ErrorHandler
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pysnmp.hlapi import *
from selenium.common.exceptions import NoAlertPresentException

import unittest

driver = webdriver.Firefox()
driver.get("http://11.19.20.18")

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

username.send_keys("root")
password.send_keys("admin123")

driver.find_element_by_name("submit").click()
driver.implicitly_wait("20")


#driver.find_element_by_id("menu_node_status_tree").click()
#driver.find_element_by_id("menu_node_equipment").click()

#driver.find_element_by_xpath(".//*[@id='ChassisViewWidget1_options']/div[1]/label[2]").click()


driver.find_element_by_xpath(".//*[@id='menu_node_ethernet_tree']/div[1]").click()
driver.find_element_by_id("menu_node_port_management").click()
#driver.find_element_by_xpath(".//*[@id='PortSettingsWidget1intSet_TW_1_admin_status_renderer']/div[1]/label/input").clear()
#driver.find_element_by_xpath(".//*[@id='PortSettingsWidget1intSet_TW_1_admin_status_renderer']/div[1]/label/input").click()
# for



driver.find_element_by_xpath(".//*[@id='PortSettingsWidget1intSet_TW_1_admin_status_renderer']/div[1]/label/input").click()
driver.find_element_by_xpath(".//*[@id='page_toolbar_PageToolbarWidget1']/div[3]/button").click()
driver.find_element_by_id("top_menu_product_description").click()
#driver.find_element_by_css_selector("#AlarmTreeWidget1_tree_504889344_description > div > div > div.alarms_entity").click()




def close_alert_and_get_its_text(self):
    try:
        alert = self.driver.switch_to_alert()
        alert_text = alert.text
        if self.accept_next_alert:
            alert.accept()
        else:
            alert.dismiss()
        return alert_text
    finally:
        self.accept_next_alert = True


print("alarm is raised")
