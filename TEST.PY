import re
import pip._vendor.requests

from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
import string


headers = {'User-Agent': 'whatever'}

r = pip._vendor.requests.get(
    "http://www5.austlii.edu.au/au/legis/nsw/consol_act/capva2007347/", headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')
text = "".join(soup.strings)

new_text = text.translate(str.maketrans('', '', string.punctuation))

# text_count = len(new_text.split())

total_text = "".join(soup.strings)
# print(total_text)

##~~~~~~~~~~~~~~`` problem how to print the last part??~~~~~~~~~~

b = total_text.count('PART'.upper())

n = 1
for text in range(0, b):

    sub1 = 'PART ' + str(n)
    sub2 = 'PART ' + str(n+1)

    # getting index of substrings
    idx1 = total_text.index(sub1)
    idx2 = total_text.index(sub2)

    res = ''
    # getting elements in between
    for idx in range(idx1 + len(sub1) + 1, idx2):
        res = res + total_text[idx]
    print("The extracted string : " + res)
    n=n+1

part_text = res.translate(str.maketrans('','',string.punctuation))

part_count = len(part_text.split())
print(part_count)

        
        
