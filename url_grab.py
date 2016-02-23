import requests
from bs4 import BeautifulSoup
import re
a = ''
b = ''
c =[]
r = requests.get("http://dart.fss.or.kr/dsaf001/main.do?rcpNo=20151116001340")
soup = BeautifulSoup(r.content, "html5lib")
word = "treenode"
looper = soup.prettify().lower().split('\n')
quoted = re.compile('"[^"]*"')
quoted2 = re.compile(r"'(.*?)'")
for item in looper:
    if "text:" in item:
        for i in quoted.findall(item):
            print "\n" + i,
    if "click:" in item:
        for i in quoted2.findall(item):
            print i,