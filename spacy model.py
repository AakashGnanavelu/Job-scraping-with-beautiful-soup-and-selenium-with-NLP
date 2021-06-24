# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 11:07:54 2021

@author: Aakash
"""

import en_core_web_md
import en_core_web_lg
import os
os.chdir(r'C:\Users\Aakash\Desktop\AAKASH\Coding Stuff\Python\Project\Linkedin Project')
 
resume_file = open('resume.txt', 'r', encoding='utf-8')
resume = resume_file.read()
resume_file.close()

nlp_md = en_core_web_md.load()
nlp_lg = en_core_web_lg.load()

doc_md = nlp_md(resume)
result_md = list(doc_md.ents)

doc_lg = nlp_lg(resume)
resume_lg = list(doc_lg.ents)

resume_lg