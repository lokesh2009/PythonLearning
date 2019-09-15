
from selenium import  webdriver

from time import sleep
import unittest
import  datetime

class MyTestCase(unittest.TestCase):


    def setUp(self) -> None:
        self.driver = webdriver.Chrome("D:/Drivers/chromedriver_win32/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(20)

        print("-----------------------------------------------------")
        print("Test Environment created")
        print("Run started at :" + str(datetime.datetime.now))



    def test_navigatetoMercury(self):
            self.driver.get("http://gmail.com")
            sleep(2)
            print(self.driver.title)
            self.driver.get_screenshot_as_file("C:/Users/lsharma/Desktop/chromedriver_win32/UnitTest.jpeg")
            self.driver.maximize_window()



    def tearDown(self):
        if(self.driver!= None):
              print("-----------------------------------------------------")
              print("Test Environment Destroyed")
              print("Run started at :" + str(datetime.datetime.now()))



