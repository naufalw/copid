import requests
from bs4 import BeautifulSoup
import pprint
a = requests.get("https://www.worldometers.info/coronavirus/")
soupString = BeautifulSoup(a.text, "lxml")
table = soupString.find(id="main_table_countries_today")
dList, dDict = [], []
for i in table.findAll("tr"):
	dList.append(i.findAll("td"))
for i in dList[9:-9]:
	dDict.append(
		{
			"Name": "Unnamed" if i[1].string ==  None else i[1].string,
			"TCases": "0" if i[2].string == None else i[2].string,
			"NCases": "0" if i[3].string ==  None else i[3].string,
			"TDeaths": "0" if i[4].string == None else i[4].string,
			"NDeaths": "0" if i[5].string ==  None else  i[5].string,
			"TRecovered": "0" if i[6].string ==  None else i[6].string,
			"NRecovered": "0" if i[7].string ==  None else i[7].string,
			"Active": "0" if  i[8].string ==  None else i[8].string,
			"Population" : "0" if (i[14].a.string if i[14].find('a') else i[14].string) == ' ' else (i[14].a.string if i[14].find('a') else i[14].string)
		}
	)
pprint.pprint(dDict)