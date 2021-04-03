from selenium import webdriver
import json

# location of the installation directory of chrome browser
driver = webdriver.Chrome('/usr/local/bin/chromedriver')

driver.get('https://forums.edmunds.com/discussion/2864/general/x/entry-level-luxury-performance-sedans/p100')


# this will hold all the comment id to extract data from them
comment_ids = []

# this list will hold all dict of comment
all_comments = []

# find all element that contains an id='Comment_'
ids = driver.find_elements_by_xpath("//*[contains(@id, 'Comment_')]")

# add all comments in the list
for i in ids:
    comment_ids.append(i.get_attribute('id'))

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

    # make a json like object or dict with each comment
    comment = {
        'user_id': userid,
        'date': date,
        'comment': comment_text
    }

    # add the comment dict in the list
    all_comments.append(comment)


# write the list of dict in a json file
with open('comments.json', 'w') as f:
    f.write(json.dumps(all_comments, indent=4))

# after finishing, quit the driver
driver.quit()
