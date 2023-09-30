from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service=Service() #chrome driver open krne ke liya
options=webdriver.ChromeOptions() #chrome driver run krwane ke liya
startUrl="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars" #website ka url
browser=webdriver.Chrome(service=service,options=options)
browser.get(startUrl)
time.sleep(10) #webpage ko load hone se pehla to thoda time lapse

def scrape():
    headers=["Name","Distance","Mass","Radius"]#topics jinme data stored h wocsv file mei kaisa appear hone
    starData=[]

    for i in range(0,1):#kyu ki 428 pages h read krne ko
        soup=BeautifulSoup(browser.page_source,"html.parser")#page ko read krne ke liya

        for ul_tag in soup.find_all("tr",attrs={"class","wikitable sortable jquery-tablesorter"}):#topics ki andar jo data h wo li tag mei stored h webpage mei to saare ul tag ko access kr rahe h jinke class name exoplanet h
            td_tags=ul_tag.find_all("td")#phir hum ul tag ke andar saare li tag ko access kr rahe jinme actually data h isliya humne koi atrribute bhi nhi diya...waha 4 li tag h 4 data ke liya
            temp_list=[]

            for index,li_tag in enumerate(td_tags):#data 1 indirect diya hua h furthi li tag ke andar phir a tag ke andar par data 2 data 3 aur data4 direct diya hua h wo console mei elements mei jake chekc kr skta h
                if index==0: #agar li tag mei jo data 1 mei a tag h to uska info show ho jaye(fetch) 
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                else :#agar false h to...
                    try:#error dikhane ke jagha(jiski wajhe se page load nhi hoga aur error dikhayega)
                        temp_list.append(td_tag.contents[0])
                    
                    except:#ye sir uss data ki jagha blank space chod dega
                        temp_list.append("")
#iss sabko hum time_list wale empty array mei store kr rahe h aur further planet data wale empty dal rahe h
            
            starData.append(temp_list)

    #yaha humne next page click krne wala button tha to uska code uspa right click krke elements mei jake yaha pe pasta krdiya disse ab ye next page code ke har loop khatam hone ke baad khol skta h
    