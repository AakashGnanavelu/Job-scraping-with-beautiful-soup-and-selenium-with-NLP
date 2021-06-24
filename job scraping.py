# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 12:26:52 2021

@author: Aakash
"""

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from time import time
import os 

start_time = time()
os.chdir(r"C:\Users\Aakash\Desktop\AAKASH\Coding Stuff\Python\Project\Linkedin Project")

url = 'https://www.linkedin.com/jobs/search/?keywords=senior%20electrical%20engineer'

driver = webdriver.Chrome()
driver.get(url)
sleep(3)
action = ActionChains(driver)

for scroll in range(0, 500):
    sleep(2) # Has time to load
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

source = driver.page_source
soup = BeautifulSoup(source, 'lxml')

job_link = []

for a in soup.find_all('a', 'base-card__full-link',href=True):
    job_link.append(a['href'])
    
raw_job_title = []
raw_company_name = []
raw_location = []
raw_job_description = []
raw_level = []
raw_function = []

for x in range(0, len(job_link)):
    driver.get(job_link[x])
    sleep(2)
      
    job_source = driver.page_source
    soup = BeautifulSoup(job_source, 'lxml')
    
    raw_job_title.append(soup.find('h1', class_='top-card-layout__title topcard__title'))
    raw_company_name.append(soup.find('a', class_ = 'topcard__org-name-link topcard__flavor--black-link'))
    raw_location.append(soup.find('span', class_='topcard__flavor topcard__flavor--bullet'))
    raw_job_description.append(soup.find('div', class_='show-more-less-html__markup show-more-less-html__markup--clamp-after-5'))
    raw_level.append(soup.find('span', class_= "description__job-criteria-text description__job-criteria-text--criteria")) 
    raw_function.append(soup.find('span',class_= 'description__job-criteria-text description__job-criteria-text--criteria'))
    
    sleep(2)
    
driver.close()

len(job_link)
len(raw_job_title)
len(raw_company_name)
len(raw_location)
len(raw_job_description)
len(raw_level)
len(raw_function)

job_title = []
company_name = []
location = []
job_description = []
level = []
function = []

for y in range(0, len(job_link)):
    job_title.append(raw_job_title[y].text)
    company_name.append(raw_company_name[y].text)
    location.append(raw_location[y].text)
    level.append(raw_level[y].text)
    function.append(raw_function[y].text)
    job_description.append(raw_job_description[y].get_text())
    
len(job_title)
len(company_name)
len(location)
len(job_description)
len(level)
len(function)
    
data_dict = {
    'link':job_link,
    'job_title' : job_title,
    'company_name':company_name,
    'location': location,
    'job_description' : job_description,
    'level':level,
    'function':function}

data = pd.DataFrame(data_dict)

