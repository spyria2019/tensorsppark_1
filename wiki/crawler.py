from bs4 import BeautifulSoup

import requests

class Wiki:

    def __init__(self,url):
        base_url = url
        con = requests.get(base_url)
        soup = BeautifulSoup(con.content, 'html.parser')
#        print(soup)

        infoTable = soup.find('table',{'class','wikitable sortable'})
        result = []

        for a in infoTable.find_all('tr'):
            inforlist = []

            for b in infoTable.find_all('td'):
                 pass



