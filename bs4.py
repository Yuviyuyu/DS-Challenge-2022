import requests 
from bs4 import BeautifulSoup 
from collections import Counter 
from string import punctuation 
from lxml.html.soupparser import fromstring 

  

# We get the url 
headers = {'User-Agent': 'whatever'} 
r = requests.get("http://www5.austlii.edu.au/au/legis/nsw/consol_act/capva2007347/", headers=headers) 
soup = BeautifulSoup(r.content, 'html.parser') 


# print(soup.prettify()) 

 
text = "".join(soup.strings) 
new_text = text.translate(str.maketrans('','',string.punctuation)) 
text_count = len(new_text.split()) 
print (text_count) 

 
 

urls = [] 
# for link in soup.find_all('a'): 
   # print(link.get('href')) 
# print("".join(soup.strings)) 

 
