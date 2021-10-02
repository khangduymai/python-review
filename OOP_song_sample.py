#%%
class Song:
    """Class to represent a song

    Attibutes:
        title (str): The title of the song
        artist (Artist): An artist object representing the song creator
        duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):
        """Song init method

        Args:
        ----------
        title : [str]
            [Initialises the 'title' attribute]
        artist : [Artist]
            [At Artist object representing the song's creator]
        duration : int, optional
            [Initialises value for the 'duration' attribute], by default 0
        """

        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """Class to represent an Album, using it's track list

    Attributes:
        name (str): The name of the album.
        year (int): The year was album was released.
        artist: (Artist): The artist reponsible for the album. If not specified,
        the artist will default to an artist with the name "Various Artists".
        tracks (List[Song]): A list of the songs in the album.

    Methods:
        addSong: Used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.track = []

    def add_song(self, song, position=None):
        """Adds a song to the track list

        Parameters
        ----------
        song (Song): A song to add
        position (Optional[int]): If specified, the song will be added to that position
            in the track list - inserting in between other songs if necessary.
            Otherwise, the song will be added to the end of the list.
        """
        if position is None:
            self.track.append(song)
        else:
            self.track.insert(position, song)


class Artist:
    """Basic class to store artist details.

    Attributes:
        name (str): The name of the artist.
        albums (List[Album]): A list of the albums by this artist.
            The list includes only those albums in this collection, it is 
            not an exhaustive list of the artist's published albums.

    Methods:
        add_album: Use to add a new album to the artist's albums list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list

        Parameters
        ----------
        album (Album): Album object to add to the list.
            If the album is already present, it will not add again (although this is yet to implemented)
        """
        self.albums.append(album)


def find_object(field, object_list):
    """Check 'object_list' to see if an object with a 'name' attribute equal to 'field' exists, return it if so."""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("D:\python\Python_practice\documents\\albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of  (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field =int(year_field)
            # print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field) #1000 Maniacs
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                # we've just read details for a new artist
                # store the current album in the current artist collection then creating a new artist obj (OLD METHOD)
                # (NEW METHOD) retrieve the artist object if there is one, 
                # otherwise, create a new artist object and add it to the artist list.
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist) 
                    new_album = None

                # new_artist.add_album(new_album) (OLD METHOD)
                # artist_list.append(new_artist) (OLD METHOD)
                # new_artist = Artist(artist_field) (OLD METHOD)
                # new_album = None (OLD METHOD)

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
                new_artist.add_album(new_album)
            elif new_album.name != album_field: # Our Time in Eden
                # we've just read a new ablum for the current artist
                # store the current album in the current artist collection then creating a new album obj (OLD METHOD)
                # retrieve album object if there is one
                # otherwise create a new album object and store it in the artist's collection
                new_album = find_object(album_field, new_album.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)  
                    new_artist.add_album(new_album)

                # new_artist.add_album(new_album) (OLD METHOD)
                # new_album = Album(album_field, year_field, new_artist)  (OLD METHOD)              


            # create a new song object and add it to the current album's collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        # After reading the last line of the text file, we will have an artist and album that have not
        # been stored - process them now
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)

    return artist_list



# with open("D:\python\Python_practice\documents\\albums.txt", "r") as albums:
#     for line in albums:
#         # data row should consist of  (artist, album, year, song)
#         print(line)
#         artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
#         year_field =int(year_field)
#         print(artist_field, album_field, year_field, song_field)


def create_checkfile(artist_list):
    """Create a check file from the object data for comparision with the original file"""
    with open("D:\python\Python_practice\documents\\checkfile.txt", "w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.track:
                    print("{0.name}\t{1.name}\t{1.name}\t{2.title}".format(new_artist, new_album, new_song), file=checkfile)

if __name__ == '__main__':
    artists = load_data()
    print(len(artists))

    create_checkfile(artists)
# %%
