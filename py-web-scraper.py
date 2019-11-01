import requests
from bs4 import BeautifulSoup


source = requests.get("https://tvods.se/v/lirik.html").text

soup = BeautifulSoup(source, "lxml")

tbody = soup.find("tbody", attrs={"class": "searchable"})

try:
    for table in tbody.find_all("tr", attrs={"class": "table-primary"}):

        cols = table.find_all("td")
        cols = [x.text.strip() for x in cols]
        video = table.find("a")["href"]

        print(cols[0] + " - " + cols[1] + " - " + cols[4] + " - " + video)
        match_day = cols[0]

        for sec_table in tbody.find_all("tr", attrs={"class": "table-secondary"}):
            sec = sec_table.find_all("td")
            sec = [y.text.strip() for y in sec]
            if sec[0] == match_day:
                print(sec[3])

        print()


except Exception as e:
    cols = None
    video = None
    sec = None

