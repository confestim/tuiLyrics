from config import TOKEN
import lyricsgenius
import argparse

def lookup(song_name, artist):
    genius = lyricsgenius.Genius(TOKEN, skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)
    song = genius.search_song(song_name, artist)

    print(song.lyrics)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
                    prog='tuiLyrics',
                    description='Look up at lyrics',
                    epilog='garbage code')

    parser.add_argument('song_name')
    parser.add_argument('artist')
    args = parser.parse_args()
    if not args.song_name and not args.artist:
        raise IOError("Provide the name and artist")

    lookup(args.song_name, args.artist)
