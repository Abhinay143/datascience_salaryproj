# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 13:00:48 2020

@author: ABhI
"""



import glassdoor_scraped as gs
import pandas as pd
path=(r"C:\Users\ABhI\Documents\salary_proj\chromedriver")
df=gs.get_jobs("Data Scientist",10,False,path,15)

df



