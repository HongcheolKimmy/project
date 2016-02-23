import requests
from bs4 import BeautifulSoup

r = requests.get("http://dart.fss.or.kr/report/viewer.do?rcpNo=20151116001340&dcmNo=4855157&eleId=3&offset=9323&length=766460&dtd=dart3.xsd")
soup = BeautifulSoup(r.content, "html5lib")
for i in soup.find_all("tr"):
    print "\n" + "--------------------"
    for n in i.find_all("th"):
        print "|" + n.text + "|",
    for l in i.find_all("td"):
        print "|" + l.text + "|",