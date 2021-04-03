from selenium import webdriver
from time import sleep
import panda as pd

driver = webdriver.Chrome('/usr/local/bin/chromedriver')

driver.get('https://forums.edmunds.com/discussion/2864/general/x/entry-level-luxury-performance-sedans/p100')


comment_ids = []
all_comments = []

ids = driver.find_elements_by_xpath("//*[contains(@id, 'Comment_')]")

for i in ids:
    comment_ids.append(i.get_attribute('id'))

print(comment_ids)

for comment in comment_ids:
    # extract user id
    userid_element = driver.find_element_by_xpath(
        '//*[@id="' + comment + '"]/div/div[2]/div[1]/span[1]/a[2]')
    userid = userid_element.text

    # extract date of the comment
    comment_date = driver.find_element_by_xpath(
        '//*[@id="' + comment + '"]/div/div[2]/div[2]/span/a/time')
    date = comment_date.get_attribute('title')

    # extract actual comment
    comment_text = driver.find_element_by_xpath(
        '//*[@id="' + comment + '"]/div/div[3]/div/div[1]').text

    comment = {
        'user_id': userid,
        'date': date,
        'comment': comment_text
    }
    all_comments.append(comment)

sleep(10)
driver.quit()

print(all_comments)
# print(userid, date, comment_text, sep='\n')
