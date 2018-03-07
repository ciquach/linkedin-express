import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.FireFox()

name = input('What’s your name?')
email = input('What’s your email?')
phone = input('What is your phone number?')
title = input('What kind of job are you looking for?')
title.replace(' ', '%20')

page = driver.get('https://www.linkedin.com/jobs/search/?f_LF=f_AL&keywords={}&location=United%20States&locationId=us%3A0'.format(title))

jobs = []
i = 0
links = driver.find_element_by_css_selector('li>div>div>div>div>a')
for link in links:
    jobs[i] = 'https://www.linkedin.com' + link.get_attribute("href")

# tests
for jobs in jobs:
    print(jobs.at(i))

#EMMA
# jobs = []
# i = 0
# for idk in idk: #until there are no more jobs on the page
#     elem = browser.find_element_by_data-contol-name('A_jobssearch_job_result_click')
#     jobs[i] = elem
#     i = i + 1

#traverse above link for the links to jobs until no more jobs are on page
#data_control_name heref thingy
#push each link into an array, vector, or dictionary? file maybe?








#CINDY
#while the array, vec, whatever u chose to use is not empty
#click the link
# eg. checkout = browser.find_element_by_xpath('//*[@id="cart_checkout_button"]')
#     checkout.click()
#click easy apply button (button is not a link.. ask John)
# fill info #VANESSA 
# repeats for other links ...

