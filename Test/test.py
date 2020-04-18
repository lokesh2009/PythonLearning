from selenium import webdriver

driver = webdriver.Chrome("D:/Drivers/chromedriver_win32/chromedriver.exe")
driver.set_page_load_timeout(20)
driver.get("http://www.gmail.com")
driver.maximize_window()
driver.implicitly_wait(20)

driver.get_screenshot_as_file("C:/Users/lsharma/Desktop/chromedriver_win32/Home.jpeg")
driver.close()

