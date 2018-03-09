from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

name = input('What’s your name?')
email = input('What’s your email?')
phone = input('What is your phone number?')
title = input('What kind of job are you looking for?')
title.replace(' ', '%20')
# prompt user for resume???

page = driver.get('https://www.linkedin.com/jobs/search/?f_LF=f_AL&keywords={}&location=United%20States&locationId=us%3A0'.format(title))

jobs = []
i = 0

element = driver.find_elements_by_css_selector('a')
validJobs = []

for e in element:
    # print(e.get_attribute('href'))
    if '/jobs/view/' in str(e.get_attribute('href')):
        validJobs.append(e.get_attribute('href'))

def userProfile():
    useremail = driver.find_element_by_id("apply-form-email-select")
    userphone = driver.find_element_by_id("apply-form-phone-input")
    userresume = driver.find_element_by_id("file-browse-input")

    #Imports information into the webiste

    useremail.send_keys(email)
    userphone.send_keys(phone)
    userresume.sendKeys("<absolutePathToMyFile>")

    #This will find the button to submit and click the button
    #Button class jobs-apply-form__submit-button button-primary-large

    driver.find_element_by_xpath('//button[@type="submit"]/span[@class="jobs-apply-form__submit-button button-primary-large"]').click()

for i in validJobs:
    i = 0
    driver.find_element_by_link_text(validJobs[i]).click() 
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
    driver.find_element_by_css_selector('div.button.jobs-s-apply_button.js-apply-button ').click()
    userProfile()
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
    i = i + 1