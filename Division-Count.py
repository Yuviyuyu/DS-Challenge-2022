import re


import string

from selenium import webdriver
from selenium.webdriver.common.by import By
# browser =webdriver.Chrome()

browser = webdriver.Chrome(executable_path=r"C:\Users\hpcyi\Documents\Data Science\chromedriver.exe")  # Path to where I installed the web driver

browser.get('http://www5.austlii.edu.au/au/legis/nsw/consol_act/capva2007347/')


page_text = browser.find_element_by_xpath("html/body/pre").text
# print(page_tag)

# x=page_text.count("<b>")
# print(x)
    
string_list=[]
c= browser.find_elements(By.XPATH, "//b[contains(text(), 'PART ')]")
for element in c:
    text=element.text
    # print(text)
    string_list.append(text)
# print(string_list)    
    
    
div_list=[]
c= browser.find_elements(By.XPATH, "//b[contains(text(), 'Division ')]")
for element in c:
    text=element.text
    # print(text)
    div_list.append(text)
print(len(div_list))



index_number=[]
for idx in div_list:
    
    if (div_list.count(idx)>1):
        # print(idx)
        index_number=[index for index, div in enumerate(div_list) if div ==idx]
        
# print(index_number)      
div_idx=[]

num=len(div_list[0:index_number[1]])
div_idx.append(num)
num1=len(div_list[index_number[1]:index_number[2]])
div_idx.append(num1) 
num2=len(div_list[index_number[2]:len(div_list)])
div_idx.append(num2) 
# print(div_idx) 
      
n=0
total=[]
for x in range(0,len(string_list)):
    
    if n<len(string_list)-1:
        
        start= page_text.index(string_list[n])
        end = page_text.index(string_list[n+1])
        part= page_text[start:end]
        total.append(part)
                   
    else: 
        n == len(string_list)-1
        start= page_text.index(string_list[n])
        end = len(page_text)
        part= page_text[start:end] 
        total.append(part)  
   
    n=n+1
# print(total)   

div_part=[]
division_part= 'Division '
for div in total:
    if  division_part in div:
        div_part.append(div)
# print(div_part)

a=0
x=0
for div in div_part:
            
    for p in range(div_idx[a]):
        div_count=[] 
        if p< div_idx[a]-1:
           
                
            start= div.index(div_list[x])
            end=div.index(div_list[x+1])
            part=div[start:end]
            # print(part)
            words = part.replace('--',' ').replace('"','').replace('.','').replace('(','').replace(')','').replace(',',' ').split()      
            # print(words)
            for word in words:  
                if word.isalpha():
                    div_count.append(word)
            print(div_count)          
            print(len(div_count))        
        else:
            p==div_idx[a]-1
            start= div.index(div_list[x])
            end=len(div)
            part=div[start:end]
            # print(part)
            words = part.replace('--',' ').replace('"','').replace('.','').replace('(','').replace(')','').replace(',',' ').split()      
            # print(words)
            for word in words:  
                if word.isalpha():
                    div_count.append(word)
            print(div_count)        
            print(len(div_count))
        x=x+1 
                   
                
    a=a+1
  

browser.quit()