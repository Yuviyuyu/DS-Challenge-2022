import re
import io
import string
from string import punctuation
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import nltk
from nltk.tokenize import sent_tokenize
import syllables
import collections
import easygui
import pip._vendor.requests
from collections import Counter
import spacy
# nltk.download('punkt')

# -------------- Enviroment Set UP -------------- # 

browser = webdriver.Chrome(executable_path=r"C:\Users\ysenz\chromedriver.exe")  # Path to chrome driver
browser2 = webdriver.Chrome(executable_path=r"C:\Users\ysenz\chromedriver.exe")  # Path to chrome driver
# userUrl = easygui.enterbox("Copy paste your legal URL here: ")
userUrl = "http://classic.austlii.edu.au/au/legis/act/consol_act/fva2016158/index.html#s115"
browser.get(userUrl)
browser2.get(userUrl)

firstPage = []
chapters = []
parts = []
divisions = []
subdivisions = []
sec_urls = []
sections_titles = []
sections_text = []
sections = []
subsections = []
internalUrls = []
externalUrls = []
uncoverUrls = []
endnote = []
titlelist = []
yearlist = []
# -------------- Define Function to check tag existence -------------- # 
def check_exists_by_xpath(xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

####~~~~~~get the body text~~~~~~#####
page_text = browser.find_elements_by_xpath("//pre")
for element in page_text:
    text = element.text
    # print(text)
    firstPage.append(text)  

# -------------- Find Chapter and put into a list -------------- #   
c = browser.find_elements_by_xpath("//b[contains(text(), 'CHAPTER ')]")
for element in c:
    c_text = element.text
    # print(c_text)
    chapters.append(c_text)  
# print(chapters)
# index_list=[]

# c= browser.find_elements(By.XPATH, "//b[contains(text(), 'CHAPTER ')]")
# for element in c:
#     text=element.text
#     # print(text)
    
#     index_list.append(text)
# print(index_list)

# n=0

# for x in range(0,len(index_list)):
#     total=[]
#     if n<len(index_list)-1:
        
#         start= page_text.index(index_list[n])
#         end = page_text.index(index_list[n+1])
#         part= page_text[start:end]
        
#         words = part.replace('--',' ').replace('"','').replace('.','').replace('(','').replace(')','').replace(',',' ').split()      
#         for word in words:  
#             if word.isalpha():
#                 total.append(word)
#         # print(word)
#         # print(total)
#         print(len(total))
           
        
#     else: 
#         n == len(index_list)-1
#         start= page_text.index(index_list[n])
#         end = len(page_text)
#         part= page_text[start:end]   
#         words = part.replace('--',' ').replace('"','').replace('.','').replace('(','').replace(')','').replace(',',' ').split()      
#         for word in words:  
#             if word.isalpha():
#                 total.append(word)
#         # print(total)
#         print(len(total))
#     n=n+1   

# -------------- Find PART and put into a list -------------- #   
p = browser.find_elements_by_xpath("//b[contains(text(), 'PART ')]")
for element in p:
    p_text = element.text
    # print(p_text)
    parts.append(p_text)  
# print(parts)    
# index_list=[]

# c= browser.find_elements(By.XPATH, "//b[contains(text(), 'PART ')]")
# for element in c:
#     text=element.text
#     # print(text)
#     d= text[0:8]
#     index_list.append(d)
# n=0

# for x in range(0,len(index_list)):
#     total=[]
#     if n<len(index_list)-1:
        
#         start= page_text.index(index_list[n])
#         end = page_text.index(index_list[n+1])
#         part= page_text[start:end]
        
#         words = part.replace('--',' ').replace('"','').replace('.','').replace('(','').replace(')','').replace(',',' ').split()      
#         for word in words:  
#             if word.isalpha():
#                 total.append(word)
#         # print(word)
#         print(len(total))
           
        
#     else: 
#         n == len(index_list)-1
#         start= page_text.index(index_list[n])
#         end = len(page_text)
#         part= page_text[start:end]   
#         words = part.replace('--',' ').replace('"','').replace('.','').replace('(','').replace(')','').replace(',',' ').split()      
#         for word in words:  
#             if word.isalpha():
#                 total.append(word)
#         # print(total)
#         print(len(total))
#     n=n+1   

# num_p = len(parts) + len(sections)
# print("Task 2. PART Word Count: ", num_p)
# -------------- Find Division and put into a list -------------- #     
d = browser.find_elements_by_xpath("//b[contains(text(), 'Division ')]")
for element in d:
    d_text = element.text
    # print(d_text)
    divisions.append(d_text)  
# if "nsw" in userUrl:
#     ####~~~~~~~~~~~~~get the PART title into a list~~~~~~~~~~~~####   
#     string_list=[]
#     c= browser.find_elements(By.XPATH, "//b[contains(text(), 'PART ')]")
#     for element in c:
#         text=element.text
#         # print(text)
#         string_list.append(text)
#     # print(string_list)    
        
#     ####~~~~~~~~~~~~~get the Division title into a list~~~~~~~~~~~~####      
#     div_list=[]
#     c= browser.find_elements(By.XPATH, "//b[contains(text(), 'Division ')]")
#     for element in c:
#         text=element.text
#         # print(text)
#         div_list.append(text)
#     print(len(div_list))


#     ####~~~~~~~~~~~~~find the duplicated division title and index their positions~~~~~~~~~~~~####  
#     index_number=[]
#     for idx in div_list:
        
#         if (div_list.count(idx)>1):
#             # print(idx)
#             index_number=[index for index, div in enumerate(div_list) if div ==idx]
            
#     # print(index_number)      

#     ####~~~~~~~~~~~~~slice Division titles into 3 parts~~~~~~~~~~~~####  
#     div_idx=[]

#     num=len(div_list[0:index_number[1]])
#     div_idx.append(num)
#     num1=len(div_list[index_number[1]:index_number[2]])
#     div_idx.append(num1) 
#     num2=len(div_list[index_number[2]:len(div_list)])
#     div_idx.append(num2) 
#     # print(div_idx) 

#     ####~~~~~~~~~~~~~get the all PARTs ~~~~~~~~~~~~####  
#     n=0
#     total=[]
#     for x in range(0,len(string_list)):
        
#         if n<len(string_list)-1:
            
#             start= page_text.index(string_list[n])
#             end = page_text.index(string_list[n+1])
#             part= page_text[start:end]
#             total.append(part)
                    
#         else: 
#             n == len(string_list)-1
#             start= page_text.index(string_list[n])
#             end = len(page_text)
#             part= page_text[start:end] 
#             total.append(part)  
    
#         n=n+1
#     # print(total)   

#     ####~~~~~~~~~~~~~find which part has division~~~~~~~~~~~~####  
#     div_part=[]
#     division_part= 'Division '
#     for div in total:
#         if  division_part in div:
#             div_part.append(div)
#     # print(div_part)

#     ####~~~~~~~~~~~~~locate divisions in each part and count word per division ~~~~~~~~~~~~####  
#     a=0
#     x=0
#     for div in div_part:
                
#         for p in range(div_idx[a]):
#             div_count=[] 
#             if p< div_idx[a]-1:
            
                    
#                 start= div.index(div_list[x])
#                 end=div.index(div_list[x+1])
#                 part=div[start:end]
#                 # print(part)
#                 words = part.replace('--',' ').replace('"','').replace('.','').replace('(','').replace(')','').replace(',',' ').split()      
#                 # print(words)
#                 for word in words:  
#                     if word.isalpha():
#                         div_count.append(word)
#                 print(div_count)          
#                 print(len(div_count))        
#             else:
#                 p==div_idx[a]-1
#                 start= div.index(div_list[x])
#                 end=len(div)
#                 part=div[start:end]
#                 # print(part)
#                 words = part.replace('--',' ').replace('"','').replace('.','').replace('(','').replace(')','').replace(',',' ').split()      
#                 # print(words)
#                 for word in words:  
#                     if word.isalpha():
#                         div_count.append(word)
#                 print(div_count)        
#                 print(len(div_count))
#             x=x+1 
                    
                    
#         a=a+1
# else:
# num_div = len(divisions) + len(sections)
# print("Task 2. DIVISION Word Count: ", num_div)
# -------------- Find Subdivision and put into a list -------------- #        
sub = browser.find_elements_by_xpath("//b[contains(text(), 'Subdivision ')]")

for element in sub:
    sd_text = element.text
    # print(sd_text)
    subdivisions.append(sd_text)
# print(subdivisions)
# if "nsw" in userUrl:
#     string_list=[]
#     c= browser.find_elements(By.XPATH, "//b[contains(text(), 'PART ')]")
#     for element in c:
#         text=element.text
#         # print(text)
#         string_list.append(text)
#     # print(string_list)    
        
        
#     div_list=[]
#     c= browser.find_elements(By.XPATH, "//b[contains(text(), 'Division ')]")
#     for element in c:
#         text=element.text
#         # print(text)
#         div_list.append(text)
#     print(len(div_list))



#     index_number=[]
#     for idx in div_list:
        
#         if (div_list.count(idx)>1):
#             # print(idx)
#             index_number=[index for index, div in enumerate(div_list) if div ==idx]
            
#     # print(index_number)      
#     div_idx=[]

#     num=len(div_list[0:index_number[1]])
#     div_idx.append(num)
#     num1=len(div_list[index_number[1]:index_number[2]])
#     div_idx.append(num1) 
#     num2=len(div_list[index_number[2]:len(div_list)])
#     div_idx.append(num2) 
#     # print(div_idx) 
        
        
        
        
#     sub_list=[]
#     sub= browser.find_elements(By.XPATH, "//b[contains(text(), 'Subdivision ')]")
#     for element in sub:
#         text=element.text
#         text=text[0:len('Subdivision ')+1]
#         sub_list.append(text)

#     # print(sub_list)
#     sub_index=[]  
#     for sub in sub_list:
#         if (sub_list.count('Subdivision 1')>1):
#             sub_index=[index for index, s in enumerate(sub_list) if s == 'Subdivision 1']
        
#     # print(sub_index)    
#     #~~~~~~~~~~~~~~find loop range for subdivision~~~~~~~~~#
#     sub_idx=[]
#     no1=len(sub_list[0:sub_index[1]])
#     sub_idx.append(no1)
#     no2=len(sub_list[sub_index[1]:len(sub_list)])
#     sub_idx.append(no2)
#     # print(sub_idx)

#     n=0
#     total=[]
#     for x in range(0,len(string_list)):
        
#         if n<len(string_list)-1:
            
#             start= page_text.index(string_list[n])
#             end = page_text.index(string_list[n+1])
#             part= page_text[start:end]
#             total.append(part)
                    
#         else: 
#             n == len(string_list)-1
#             start= page_text.index(string_list[n])
#             end = len(page_text)
#             part= page_text[start:end] 
#             total.append(part)  
    
#         n=n+1
#     # print(total)   

#     ###~~~~~~~~~~~~~~`find which part has division and subdivision  ~~~~~######`
#     sub_part='Subdivision'


#     division_part= 'Division '

#     div_part=[]
#     for div in total:
#         if  division_part  in div:
#             div_part.append(div)
#     # print(div_part)


#     sub_div_list=[]
#     a=0
#     x=0
#     for div in div_part:
                
#         for p in range(div_idx[a]):
#             div_count=[] 
#             if p< div_idx[a]-1:
            
                    
#                 start= div.index(div_list[x])
#                 end=div.index(div_list[x+1])
#                 part=div[start:end]
#                 # print(part)
#                 if sub_part in part:
#                     sub_div_list.append(part)
                
                
#             else:
#                 p==div_idx[a]-1
#                 start= div.index(div_list[x])
#                 end=len(div)
#                 part=div[start:end]
#                 if sub_part in part:
#                     sub_div_list.append(part)
            
            
#             x=x+1 
                    
                    
#         a=a+1
    
#     # print(sub_div_list)

#     e=0
#     d=0
#     for sub in sub_div_list:
#         for sd in range(sub_idx[e]):
            
#             sub_count=[]
#             if sd <  sub_idx[e]-1:
#                 first = sub.index(sub_list[d])
#                 last= sub.index(sub_list[d+1])
#                 sd_part=sub[first:last]
#                 print(sd_part)
#                 words = sd_part.replace('--',' ').replace('"','').replace('.','').replace('(','').replace(')','').replace(',',' ').split()      
#                 # print(words)
#                 for word in words:  
#                     if word.isalpha():
#                         sub_count.append(word)
#                 print(sub_count)        
#                 print(len(sub_count))
#             else:
#                 sd = sub_idx[e]-1
#                 first=sub.index(sub_list[d])
#                 last= len(sub)
#                 sd_part=sub[first:last]
#                 print(sd_part)
#                 words = sd_part.replace('--',' ').replace('"','').replace('.','').replace('(','').replace(')','').replace(',',' ').split()      
#                 # print(words)
#                 for word in words:  
#                     if word.isalpha():
#                         sub_count.append(word)
#                 print(sub_count)        
#                 print(len(sub_count))
#             d=d+1
        
#         e=e+1
# else:
# num_subdiv = len(subdivisions) + len(sections)
# print("Task 2. SUBDIVISION Word Count: ", num_subdiv)

# -------------- Find section URL and put into a list -------------- #   
su = browser.find_elements_by_xpath("//pre/a[contains(@href,'s') and not(contains(@href, '#'))]")
for element in su:
    links = element.get_attribute("href")
    sec_urls.append(links)
# print(sec_urls)
# ##~~~~~~~~number of section~~~~~~~~~~~~~~~~##
# if "nsw" in userUrl:
#     s_link =sec_urls[1:len(sec_urls)]
#     # print(len(s_link))
#     n=0

#     for link in range(len(sec_urls)):
#         n=n+1
#         section_count=[]
#         new=''
#         driver.get(s_link[n])


#         ss=driver.find_element_by_xpath("html/body").get_attribute("outerHTML")
#         for s in ss:
        
#             new=new+s

#     # print(new)

#         tag="b"
#         b_section="<"+ tag +">(.*?)</"+tag+">"
#         section = re.findall(b_section,new)
#         first_section=str(section[0])
#         for word in first_section:
#             section_count=first_section.split()
        
        # print(section_count)        
# num_sec = len(sections)
# print("Task 2. SECTION Word Count: ", num_sec)
        
# -------------- Find internal references in first page -------------- #  
int = browser.find_elements_by_xpath("//a[@class='autolink_findacts']")
for element in int:
    text = element.text
    internalUrls.append(text)
# print(internalUrls) 

# -------------- Find external references in first page  -------------- #  
ext = browser.find_elements_by_xpath("//a[@class='autolink_findacts' and (contains(text(), 'Act') or contains(text(), 'ACT'))]")
for element in ext:
    text = element.text
    externalUrls.append(text)
# print(externalUrls)

# -------------- Find  all references in first page -------------- #  
un = browser.find_elements_by_xpath("//a[@class='autolink_findacts']")
for element in un:
    text = element.text
    uncoverUrls.append(text)
       
# -------------- Read each subpage content -------------- #   
for url in sec_urls:
    browser.get(url)
    # -------------- Extra section contents -------------- #   
    t = browser.find_elements_by_xpath("//*[self::h3 or self::h4 or self::b]")
    for element in t:
        title = element.text
        # print(title)
        sections_titles.append(title)
    # print(sections_titles)
    
    # -------------- Define if/else statement -------------- # 
    if (check_exists_by_xpath("//blockquote") == True):
        tt2 = browser.find_elements_by_xpath("//blockquote")
        for element in tt2:
            text = element.text
            # print(text)
            sections_text.append(text)
    else:
        tt = browser.find_elements_by_xpath("//p[@class='cause']")
        for element in tt:
            text = element.text
            # print(text)
            sections_text.append(text)
    # print(sections_text)
    
    sections = sections_titles + sections_text
# print(sections)
 # -------------- Find subsections -------------- #
    if (check_exists_by_xpath("//blockquote") == True):
        tt3 = browser.find_elements_by_xpath("//blockquote[contains(text(), '(1)') or contains(text(), '(2)') or contains(text(), '(3)') or contains(text(), '(4)') or contains(text(), '(5)')]")
        for element in tt3:
            text = element.text
            subsections.append(text)
    else:
        tt4 = browser.find_elements_by_xpath("//p[contains(text(), '(1)') or contains(text(), '(2)') or contains(text(), '(3)') or contains(text(), '(4)') or contains(text(), '(5)')]")
        for element in tt4:
            text = element.text
            subsections.append(text)
    
    # -------------- Check internal cross references in section page-------------- # 
    if (check_exists_by_xpath("//blockquote") == True):
        url2 = browser.find_elements_by_xpath("//blockquote/a[@class='autolink_findacts']")
        for element in url2:
            links = element.text
            internalUrls.append(links)
    else:
        url1 = browser.find_elements_by_xpath("//p/a[@class='autolink_findacts']")
        for element in url1:
            links = element.text
            internalUrls.append(links)
# print(internalUrls)

  # -------------- Check external cross references in section page-------------- # 
    if (check_exists_by_xpath("//blockquote") == True):
        url4 = browser.find_elements_by_xpath("//blockquote/a[@class='autolink_findacts' and (contains(text(), 'Act') or contains(text(), 'ACT'))]")
        for element in url4:
            text = element.text
            externalUrls.append(text)
    else:
        url3 = browser.find_elements_by_xpath("//p/a[@class='autolink_findacts' and (contains(text(), 'Act') or contains(text(), 'ACT'))]")
        for element in url3:
            text = element.text
            externalUrls.append(text)
# print(externalUrls)

# -------------- Find  all references in first page -------------- #  
    if (check_exists_by_xpath("//blockquote") == True):
        un1 = browser.find_elements_by_xpath("//a[@class='autolink_findacts']")
        for element in un1:
            text = element.text
            uncoverUrls.append(text)
    else:
        un2 = browser.find_elements_by_xpath("//a[@class='autolink_findacts']")
        for element in un2:
            text = element.text
            uncoverUrls.append(text)
       
# -------------- Define word count -------------- #      
def countWords(listName):
    listName = ''.join(listName).replace("--", " ").replace("&nbsp;", " ").replace("\n", " ").replace("—", " ").translate(str.maketrans('','',string.punctuation))
    listName_count = len(listName.split())
    return listName_count

# -------------- Task 1 to 3 Word count of a legislative text  -------------- #    
totalWords = countWords(firstPage) + countWords(sections) + countWords(subsections)
print("Task 1. Total legislative words: ", totalWords)

print("Task 3. Number of Sections: ", len(sec_urls)) 
# print(sec_urls)
print("Task 3. Number of Subsections: ", len(subsections))

# -------------- Task 4 to 5 Enactment Year and Years/Frequencies of Amendents  -------------- # 

if 'nt' in userUrl:
    title = browser2.find_element_by_xpath("html/body/h3").text
    s_title=title.split()
    year= s_title[-1]
    print("Task 4. Legislation Enactment Year: ", year)
    
    endnote = browser2.find_element_by_xpath("//a[contains(@href,'endnotes')]").get_attribute("href")
    browser2.get(endnote)
    
    title=browser2.find_element_by_xpath("html/body/h3").text
    title_split=title.split()
    new_title=title_split[0:-4]
    new_title=(' '.join(new_title)).lower()
    
    print(new_title)

    abbr= browser2.find_elements(By.XPATH, "html//body//p//table//tbody//tr//td//p//b//i[contains(text(), new_title )]")
    for element in abbr:
        text=element.text
        titlelist.append(text)
    print("Amendment Frequencies in NT: ", len(titlelist)-1)   
    for li in titlelist:
        li=li.split()
        new_li=li[-1]
        yearlist.append(new_li)
    print("List of Years of amendents in NT: ", yearlist)
    
elif 'vic' in userUrl:
    title = browser2.find_element_by_xpath("html/body/h3").text
    s_title=title.split()
    year= s_title[-1]
    print("Task 4. Legislation Enactment Year: ", year)
 
    endnote = browser2.find_element_by_xpath("//a[contains(@href,'endnotes')]").get_attribute("href")
    browser2.get(endnote)
    
    b_list= browser2.find_elements(By.XPATH, "html//body//p//font//b")
    for b in b_list:
        b=b.text
        if  b != 'Family Violence Protection Act 2008':
            titlelist.append(b)
    amend_list=titlelist[18:]
    print("Amendment Frequencies in VIC: ", len(amend_list)-1)
    # print(amend_list)
    
    for al in amend_list:
        new_li=al[-4:]
        yearlist.append(new_li)
    print("List of Years of amendents in VIC: ", yearlist)
    
elif '2016158' in userUrl:
    title = browser2.find_element_by_xpath("html/body/h3").text
    s_title=title.split()
    year= s_title[-1]
    print("Task 4. Legislation Enactment Year: ", year)
    
    endnote = browser2.find_element_by_xpath("//a[contains(@href,'endnotes')]").get_attribute("href")
    browser2.get(endnote)
  
    b_list= browser2.find_elements(By.XPATH, "html/body/p/font/b")
    for b in b_list:
        b=b.text
        titlelist.append(b)
    print("Amendment Frequencies in ACT: ", len(titlelist)-1)
    for li in titlelist:
        new=li.split()
        for y in new:
            if y.isnumeric():
                if len(y)==4:
                    yearlist.append(y)
    print("List of Years of amendents in ACT: ", yearlist) 
    
else:
    print("No endnotes to find amendent hitosry!") 
    
browser2.quit()

# -------------- Task 6 Calculate Flesch Reading Ease score -------------- #    

sectionSentences = '. '.join(sections)
subsectionSentences = '.'.join(subsections)
firstPageSentences = '.'.join(firstPage)
# print('1st sentence', firstPageSentences)
firstPageWords = firstPageSentences.translate(str.maketrans('','',string.punctuation)).replace("-", " ").replace("&nbsp;", " ").replace("\n", " ").replace("|", " ").replace("—", " ")
sectionWords = sectionSentences.translate(str.maketrans('','',string.punctuation)).replace("-", " ").replace("&nbsp;", " ").replace("\n", " ").replace("|", " ").replace("—", " ")
subsectionWords = subsectionSentences.translate(str.maketrans('','',string.punctuation)).replace("-", " ").replace("&nbsp;", " ").replace("\n", " ").replace("|", " ").replace("—", " ")
# print('1st word', firstPageWords)
# print(len(sent_tokenize(sectionSentences)))
nlp = spacy.load('en_core_web_sm')

# print('sec word',len(list(nlp(firstPageSentences).sents)))

# print(totalWords)
# totalSentences = len(sent_tokenize(sectionSentences)) + len(sent_tokenize(subsectionSentences)) +len(sent_tokenize(firstPageSentences))
totalSentences = len(list(nlp(firstPageSentences).sents)) + len(list(nlp(sectionSentences).sents)) + len(list(nlp(subsectionSentences).sents))
# print(totalSennces)

firstPgSyll = 0
sectionSyll = 0
subsecSyll = 0

for word in firstPageWords.split():
    n = syllables.estimate(word)
    firstPgSyll += n
for word in sectionWords.split():
    n = syllables.estimate(word)
    sectionSyll += n
for word in subsectionWords.split():
    n = syllables.estimate(word)
    subsecSyll += n
totalSyllables = firstPgSyll + sectionSyll + subsecSyll
# print(totalSyllables)

def FRES(totalWords, totalSentences, totalSyllables):
    score = 206.835 - 1.015*(totalWords/totalSentences) - 84.6*(totalSyllables/totalWords)
    return score
print("Task 6. Flesch Reading Ease Score: ", FRES(totalWords, totalSentences, totalSyllables))
# -------------- Task 7 to 9 Find Internal / External / Uncovered cross-references -------------- #

NumofExternal = len(externalUrls) 
print(externalUrls)
NumofInternal = len(internalUrls) -NumofExternal
print(internalUrls)
NumofUncover = len(uncoverUrls) - NumofExternal -NumofInternal


print("Task 7. Number of Internal Cross-references: ", NumofInternal)    
print("Task 8. Number of External Cross-references: ", NumofExternal)
print("Task 9. Number of Uncoover Cross-references: ", NumofUncover)


browser.quit()
