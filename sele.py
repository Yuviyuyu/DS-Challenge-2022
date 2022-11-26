import re
import io
import string
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import nltk
from nltk.tokenize import sent_tokenize
import syllables
# browser =webdriver.Chrome()

browser = webdriver.Chrome(executable_path=r"C:\Users\ysenz\chromedriver.exe")  # Path to where I installed the web driver
browser.get('http://www5.austlii.edu.au/au/legis/nsw/consol_act/capva2007347/')

chapters = []
parts = []
divisions = []
subdivisions = []
sec_urls = []
sections_titles = []
sections_text = []
sections = []
####~~~~~~get the body text~~~~~~#####
page_text = browser.find_element_by_xpath("html/body/pre").text
# print(page_text)

# -------------- Find Chapter and put into a list -------------- #   
c = browser.find_elements_by_xpath("//b[contains(text(), 'CHAPTER ')]")
for element in c:
    c_text = element.text
    # print(c_text)
    chapters.append(c_text)  
# print(chapters)

# -------------- Find PART and put into a list -------------- #   
p = browser.find_elements_by_xpath("//b[contains(text(), 'PART ')]")
for element in p:
    p_text = element.text
    # print(p_text)
    parts.append(p_text)  
# print(parts)    

# -------------- Find Division and put into a listt -------------- #     
d = browser.find_elements_by_xpath("//b[contains(text(), 'Division ')]")
for element in d:
    d_text = element.text
    # print(d_text)
    divisions.append(d_text)
# print(divisions)

# -------------- Find Subdivision and put into a list -------------- #        
sd = browser.find_elements_by_xpath("//b[contains(text(), 'Subdivision ')]")

for element in sd:
    sd_text = element.text
    # print(sd_text)
    subdivisions.append(sd_text)
# print(subdivisions)

# # -------------- Find section URL and put into a list -------------- #   
# su = browser.find_elements_by_xpath("//pre/a[@href]")
# for element in su:
#     links = element.get_attribute("href")
#     sec_urls.append(links)

# # -------------- Read each subpage content -------------- #   
# for url in sec_urls:
#     browser.get(url)
#     # -------------- Extra section contents -------------- #   
#     t = browser.find_elements_by_xpath("//*[self::h3 or self::h4 or self::b]")
#     for element in t:
#         title = element.text
#         # print(title)
#         sections_titles.append(title)
#     # print(sections_titles)
    
#     # -------------- Section text has two formats, define a funtion to set up if /else statement to include both formats -------------- # 
#     def check_exists_by_xpath(xpath):
#         try:
#             browser.find_element_by_xpath(xpath)
#         except NoSuchElementException:
#             return False
#         return True
#     # -------------- Define if/else statement -------------- # 
#     if (check_exists_by_xpath("//blockquote") == True):
#         tt2 = browser.find_elements_by_xpath("//blockquote")
#         for element in tt2:
#             text = element.text
#             # print(text)
#             sections_text.append(text)
#     else:
#         tt = browser.find_elements_by_xpath("//p[@class='clause']")
#         for element in tt:
#             text = element.text
#             # print(text)
#             sections_text.append(text)
#     # print(sections_text)

#     sections = sections_titles + sections_text
#     print(sections)

browser.quit()

# -------------- Count words for chapters and parts -------------- #      
def countWords(listName):
    listName = ' '.join(listName).replace("--", " ").translate(str.maketrans('','',string.punctuation))
    listName_count = len(listName.split())
    return listName_count

# -------------- Task 1 to 3 Word count of a legislative text  -------------- #    


# -------------- Task 4 to 5 Calculate Flesch Reading Ease score -------------- #    

# -------------- Task 6 Calculate Flesch Reading Ease score -------------- #    

sectionSentences = ''.join(sections).replace("--", " ").replace("\n", " ")
sectionWords = sectionSentences.translate(str.maketrans('','',string.punctuation))
firstPageWords = page_text.replace("--", " ").replace("\n", " ").translate(str.maketrans('','',string.punctuation))
totalWords = len(firstPageWords.split()) + countWords(sections)
# print(totalWords)

totalSentences = len(sent_tokenize(page_text)) + len(sent_tokenize(sectionSentences))
# print(totalSentences)

totalSyllables = 0
for word in firstPageWords.split():
    n = syllables.estimate(word)
    totalSyllables += n
for word in sectionWords.split():
    n = syllables.estimate(word)
    totalSyllables += n
# print(totalSyllables)

def FRES(totalWords, totalSentences, totalSyllables):
    score = 206.835 - 1.015*(totalWords/totalSentences) - 84.6*(totalSyllables/totalWords)
    return score
print("Flesch Reading Ease Score: ", FRES(totalWords, totalSentences, totalSyllables))

