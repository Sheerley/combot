from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import datetime
import random
import emojis

from secrets import username, password, channel

class combot:
    # holding title of last video
    current_title = emojis.encode("Surprising LilHuddy & Charli D'Amelio With 10 Custom Louis Vuitton Bags!! :briefcase::school_satchel: ft. TikTok, Addison Rae")
    message = 'You rocks! You can DM me on my insta @Shanduur :D'

    iterator = 0

    # holding timestamp
    d1 = datetime.datetime(2020, 3, 26, 19, 57, 15, 0)

    def __init__(self):
        self.driver=webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Driver\chromedriver.exe")

    def login(self):
        # load leaving youtube page
        self.driver.get('https://www.youtube.com/redirect?redir_token=A9J4Gqf8428258NOLOOXoRRLB918MTU4NTMwNDMxMEAxNTg1MjE3OTEw&q=https%3A%2F%2Fstackoverflow.com%2Fusers%2Fsignup%3Fssrc%3Dhead%26returnurl%3D%252fusers%252fstory%252fcurrent%27&event=video_description&v=HkgDRRWrZKg')
        time.sleep(3)

        # go to stack overflow
        self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[5]/div/div[3]/a[1]').click()
        time.sleep(2)
        
        # login with google
        self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        time.sleep(3)
        
        # write mail to login
        self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        time.sleep(3)
        
        # write password to login
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        time.sleep(2)

    def go_to_page(self):
        self.driver.get(channel)
        time.sleep(5)

    def check_and_refresh(self):
        # load newest video title 
        vid = self.driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse[1]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[1]/div[1]/div[1]/div[1]/h3/a')
        title = vid.get_attribute('title')

        # check if video title changed
        while self.current_title == title:
            self.driver.get(channel)
            time.sleep(5)
            vid = self.driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse[1]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[1]/div[1]/div[1]/div[1]/h3/a')
            title = vid.get_attribute('title')
            if self.iterator % 12 == 0:
                print('Reloading...')
            self.iterator += 1


        vid.click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(2)
            
    def comment(self):
        # click on placeholder
        self.driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[5]/ytd-comment-simplebox-renderer/div[1]').click()
        
        # click on textbox
        self.driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[5]/ytd-comment-simplebox-renderer/div[3]/ytd-comment-dialog-renderer/ytd-commentbox/div/div[2]/paper-input-container/div[2]/div/div[1]/ytd-emoji-input/yt-user-mention-autosuggest-input/yt-formatted-string/div').click()
        
        # input text inside textbox
        self.driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[5]/ytd-comment-simplebox-renderer/div[3]/ytd-comment-dialog-renderer/ytd-commentbox/div/div[2]/paper-input-container/div[2]/div/div[1]/ytd-emoji-input/yt-user-mention-autosuggest-input/yt-formatted-string/div').send_keys(self.message)
        
        # write comment
        self.driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[5]/ytd-comment-simplebox-renderer/div[3]/ytd-comment-dialog-renderer/ytd-commentbox/div/div[4]/div[5]/ytd-button-renderer[2]/a/paper-button').click()

        
def main(): 
    iterator = 0
    bot = combot()
    bot.login()
    bot.go_to_page()
    bot.check_and_refresh()
    bot.comment()

if __name__ == '__main__':
    main()