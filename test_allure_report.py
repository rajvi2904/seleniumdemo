from selenium import webdriver
import pytest
import allure

class TestHRM:
    @allure.severity(allure.severity_level.NORMAL)
    def test_logo(self):
         self.driver=r'chromedriver.exe'
         url = "https://opensource-demo.orangehrmlive.com/"
         self.driver.get(url)
         status=self.driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/img").is_displayed()
         if status==True:
             assert True
         else:
             assert False
         self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_listemployees(self):
        pytest.skip('skipping test')
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        act_title=self.driver.title
        
        if act_title=="OrangeHRM":
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False