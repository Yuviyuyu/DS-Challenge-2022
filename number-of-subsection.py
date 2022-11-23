import re


import string

from selenium import webdriver
from selenium.webdriver.common.by import By
# browser =webdriver.Chrome()

browser = webdriver.Chrome(executable_path=r"C:\Users\hpcyi\Documents\Data Science\chromedriver.exe")  # Path to where I installed the web driver

browser.get('http://www5.austlii.edu.au/au/legis/nsw/consol_act/capva2007347/')

sub_link=[]
s = browser.find_elements(By.XPATH, "html/body/pre/a")
for s in s:
    s=s.get_attribute("name")
    if s!= '':
        sub_link.append(s)
sub_link=sub_link[1:len(sub_link)]
# print(sub_link)
newsub=[]
sub_count=[]
for sub in sub_link:
    ss= sub[-1]
    newsub.append(ss)
    
for character in newsub:
    if character.isalpha():
        sub_count.append(character)
            
# print(newsub)      
# print(sub_count)
print(len(sub_count))
        