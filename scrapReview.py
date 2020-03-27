import requests 
from bs4 import BeautifulSoup 
import csv 
import re
from selenium import webdriver
import os
import time
def scrap(url,num):
    chromedriver = "./chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    # browser = webdriver.Chrome(executable_path=r'C:\path\to\chromedriver.exe')
    driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
    fname = "reviews/"+str(num)+".txt"
    f = open(fname,"w")
    f.write(" ");
    f.close
    f = open(fname,"a")
    lis = []
    count = 1

    found=url
    count+=1
    while True:
        url=found
        driver.get(url)
        try:
            driver.find_element_by_class_name('ulBlueLinks').click()
            time.sleep(2)
            all_spans = driver.find_elements_by_xpath("//p[@class='partial_entry']")
            for span in all_spans:
                print(span.text)
                st = span.text
                st = st.replace('\n', ' ').replace('\r', '')
                lis.append(st)
                print("\n\n\n\n\n")
                
            for i in lis:
                f.write(str(i))
                f.write("\n")

            driver.find_element_by_class_name('next').click()
            found=driver.current_url

        except Exception as e:
            print("exit")
            print(e)
            break
    
    f.close()
    driver.close()
    print(url)
# scrap('https://www.tripadvisor.in/Restaurant_Review-g297637-d5922318-Reviews-or400-Mothers_Veg_Plaza-Thiruvananthapuram_Trivandrum_Thiruvananthapuram_District.html',11)
