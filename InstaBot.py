from selenium import webdriver
from time import sleep
from secret import username, password

class InstaBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.instagram.com/")

        sleep(1.5)

        facebook_login = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[1]/button')
        facebook_login.click()

        sleep(1)

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)
        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login_btn.click()

        sleep(3)

        notification_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        notification_btn.click()

    def go_follow_view(self):
        explore_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/a')
        explore_btn.click()

        sleep(1)

        viewall_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/h2/a')
        viewall_btn.click()

        sleep(1)

    def follow_people(self):
        std = 1
        while True:
            try:
                follow_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/div/div/div[{}]/div[3]/button'.format(str(std)))
                print('//*[@id="react-root"]/section/main/div/div[2]/div/div/div[{}]/div[3]/button'.format(str(std)))
                follow_btn.click()
                std += 1
            except Exception:
                self.go_follow_view()
                std = 1

    def auto_follow(self):
        self.go_follow_view()
        try:
            self.follow_people()
        except Exception:
            print(Exception)



bot = InstaBot()
bot.login()
