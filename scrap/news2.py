import requests
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
from slacker import Slacker

# 크롬 드라이버 호환성 에러로 인해 options 설정을 추가한다.
options = Options()
options.add_argument('--no-sandbox')

slack = Slacker('토큰키')
url = "url"
webpage = requests.get(url)
wd = webdriver.Chrome(chrome_options=options, executable_path='C:/Program Files/Google/Chrome/Application/chromedriver.exe')

todayUrl = ''
today = datetime.today()
todayStr = datetime.today().strftime("%Y년 %m월 %d일") #yyyy년 mm월 dd일
#todayStr = "{0}년 {1}월 {2}일".format(today.year, today.month, today.day) #yyyy년 m월 d일
#todayStr2 = datetime.today().strftime("%Y/%m/%d/")

#f = open('C:/Users/LHE/Desktop/' + todayStr + ' news2.txt', 'a', -1, 'utf-8')
resultStr = ""
#print(webpage.text)

def remove_tag(content):
   cleanr =re.compile('<.*?>')
   cleantext = re.sub(cleanr, '', content)
   return cleantext

soup = BeautifulSoup(webpage.content, "html.parser")
#spanTags = soup.find('div','sub_list')
spanTags = soup.select('div.sub_list')[0]

print(spanTags)

# 오늘날짜인 경우 내용 출력
print('# 오늘날짜인 경우 내용 출력')
print(todayStr)

if todayStr in spanTags.text:
    todayUrl = spanTags.select('a')[0]['href']
#print(todayUrl)

# 뉴스 내용 정리
wd.get(todayUrl)
sou = BeautifulSoup(wd.page_source, "html.parser")
#resultStr = sou.select('div.art_txt')[0].get_text('\n')
resultStr = sou.select('div.art_txt')[0].get_text('\n').split("===================================================")[0]

print(type(resultStr))
print(resultStr)

# 메시지보내기
#f.write(resultStr)
slack.chat.post_message('#news', resultStr)
print('#########################end#########################')

