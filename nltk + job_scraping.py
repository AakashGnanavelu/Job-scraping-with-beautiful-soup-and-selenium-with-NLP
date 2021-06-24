# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 12:45:43 2021

@author: Aakash
"""
import os 
import re
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from time import time
import yake
import spacy
from rake_nltk import Rake
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from statistics import mean

start_time = time()
os.chdir(r"C:\Users\Aakash\Desktop\AAKASH\Coding Stuff\Python\Project\Linkedin Project")

url = 'https://www.linkedin.com/jobs/search?keywords=Senior%20Electrical%20Engineer&location=India&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0&f_TPR=r604800'
nlp = spacy.load('en_core_web_lg')

driver = webdriver.Chrome()
driver.get(url)
sleep(3)
action = ActionChains(driver)

scroll_num = 0
for scroll in range(0, scroll_num):
    try:
        element = driver.find_element_by_link_text("See more jobs")
        action.click(element).preform()
        #See More Jobs Button si not being clicked 
    except:
        sleep(2) # Has time to load
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

source = driver.page_source
soup = BeautifulSoup(source, 'lxml')

job_link = []

for a in soup.find_all('a', 'base-card__full-link',href=True):
    job_link.append(a['href'])
    
class WebLinkError(Exception):
    def __init__(self, link, message='is a invalid Linkedin url!'):
        self.link = link
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.link} {self.message}'
    
class AakashError(Exception):
    def __init__(self, message = 'Aakash has completed you code, now bring Aakash his donuts'):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f"{self.message}"

raw_job_title = []
raw_company_name = []
raw_location = []
raw_job_description = []
raw_level = []
raw_function = []

for x in range(0, len(job_link)):
    driver.get(job_link[x])
    sleep(2)
    
    url_count = 0 
    url_flag = True
    while url_flag == True:
        current_url = driver.current_url
        if current_url != job_link[x]:
            driver.get(job_link[x])
            url_count =+ 1
        else: 
            url_flag = False
        if url_count == 10:
            raise WebLinkError(job_link[x])
    
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

if len(job_link) == len(raw_job_title) == len(raw_company_name) == len(raw_location) == len(raw_job_description) == len(raw_level) ==len(raw_function):
    pass
else:
    raise ValueError("Lengh of job information list is mismatched.")
    
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

len(job_link)
len(job_title)
len(company_name)
len(location)
len(job_description)
len(level)
len(function)

if len(job_link) == len(job_title) == len(company_name) == len(location) == len(job_description) == len(level) ==len(function):
    pass
else:
    raise ValueError("Lengh of job information list is mismatched.")
    
for x in range(0, len(job_description)):
    job_description[x] = re.sub("[^A-Za-z" "]+"," ",job_description[x]).lower()
    job_description[x] = re.sub("[0-9" "]+"," ", job_description[x])

resume_file = open('resume.txt', 'r', encoding='utf-8')
resume = resume_file.read()
resume_file.close()

resume = re.sub("[^A-Za-z" "]+"," ",resume).lower()
resume = re.sub("[0-9" "]+"," ", resume)

dict_file = open('dict.txt', 'r', encoding='utf-8')
dict = dict_file.read()
dict_file.close()

raw_dict = re.sub("[^A-Za-z" "]+"," ",dict).lower()
raw_dict = re.sub("[0-9" "]+"," ", dict)

stop_words = set(stopwords.words('english'))
dict_tokens = word_tokenize(raw_dict)

dict = []
for w in dict_tokens:
    if w not in stop_words:
        dict.append(w)
    
language = 'en'
max_ngram_size = 3
deduplication_threshold = 0.5
numOfKeywords = 30

custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
rake_nltk_var = Rake()

raw_yake_job_keyword = []
rake_job_keyword = []

for z in range(0, len(job_link)):
    raw_yake_job_keyword.append(list(custom_kw_extractor.extract_keywords(job_description[z])))
    rake_nltk_var.extract_keywords_from_text(job_description[z])
    rake_job_keyword.append(rake_nltk_var.get_ranked_phrases())

for list_num in range(0, len(rake_job_keyword)):
    
    filtered_sentence = []
    for word_num in range(0, len(rake_job_keyword[list_num])):
        keyword_phrase = rake_job_keyword[list_num][word_num]
        word_tokens = word_tokenize(keyword_phrase)
        
        filter_sentence = []
        for w in word_tokens:
            
            doc = nlp(w)
            if doc[0].tag_ == 'NNP':
                proper = True
            else:
                proper = False
            
            if w in dict:
                in_dict = True
            else:
                in_dict = False
                
            if w not in stop_words and proper == False and in_dict == True:
                filter_sentence.append(w)
            
        filtered_sentence.append(filter_sentence)
    
   
    synonyms = []
    for filtered_num in range(0, len(filtered_sentence)):
        for filtered_word in range(0, len(filtered_sentence[filtered_num])):
            word_synonym = []
            for syn in wordnet.synsets(filtered_sentence[filtered_num][filtered_word]):
                for l in syn.lemmas():
                    syn_word = l.name()
                    try:
                        syn_word = syn_word.replace("_", " ")
                    except:
                        pass
                    word_synonym.append(syn_word)
            synonyms.append(word_synonym)
    for num in range(0, len(rake_job_keyword[list_num])):
        rake_job_keyword[list_num][num] = synonyms[num]


yake_job_keyword = []
for f in range(0, len(job_link)):
    yake_job = []
    for word in raw_yake_job_keyword[f]:
        yake_job.append(word[0])
    yake_job_keyword.append(yake_job)
    
for list_num in range(0, len(yake_job_keyword)):
    
    filtered_sentence = []
    for word_num in range(0, len(yake_job_keyword[list_num])):
        keyword_phrase = yake_job_keyword[list_num][word_num]
        word_tokens = word_tokenize(keyword_phrase)
        
        filter_sentence = []
        for w in word_tokens:
            
            doc = nlp(w)
            if doc[0].tag_ == 'NNP':
                proper = True
            else:
                proper = False
            
            if w in dict:
                in_dict = True
            else:
                in_dict = False
                
            if w not in stop_words and proper == False and in_dict == True:
                filter_sentence.append(w)
            
        filtered_sentence.append(filter_sentence)
    
   
    synonyms = []
    for filtered_num in range(0, len(filtered_sentence)):
        for filtered_word in range(0, len(filtered_sentence[filtered_num])):
            word_synonym = []
            for syn in wordnet.synsets(filtered_sentence[filtered_num][filtered_word]):
                for l in syn.lemmas():
                    syn_word = l.name()
                    try:
                        syn_word = syn_word.replace("_", " ")
                    except:
                        pass
                    word_synonym.append(syn_word)
            synonyms.append(word_synonym)
    for num in range(0, len(yake_job_keyword[list_num])):
        yake_job_keyword[list_num][num] = synonyms[num]

def calculate_percentage(num, length):
    decimal = num / length
    return  decimal*100

yake_percent = []
rake_percent = []
avg_percent = []

for q in range(0, len(job_link)):
    rake_point = 0
    for keyword in rake_job_keyword[q]:
        for key in keyword:
            if key in resume:
                rake_point += 1
                break
    rake_percent.append(calculate_percentage(rake_point, len(rake_job_keyword[q])))
    
for q in range(0, len(job_link)):
    yake_point = 0
    for keyword in yake_job_keyword[q]:
        for key in keyword:
            if key in resume:
                yake_point += 1 
                break
    yake_percent.append(calculate_percentage(yake_point, len(yake_job_keyword[q])))
    
for g in range(0, len(job_link)):
    avg_percent.append(mean([yake_percent[g], rake_percent[g]]))
    
data_dict = {
    'link':job_link,
    'job_title' : job_title,
    'company_name':company_name,
    'location': location,
    'job_description' : job_description,
    'yake_keywords' : yake_job_keyword,
    'rake_keywords' : rake_job_keyword,
    'level':level,
    'function':function,
    'yake_percent': yake_percent,
    'rake_percent': rake_percent,
    'avg_percent': avg_percent}

data = pd.DataFrame(data_dict)
data = data.sort_values(by = 'avg_percent')
