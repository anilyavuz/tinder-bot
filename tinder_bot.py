from selenium import webdriver
import selenium
from time import sleep
from secrets import email_id, password

class TinderBot():
    def __init__(self):
        self.driver= webdriver.Chrome()
        
    def login(self):
        self.driver.get('https://tinder.com')
        sleep(3)
        
        login_with_facebook = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        login_with_facebook.click()
        sleep(2)
        #switching to popup window
        popup_window =self.driver.window_handles[1]
        base_window=self.driver.window_handles[0]
        
        self.driver.switch_to_window(popup_window)
        
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(email_id)
        password_in=self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_in.send_keys(password)
        login_btn= self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()
        sleep(2)
        self.driver.switch_to_window(base_window)
        #enablelocations and notifications
        sleep(3)
        allow_location= self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow_location.click()
        notification_allow = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        notification_allow.click()
        
        
    def like(self):
        like= self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[4]/button')
        like.click()


    def dislike(self):
        dislike= self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[2]/button/span/svg')
        dislike.click()

    
    def close_popup(self):
        close_popup= self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]/span')
        close_popup.click()

    def close_match(self):
        close_match = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        close_match.click()
    def autoswipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    
                    self.close_popup()
                    
                except Exception:
                    self.close_match()
bot= TinderBot()
bot.login()
bot.autoswipe()
