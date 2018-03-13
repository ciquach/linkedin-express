from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# imported to wait for element to appear before performing an action
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome() #add driver path 'C:/Users/Cindy Quach/Desktop'

# name = input('What’s your name?')
# email = input('What’s your email?')
# phone = input('What is your phone number?')
# title = input('What kind of job are you looking for?')
title = "software"
title.replace(' ', '%20')
# prompt user for resume???

page = driver.get('https://www.linkedin.com/jobs/search/?f_LF=f_AL&keywords={}&location=United%20States&locationId=us%3A0'.format(title))



def login():
   # userEmail = input('Enter your email: ')
   # userPassword = input('Enter your password')
   userEmail = ''
   userPassword = ''
   
   signIn = '//*[@id="mobile-chrome"]/nav/div/ul/li[1]/a'
   driver.find_element_by_xpath(signIn).click()
  
   formEmail = '//*[@id="session_key-login"]'
   formPassword = '//*[@id="session_password-login"]'
   formSubmit = '//*[@id="btn-primary"]'

   form = WebDriverWait(driver, 20).until(
       EC.element_to_be_clickable((By.XPATH, formEmail))
   )

   driver.find_element_by_xpath(formEmail).send_keys(userEmail)
   driver.find_element_by_xpath(formPassword).send_keys(userPassword)
   driver.find_element_by_xpath(formSubmit).click()


login()

#ISSUE IS HERE. ELEMENT IS NOT GETTING THE LINKS ANYMORE **********************
# HARD CODE LOGIN INFO TO TEST
element = driver.find_elements_by_css_selector('a')
validJobs = []

for e in element:
   if '/jobs/view/' in str(e.get_attribute('href')):
       validJobs.append(str(e.get_attribute('href')))
 

def userProfile():
   useremail = driver.find_element_by_id("apply-form-email-select")
   userphone = driver.find_element_by_id("apply-form-phone-input")
   userresume = driver.find_element_by_id("file-browse-input")

   #Imports information into the webiste

   useremail.send_keys(email)
   userphone.send_keys(phone)
   # userresume.sendKeys("<absolutePathToMyFile>")

   #This will find the button to submit and click the button
   #Button class jobs-apply-form__submit-button button-primary-large

   # driver.find_element_by_css_selector('.jobs-s-apply').click()

   # click easy apply button
   # easyApply = '//*[@id="ember6833"]/button'
   # driver.find_element_by_xpath('//*[matches(@id, "ember\w*"]/button').click()

for i in range(len(validJobs)):
   #driver.find_element_by_link_text(validJobs[i]).click()
   #Stack Over Flow: https://stackoverflow.com/questions/18023678/how-to-find-element-by-link-text-while-having-nosuchelement-exception
   # driver.find_element_by_xpath["//a[contains(@href = '{}')]"].format(validJobs[i]).click()
   driver.get(validJobs[i])
   userProfile()

