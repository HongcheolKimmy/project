import requests
from bs4 import BeautifulSoup
import re

r = requests.get("http://dart.fss.or.kr/report/viewer.do?rcpNo=20151116001340&dcmNo=4855157&eleId=3&offset=9323&length=766460&dtd=dart3.xsd")
soup = BeautifulSoup(r.content, "html5lib")
for i in soup.find_all("table"):
    print "\n"
    counter_a = 0
    for m in i.find_all("col"):
        counter_a += 1
        counter_b = 0
    for o in i.find_all("th"):
        string_ver = str(o)
        if "colspan=" in string_ver:
            letter_number = int(string_ver.find("colspan"))
            position_number = letter_number + 9
            counter_b += int(string_ver[position_number])
        else:
            counter_b += 1
        print o.text,
        if counter_b == counter_a:
            counter_b = 0
            print "\n"
    counter_c = 0
    for p in i.find_all("td"):
        string_ver1 =str(p)
        if "colspan=" in string_ver1:
            letter_number2 = int(string_ver1.find("colspan"))
            position_number1 = letter_number2 + 9
            counter_c += int (string_ver1[position_number1])
        else:
            counter_c += 1
        print p.text,

        if counter_c == counter_a:
            counter_c = 0
            print "\n"

