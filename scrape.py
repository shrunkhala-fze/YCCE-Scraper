import requests
import urllib3
import os
from bs4 import BeautifulSoup

url = "https://www.ycce.edu/ExaminationTimetable.php"
#url = "img/examination_timetable/1599563258.pdf"
pman = urllib3.PoolManager()
res = pman.request('GET',url)
#res.raise_for_status()
soup = BeautifulSoup(res.data,features="html5lib")
#print(soup)
lim = 2
tmp = soup.find('table',{'class':'table table-bordered table_row_color'})		
for tr in tmp.find_all('tr'):
	for a in tr.find_all('a'):
		s = "https://www.ycce.edu/"+a['href']
		fname = "C:/Users/PUSHKAR/Downloads/" + a['href']
		print("Downloading ")
		result = pman.request('GET',s)
		with open(fname,'wb') as itr:
			itr.write(result.data)
		os.system("start "+fname)
	if lim==0:
		break
	lim-=1
		
#print(tmp)



