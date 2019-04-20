from bs4 import BeautifulSoup
import requests
import json
import lxml
class Get_list:
    def getlist(self):

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
        #bug_list.append('1306942')
        #bug_list.append('1361695')
        # bug_list.append("1470284")
        # bug_list.append("1471243")
        # bug_list.append("1306942")
        # bug_list.append("1306942")
        return bug_list
