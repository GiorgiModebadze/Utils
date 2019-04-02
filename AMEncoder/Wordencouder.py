import pandas as pd
import random

songs = pd.read_json("data.json")

# random encoder
# encodes word in the following pattern album number | song number | word position
# if this word is found several times returns random one

def encode_word_random(word, songs, reverse=False):
    word_list = list()
    for index, row in songs.iterrows():
        album_number = row['album_number']
        track_number = row['track_number']
        word_position = 0
        for text_word in row['text'].split():
            word_position += 1
            if text_word.lower() == word.lower():
                if reverse:
                    secret = str(word_position) + '|' + str(track_number) + '|' + str(album_number)
                else:
                    secret = str(album_number) + '|' + str(track_number) + '|' + str(word_position)
                word_list.append(secret)
                break
    if len(word_list) > 0:
        return random.choice(word_list)
    else:
        return word


text = input("please input your text: ")
reverse = input("reverse encoding (Yes/No): ")

should_reverse = reverse.lower() == 'yes'

for word in text.split():
    print(encode_word_random(word, songs, should_reverse))
