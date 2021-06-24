# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 14:54:19 2021

@author: Aakash
"""

import job_finder
import os

os.chdir(r'C:\Users\Aakash\Desktop\AAKASH\Coding Stuff\Python\Project\Linkedin Project')
job_data = job_finder.job_find(url = 'https://www.linkedin.com/jobs/search?keywords=Electrical%20Engineering&location=India&locationId=&geoId=102713980&sortBy=R&f_TPR=r604800&f_JT=F&f_E=4%2C5&position=1&pageNum=0', scroll_num = 0)
