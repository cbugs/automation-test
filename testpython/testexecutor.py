# -*- coding: utf-8 -*-
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import mysql.connector
import os
import sys
import datetime



class UntitledTestCase(unittest.TestCase):
    #steps = [["open","https://www.facebook.com/",""],["click","id=email",""],["type","id=email","salmanplaystation2@gmail.com"],["click","id=pass",""],["type","id=pass","12345678"],["click","id=u_0_2",""]]
    #case_name = "kaufmanverifier.xml"
    #print('Number of arguments:', len(sys.argv), 'arguments.')
    #print('Argument List:', str(sys.argv))
    #
    count = 0
    case_name = ""
    browserdriver = []
    browsers = ""
    currentbrowser = ""
    driver = ""

    browser_options = Options()
    browser_options.add_argument("--headless")

    browser_options.add_argument("--window-size=1920x1080")

    def setUp(self):
        print(self.browsers)
        cwd = os.getcwd()

        if "chrome" in self.browsers:
            self.currentbrowser="chrome"
            self.browsers.remove('chrome')
            chrome_driver = cwd+"\\chrome\\chromedriver.exe"
            print("path=", chrome_driver)
            self.driver = webdriver.Chrome(options=self.browser_options, executable_path=chrome_driver)
        elif "firefox" in self.browsers:
            self.currentbrowser = "firefox"
            self.browsers.remove('firefox')
            chrome_driver = cwd + "\\firefox\\geckodriver.exe"
            self.driver = webdriver.Firefox(firefox_options=self.browser_options, executable_path=chrome_driver)
        else:
            self.currentbrowser = "edge"
            self.browsers.remove('edge')
            self.driver = webdriver.Edge(options=self.browser_options, executable_path=cwd+"\\edge\\MicrosoftWebDriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        print(self.case_name)
        steps = self.getArray(self.case_name)
        size = len(steps)
        if size > 0:
            # open file
            print("executing testcase: ", self.case_name)
            now = datetime.datetime.now()
            b = now.strftime("%Y-%m-%d_%H-%M-%S")
            f = open(self.case_name + self.currentbrowser + b + ".txt", "a+")

            f.write(
                "\n-----------------------------------------------------------------------------------------------------------------------\n")
            f.write(
                "######################################################################################################################\n")
            f.write(
                "-----------------------------------------------------------------------------------------------------------------------\n")
            f.write("Current Time \n")
            f.write(now.strftime("%Y-%m-%d %H:%M:%S\n"))
            f.write(
                "-----------------------------------------------------------------------------------------------------------------------\n")
            print("executing testcase: ", self.case_name, "\n")
            a = "executing testcase: " + self.case_name + "\n"
            f.write(a)
            try:
                print(self.case_name)
                self.execute_steps(steps, f)
            except Exception as e:
                print("type error: " + str(e))
                a="type error: " + str(e)
                f.write(a)
                f.write("taking screenshot")
                self.driver.get_screenshot_as_file("test.png")
                raise e
            f.close()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

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


    def execute_steps(self,listSteps,f):
        driver = self.driver
        driver.maximize_window()
        for step in listSteps:
            # print(step)

            target = step[1]
            if "open" in step[0]:
                print("opening ", step[1])
                a = "opening " + step[1] + "\n"
                f.write(a)
                driver.get(step[1])
            elif "click" in step[0]:
                if "/" in target[1]:
                    print("click element by xpath ", target)
                    a = "click element by xpath " + target + "\n"
                    f.write(a)
                    driver.find_element_by_xpath(target).click()
                elif "link=" in target:

                    linktag = target.split("=")
                    print("click link ", linktag[1])
                    a = "click link " + linktag[1] + "\n"
                    f.write(a)
                    driver.find_element_by_link_text(linktag[1]).click()
                elif "id=" in step[1]:
                    idtag = target.split("=")
                    print("click on element with id ", idtag[1])
                    a = "click on element with id " + idtag[1] + "\n"
                    f.write(a)
                    driver.find_element_by_id(idtag[1]).click()
                elif "name=" in target:
                    nametag = target.split("=")
                    print("click on element with name ", nametag[1])
                    a = "click on element with name " + nametag[1] + "\n"
                    f.write(a)
                    driver.find_element_by_name(nametag[1]).click()
            elif "type" in step[0]:
                if "/" in target[1]:
                    print("clearing field with xpath ", target)
                    a = "clearing field with xpath " + target + "\n"
                    f.write(a)
                    driver.find_element_by_xpath(target).clear()
                    print("typing ", step[2], " field with xpath ", target)
                    a = "typing " + step[2] + " field with xpath " + target + "\n"
                    f.write(a)
                    driver.find_element_by_xpath(target).send_keys(step[2])
                elif "id=" in step[1]:
                    idtag = target.split("=")
                    print("clearing field with element id ", idtag[1])
                    x = str(idtag[1])
                    b = "clearing field with element id " + x + "\n"
                    f.write(b)
                    driver.find_element_by_id(idtag[1]).clear()
                    print("inserting ", step[2], "field with element id ", idtag[1])
                    a = "inserting " + step[2] + "field with element id " + idtag[1] + "\n"
                    f.write(a)
                    driver.find_element_by_id(idtag[1]).send_keys(step[2])
                elif "name=" in target:
                    nametag = target.split("=")
                    print("clearing field with element name ", nametag[1])
                    a = "clearing field with element name " + nametag[1] + "\n"
                    f.write(a)
                    driver.find_element_by_name(nametag[1]).clear()
                    print("inserting", step[2], "field with element name ", nametag[1])
                    a = "inserting" + step[2] + "field with element name " + nametag[1] + "\n"
                    f.write(a)
                    driver.find_element_by_name(nametag[1]).send_keys(step[2])
            elif "assertText" in step[0]:
                if "/" in target[1]:
                    print("assertEqualText ", step[2], "with text in element with xpath ", target)
                    a = "assertEqualText " + step[2], "with text in element with xpath " + target + "\n"
                    f.write(a)
                    self.assertEqual(step[2], driver.find_element_by_xpath(
                        target).text)
                elif "link=" in target:

                    linktag = target.split("=")
                    print("assertEqualText ", step[2], "with text in link ", linktag[1])
                    a = "assertEqualText " + step[2] + "with text in link " + linktag[1] + "\n"
                    f.write(a)
                    self.assertEqual(step[2], driver.find_element_by_link_text(linktag[1]).text)

                elif "id=" in step[1]:
                    idtag = target.split("=")
                    print("assertEqualText ", step[2], "with text in element with id ", idtag[1])
                    a = "assertEqualText " + step[2], "with text in element with id " + idtag[1] + "\n"
                    f.write(a)
                    self.assertEqual(step[2], driver.find_element_by_id(idtag[1]).text)

                elif "name=" in target:
                    nametag = target.split("=")
                    print("assertEqualText ", step[2], "with text in element with name ", nametag[1])
                    a = "assertEqualText " + step[2], "with text in element with name " + nametag[1] + "\n"
                    f.write(a)
                    self.assertEqual(step[2], driver.find_element_by_name(nametag[1]).text)
            elif "assertElementPresent" in step[0]:
                if "/" in target[1]:
                    print("assert element is present with xpath ", target)
                    a = "assert element is present with xpath " + target + "\n"
                    f.write(a)
                    self.assertTrue(self.is_element_present(By.XPATH, target))
                elif "link=" in target:

                    linktag = target.split("=")
                    print("assert element is present with link ", linktag[1])
                    a = "assert element is present with link " + linktag[1] + "\n"
                    f.write(a)
                    self.assertTrue(self.is_element_present(By.LINK_TEXT, linktag[1]))

                elif "id=" in step[1]:
                    idtag = target.split("=")
                    print("assert element is present with id ", idtag[1])
                    a = "assert element is present with id " + idtag[1] + "\n"
                    f.write(a)
                    self.assertTrue(self.is_element_present(By.ID, idtag[1]))

                elif "name=" in target:
                    nametag = target.split("=")
                    print("assert element is present with name ", nametag[1])
                    a = "assert element is present with name " + nametag[1] + "\n"
                    f.write(a)
                    self.assertTrue(self.is_element_present(By.NAME, nametag[1]))

            elif "waitForVisible" in step[0]:
                if "/" in target[1]:
                    print("waiting for element with xpath ", target, "to be visible")
                    a = "waiting for element with xpath " + target + "to be visible" + "\n"
                    f.write(a)
                    for i in range(60):
                        try:
                            if driver.find_element_by_xpath(target).is_displayed():
                                break
                        except:
                            pass
                        time.sleep(1)
                    else:
                        print("element is not visible within time frame")
                        a = "element is not visible within time frame" + "\n"
                        f.write(a)
                        self.fail("time out")

                elif "link=" in target:

                    linktag = target.split("=")
                    print("waiting for element with link ", linktag[1], "to be visible")
                    a = "waiting for element with link " + linktag[1], "to be visible" + "\n"
                    f.write(a)
                    for i in range(60):
                        try:
                            if driver.find_element_by_link_text(linktag[1]).is_displayed():
                                break
                        except:
                            pass
                        time.sleep(1)
                    else:
                        print("element is not visible within time frame")
                        a = "element is not visible within time frame" + "\n"
                        f.write(a)
                        self.fail("time out")

                elif "id=" in step[1]:
                    idtag = target.split("=")
                    print("waiting for element with id ", idtag[1], "to be visible")
                    a = "waiting for element with id " + idtag[1], "to be visible" + "\n"
                    f.write(a)
                    for i in range(60):
                        try:
                            if driver.find_element_by_id(idtag[1]).is_displayed():
                                break
                        except:
                            pass
                        time.sleep(1)
                    else:
                        print("element is not visible within time frame")
                        a = "element is not visible within time frame" + "\n"
                        f.write(a)
                        self.fail("time out")

                elif "name=" in target:
                    nametag = target.split("=")
                    print("waiting for element with name ", nametag[1], "to be visible")
                    a = "waiting for element with name " + nametag[1], "to be visible" + "\n"
                    f.write(a)
                    for i in range(60):
                        try:
                            if driver.find_element_by_name(nametag[1]).is_displayed():
                                break
                        except:
                            pass
                        time.sleep(1)
                    else:
                        print("element is not visible within time frame")
                        a = "element is not visible within time frame" + "\n"
                        f.write(a)
                        self.fail("time out")
            elif "assertTextPresent" in step[0]:
                self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text,
                                         r"^[\s\S]*" + target + "[\s\S]*$")

        print("taking screenshot")
        a = "taking screenshot"
        f.write(a)
        driver.get_screenshot_as_file("test.png")

    def getArray(self,testcase):

        conn = mysql.connector.connect(user="root", password="", host="localhost", database="testcasedb")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM testcases WHERE testCaseName='" + testcase + "' ORDER BY ID")
        array = []

        for row in cursor.fetchall():
            array.append([row[2], row[3], row[4]])
        conn.close()
        if array == []:
            print("Test case not found ")

        else:
            return array

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    UntitledTestCase.count = 3
    if len(sys.argv) == 3:
        UntitledTestCase.browserdriver = sys.argv.pop()
        UntitledTestCase.case_name = sys.argv.pop()
        UntitledTestCase.browsers = UntitledTestCase.browserdriver.split(",")
        if len(UntitledTestCase.browsers) > 1:
            UntitledTestCase.count = 2
        else:
            UntitledTestCase.count = 1
    else:
        UntitledTestCase.case_name = sys.argv.pop()
        UntitledTestCase.browsers = ['chrome', 'firefox', 'edge']

    print("testbrosers",UntitledTestCase.browsers)
    for x in range(UntitledTestCase.count):
        unittest.main(testRunner=HTMLTestRunner(output="example_dir"),exit=False)
