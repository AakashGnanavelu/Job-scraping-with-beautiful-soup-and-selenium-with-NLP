# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 12:30:53 2021

@author: Aakash
"""

from gensim.summarization import keywords
import os
os.chdir(r'C:\Users\Aakash\Desktop\AAKASH\Coding Stuff\Python\Project\Linkedin Project')

resume_file = open('resume.txt', 'r', encoding='utf-8')
resume = resume_file.read()
resume_file.close()

keyword = keywords(resume)
result = keyword.split()
