from selenium import webdriver

driver = webdriver.Chrome("D:/Drivers/chromedriver_win32/chromedriver.exe")
driver.set_page_load_timeout(20)
driver.get("http://www.gmail.com")
driver.maximize_window()
driver.imlicitly_wait(10)
driver.close()

