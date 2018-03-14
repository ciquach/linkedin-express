from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#imported for tabs
from selenium.webdriver.common.action_chains import ActionChains
# imported to wait for element to appear before performing an action
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome() #add driver path 'C:/Users/Cindy Quach/Desktop'

# name = input('What’s your name?')
# email = input('What’s your email?')
# phone = input('What is your phone number?')
# title = input('What kind of job are you looking for?')
title = "c# developer"
title.replace(' ', '%20')
# prompt user for resume???

page = driver.get('https://www.linkedin.com/jobs/search/?f_LF=f_AL&keywords={}&location=United%20States&locationId=us%3A0'.format(title))



def login():
   # userEmail = input('Enter your email: ')
   # userPassword = input('Enter your password')
   userEmail = 'johnphammail@gmail.com'
   userPassword = '1qazse4'
   
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

time.sleep(2) # added because page hasn't loaded, can't load links
elements = driver.find_elements_by_css_selector('a')
validJobs = []

for e in elements:
   if '/jobs/view/' in str(e.get_attribute('href')):
       validJobs.append(str(e.get_attribute('href')))

def userProfile():
   time.sleep(3)

   try:
      easyApplyButton = driver.find_element_by_css_selector("button.jobs-s-apply__button")
      easyApplyButton.click()
   except NoSuchElementException:
      easyApplyButton2 = driver.find_element_by_css_selector("button.jobs-apply-form__submit-button")
      easyApplyButton2.click()
   

   N = 8  # number of times you want to press TAB

   actions = ActionChains(driver) 
   for i in range(N):
       actions = actions.send_keys(Keys.TAB)
   actions = actions.send_keys(Keys.ENTER)
   actions.perform()


   
#    useremail = driver.find_element_by_id("apply-form-email-select")
#    userphone = driver.find_element_by_id("apply-form-phone-input")
#    userresume = driver.find_element_by_id("file-browse-input")

   #Imports information into the webiste

#    useremail.send_keys(email)
#    userphone.send_keys(phone)
   # userresume.sendKeys("<absolutePathToMyFile>")

   #This will find the button to submit and click the button
   #Button class jobs-apply-form__submit-button button-primary-large

   # driver.find_element_by_css_selector('.jobs-s-apply').click()

   # click easy apply button
   # easyApply = '//*[@id="ember6833"]/button'
   # driver.find_element_by_xpath('//*[matches(@id, "ember\w*"]/button').click()

for i in range(0, len(validJobs), 2):
   #driver.find_element_by_link_text(validJobs[i]).click()
   #Stack Over Flow: https://stackoverflow.com/questions/18023678/how-to-find-element-by-link-text-while-having-nosuchelement-exception
   # driver.find_element_by_xpath["//a[contains(@href = '{}')]"].format(validJobs[i]).click()
   driver.get(validJobs[i])
   userProfile()

