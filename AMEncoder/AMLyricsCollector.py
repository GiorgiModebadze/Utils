import json
import re
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

## source for lyrics: Easy for scraping
my_url_Page = 'http://www.alivelyrics.com/a/arcticmonkeys/'
uClient = uReq(my_url_Page)
page_html = uClient.read()
page_soup = soup(page_html, "html.parser")
tables = page_soup.findAll("table", {"class": "tracklist"})
album_names = page_soup.findAll('h2')

# to get all album names
studio_albums = list()
song_list = list()
# album names were mostly between ""
pattern = r'\"(.*?)\"'

for album in album_names:
    if ("\"" in album.text):
        album_name = re.search(pattern, album.text)
        studio_albums.append(album_name.group(0).replace("\"", ""))

album_number = 0

# to get all the songs
for table in tables:
    album_name = studio_albums[album_number]
    rows = table.findAll("tr")
    contains_song = 0
    for row in rows:
        song = dict()
        track_number = row.find("td", {"class": "track"})
        track_number_correct = track_number.text.replace(".", "")
        if track_number_correct.strip() != "*":
            track_name = row.find('a')
            link = row.find('a', href=True)
            song["album_number"] = album_number + 1
            song["album_name"] = album_name
            song["track_number"] = int(track_number.text.replace(".", ""))
            song["track_name"] = track_name.text
            song["lyrics_href"] = my_url_Page + link['href']
            song_list.append(song)
            contains_song += 1

    if contains_song != 0 and album_number < 6:
        album_number += 1

for song in song_list:
    href = song['lyrics_href']
    uClient = uReq(href)
    page_html = uClient.read()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.find("pre", {"class": "lyrics"})

    song['text'] = containers.text.rstrip()
    song['text'] = song['text'].strip()
    song['text'] = song['text'].replace('\r\n', " ")
    song['text'] = song['text'].replace('\n', " ")

with open('data.json', 'w') as fp:
    json.dump(song_list, fp)
