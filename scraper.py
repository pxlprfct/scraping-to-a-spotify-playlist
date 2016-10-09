# -*- coding: latin-1 -*-

import requests

import parser
from bs4 import BeautifulSoup

# todo - Is it worth the time to parse it in a cleaner way?
# todo - Get the first, and last show - and add it to the playlist name
# todo - Remove all songs from the playlist each time spotify.py is run


url = 'http://www.resident-music.com/tickets'
page = requests.get(url).text
soup = BeautifulSoup(page, "html.parser")
table = soup.find('tbody')
f = open("./Resident.txt", "w")


def scrape_first_column():
    for row in table.findAll('tr'):
        is_first_column = True

        for cell in row.findAll('td'):
            if is_first_column:
                text = parser.parse(cell.text)
                f.write(text)
                is_first_column = False

scrape_first_column()
