# encoding: utf-8

import requests

import parser
from bs4 import BeautifulSoup

url = 'http://www.resident-music.com/tickets'
page = requests.get(url).text
soup = BeautifulSoup(page, "html.parser")
table = soup.find('tbody')

f = open("./resident.txt", "w+")


def scrape_first_column():
    for row in table.findAll('tr'):
        is_first_column = True

        for cell in row.findAll('td'):
            if is_first_column:
                # clean up the scraped text
                text = cell.text.encode('utf-8')

                # stops duplicate artists from being added
                artist_set = set()

                # _generally_ acts are split on a ' / '
                if ' / ' in text:
                    text = text.split(' / ')
                    for line in text:
                        artist_set.add(line)
                else:
                    artist_set.add(text)

                for l in artist_set:
                    f.write(parser.stripper(l))

                is_first_column = False

scrape_first_column()
