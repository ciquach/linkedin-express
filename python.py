from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome() #add driver path 'C:/Users/Cindy Quach/Desktop'

name = input('What’s your name?')
email = input('What’s your email?')
phone = input('What is your phone number?')
title = input('What kind of job are you looking for?')
title.replace(' ', '%20')

page = driver.get('https://www.linkedin.com/jobs/search/?f_LF=f_AL&keywords={}&location=United%20States&locationId=us%3A0'.format(title))

jobs = []
i = 0

element = driver.find_elements_by_css_selector('a')
validJobs = []

for e in element:
    # print(e.get_attribute('href'))
    if '/jobs/view/' in str(e.get_attribute('href')):
        validJobs.append(e.get_attribute('href'))

#test function to print the links. Cindy u can use this loop to traverse 
for i in validJobs:
    i = 0
    print(validJobs[i])
    i = i + 1

for i in validJobs:
    i=0
    driver.find_element_by_link_text(validJobs[i]).click() 
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
    driver.find_element_by_css_selector('div.button.jobs-s-apply_button.js-apply-button ').click()
    addInput()
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
    i = i + 1
