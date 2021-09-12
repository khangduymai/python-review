

# print(len(albums))

# #%%
# for name, artist, year, songs in albums:
#     print("Album: {}, Artist: {}, Year: {}, Songs: {}".format(name, artist, year, songs))
#     print()

# # %%
# album = albums[2]
# print(album)
# print()
# songs = album[3]
# print(songs)
# print()
# song = songs[1]
# print(song)
# print()
# print('Song title: ',song[1])
# print()
# print()

# print(albums[2])
# print(albums[2][3])
# print(albums[2][3][1])
# print(albums[2][3][1][1])

# # %%
# album1 = albums[2][3][1][1]
# print('Alternative way to get data in nested list turple: ', album1)


#%%
from nested_data import  albums

#print(albums)
SONG_LIST_INDEX = 3
SONG_TITLE_INDEX = 1
while True:

    print("please choose your album (invalid choice exists)")

    for album_index, album in enumerate(albums):
        title, artist, year, songs = album
        print("{}: {}".format(album_index + 1,title))

    choice = int(input("ENTER ALBUM NUMBER:"))
    print()

    if 1 <= choice < len(albums):

        songs_list = albums[choice -1][SONG_LIST_INDEX]

        # for song in songs_list:
        #     print(song)

        print()

    else:    
        break

    print("Please choose your song")  

    for song_index, (track, song) in enumerate(songs_list):
        print("{}: {}".format(song_index +1, song))  

    song_choice = int(input("Choose your song"))

    if 1 <= song_choice < len(songs_list):

        song_title = songs_list[song_choice -1][SONG_TITLE_INDEX]
    else:
        break   

    print()    
    print("PLAYING: {}".format(song_title)) 
    print('*' * 40)
# %%
