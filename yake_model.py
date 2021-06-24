# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 12:03:21 2021

@author: Aakash
"""

import yake
import os
os.chdir(r'C:\Users\Aakash\Desktop\AAKASH\Coding Stuff\Python\Project\Linkedin Project')
 
resume_file = open('resume.txt', 'r', encoding='utf-8')
resume = resume_file.read()
resume_file.close()

language = 'en'
max_ngram_size = 3
deduplication_threshold = 0.9
numOfKeywords = 30

custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
keywords = custom_kw_extractor.extract_keywords(resume)

keywords
