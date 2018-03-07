from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# name = input('What’s your name?')
# email = input('What’s your email?')
# phone = input('What is your phone number?')
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

for i in validJobs:
    i = 0
    jobs[i] = validJobs[i])
    i = i + 1