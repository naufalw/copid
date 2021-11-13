import requests, pandas as pd
from bs4 import BeautifulSoup

a = requests.get("https://www.worldometers.info/coronavirus/")
soupString = BeautifulSoup(a.text, "lxml")
table = soupString.find(id="main_table_countries_today")
tRow, cData = [], []
for i in table.findAll("tr"):
    tRow.append(i.findAll("td"))
for i in tRow[9:-9]:
    pop = i[14].a.string if i[14].find("a") else i[14].string
    cData.append(
        {
            "Name": i[1].string or "Unnamed",
            "TCases": i[2].string or "0",
            "NCases": i[3].string or "-",
            "TDeaths": i[4].string if i[4].string != " " else "- ",
            "NDeaths": i[5].string or "-",
            "TRecovered": i[6].string or "0",
            "NRecovered": i[7].string or "-",
            "Active": i[8].string or "0",
            "Population": "-" if pop == " " else pop,
        }
    )
pd.set_option("display.max_rows", None)
df = pd.DataFrame(cData)
df.index += 1
print(df)
