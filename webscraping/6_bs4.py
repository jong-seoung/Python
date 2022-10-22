import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

#페이지에 대한 이해도가 높을때
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup에서 제일 처음 발견되는 a를 출력
# print(soup.a.attrs) # a태그가 가지고 있는 속성 정보를 출력
# print(soup.a["href"]) # a의 href의 속성 값 정보 출력

# print(soup.find("a",attrs={"class":"Nbtn_upload"})) # class값이 Nbtn_upload인 a element를 찾아줘
# print(soup.find(attrs={"class":"Nbtn_upload"})) # class값이 Nbtn_upload인 값을 찾아줘
# print(soup.find("li",attrs={"class":"rank01"}))
rank1 = soup.find("li",attrs={"class":"rank01"})
print(rank1.a)