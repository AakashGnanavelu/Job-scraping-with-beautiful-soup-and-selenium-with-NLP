# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 12:16:07 2021

@author: Aakash
"""

from rake_nltk import Rake
import os
os.chdir(r'C:\Users\Aakash\Desktop\AAKASH\Coding Stuff\Python\Project\Linkedin Project')

resume_file = open('resume.txt', 'r', encoding='utf-8')
resume = resume_file.read()
resume_file.close()

rake_nltk_var = Rake()
rake_nltk_var.extract_keywords_from_text(resume)
keyword_extracted = rake_nltk_var.get_ranked_phrases()
