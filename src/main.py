#!/bin/python3

from config import TOKEN
import lyricsgenius
import argparse
import os
from colorama import init as color
from colorama import Fore, Back
from time import sleep
import subprocess

def lookup(song_name, artist, offset):
    """ 
    Song lookup.
    <song_name>: name of song
    <artist>: artist
    <offset>: time to sleep between the lines of the song
    """

    # Initializing
    genius = lyricsgenius.Genius(TOKEN, skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True, verbose=False)
    song = genius.search_song(song_name, artist).to_dict()

    # Printing
    print(Fore.RED + Back.YELLOW + song.get("title") + Back.RESET)
    sleep(.5)
    print(Fore.YELLOW + Back.RED + "By " + song.get("primary_artist").get("name") + Back.RESET)
    sleep(.5)

    # Cleaning lyricst from redundant info
    sanitized_lyrics = song.get("lyrics").split("\n")
    del sanitized_lyrics[0]
    print(Fore.RESET + Back.RESET)
    for i in sanitized_lyrics:
        print(i)
        sleep(offset)

if __name__ == "__main__":
    # Init color and parser
    color()
    parser = argparse.ArgumentParser(
                    prog='tuiLyrics',
                    description='Look up at lyrics',
                    epilog='garbage code')

    parser.add_argument('song_name')
    parser.add_argument('artist')
    parser.add_argument('-o', '--offset')
    args = parser.parse_args()
    # Parsing logic
    if not args.song_name and not args.artist:
        raise IOError("Provide the name and artist")

    if not args.offset:
        args.offset = 0
    try:
        lookup(args.song_name, args.artist, offset=int(args.offset))
    except KeyboardInterrupt:
        pass
