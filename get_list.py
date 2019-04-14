from bs4 import BeautifulSoup
import requests
import json
import lxml
class Get_list:
    def getlist(self):
        # url = 'https://bugzilla.mozilla.org/show_bug.cgi?id='
        # headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        # req = requests.get(url,headers=headers)
        # # print(req.text)
        # soup = BeautifulSoup(req.text,"lxml")
        # tbody = soup.find("tbody")
        # trs = tbody.find_all("tr")
        # count = 0
        # for tr in trs:
        #     td = tr.find("td",class_="bz_id_column")
        #     bug = tr.find("a").text
        #     bug_list.append(bug)
        #     count = count + 1
        f = open('id.json')
        str = f.read()
        print(str)
        bug_list = []
        f = str.split(",")
        j=0
        for i in f:
            j = j+1
            bug_list.append(i.strip().strip('\ufeff').strip('"'))
            if j > 50:
                break
        bug_list.append('1306942')
        # bug_list.append("1470284")
        # bug_list.append("1471243")
        # bug_list.append("1306942")
        # bug_list.append("1306942")
        return bug_list
