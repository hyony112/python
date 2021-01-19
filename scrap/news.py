import requests
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
import time

url = "https://cwsjames.tistory.com/"
webpage = requests.get(url)
wd = webdriver.Chrome('C:/Program Files/Google/Chrome/Application/chromedriver.exe')
todayArray = []
today = datetime.today()
#todayStr = datetime.today().strftime("%Y년 %m월 %d일") #yyyy년 mm월 dd일
todayStr = "{0}년 {1}월 {2}일".format(today.year, today.month, today.day) #yyyy년 m월 d일
todayStr2 = datetime.today().strftime("%Y/%m/%d/")

f = open('C:/Users/LHE/Desktop/' + todayStr + ' news.txt', 'a', -1, 'utf-8')
resultStr = ""
#print(webpage.text)

soup = BeautifulSoup(webpage.content, "html.parser")
aTags = soup.find('div','another_category').find_all('a')

# 오늘날짜인 경우 내용 출력
print('# 오늘날짜인 경우 내용 출력')
#if todayStr in soup.p:
print(soup.p)
resultStr = resultStr + soup.p.get_text('\n\n',strip=True)


# 오늘날짜 다른 링크 존재하는 경우 경로 리스트 생성
print('# 오늘날짜 다른 링크 존재하는 경우 경로 리스트 생성')
for str in aTags:
    if str.get('class') is None :
        if todayStr in str.string or todayStr2 in str.string :
            todayArray.append(str.get('href'))


# 다른 링크 존재하는 경우 경로 리스트에서 내용 출력
print('# 다른 링크 존재하는 경우 경로 리스트에서 내용 출력')
for page in todayArray:
    resultStr = resultStr + '\n\n'
    wd.get(url + page)
    sou = BeautifulSoup(wd.page_source, "html.parser")
    print(sou.p)
    resultStr = resultStr + sou.p.get_text('\n\n',strip=True)
    time.sleep(3)

    

# 파일 쓰기
f.write(resultStr)
print('#########################end#########################')
