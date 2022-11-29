import re
from selenium import webdriver
from selenium.webdriver.common.by import By
# browser =webdriver.Chrome()

browser = webdriver.Chrome(executable_path=r"C:\Users\hpcyi\Documents\Data Science\chromedriver.exe")  # Path to where I installed the web driver
browser.get('https://itcodefair.cdu.edu.au/data-science-challenge/')
driver= webdriver.Chrome(executable_path=r"C:\Users\hpcyi\Documents\Data Science\chromedriver.exe")

##~~~~~~~~~~~~~~~~~~`get legislation urls~~~~~~~~~~~~~~~~~~~~`####
urls=[]

u=browser.find_elements(By.XPATH, "//div[@class='elementor-widget-container']//table//tbody//tr//td//p//a")
for url in u:
    url=url.get_attribute('innerHTML')
    urls.append(url)
# print(urls)
##~~~~~~~~~~~~~~~~~~`get each legislation 's title ~~~~~~~~~~~~~~~~~~~~`####
for u in urls:
    driver.get(u)
    title=driver.find_element_by_xpath("html/body/h2").text
    title2=driver.find_element_by_xpath("html/body/h3").text
    print(title)  
    s_title=title2.split()
    year= s_title[-1]
    print(year)
     

browser.quit()
driver.quit()
