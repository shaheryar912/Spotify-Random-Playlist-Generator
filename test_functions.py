"""
Stores test functions used to find algos and other miscleaneous functions
used to help in development.
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Spotify_Random_Playlist_Generator.settings')

import django
django.setup()


import sys
import requests
from randomizer.models import *
from randomizer.spotify_api_funcs import *

def backup_track_ids():
    """
    Saves all track ids saved in django model to a text file
    """
    try:
        file = open("track_id_backup.txt", 'w+')

        all_tracks = Track.objects.all()
        index = 0
        last_track = ""

        for track in all_tracks:
            file.write(track.id + "\n")
            print("Added: " + track.id)

            last_track = track.id
            index += 1

    except Exception as e:
        print("An unexpected error has occurred.")
        print(e)

    finally:
        print("\n")
        print("Last index: " + str(index))
        print("Last id: " + last_track)


def clear_django_model():

    try:
        print("Deleting tracks...")
        Track.objects.all().delete()
        print("Tracks deleted.")
    except Exception as e:
        print("Error.")
        print(e)




if __name__ == "__main__":
    clear_django_model()



# my_model = Track()
# single_track_size = sys.getsizeof(my_model)
# num_tracks = Track.objects.count()
# total_size = single_track_size * num_tracks
#
# print("Stats:")
# print("Single Track: " + str(single_track_size))
# print("Num of Tracks:" + str(num_tracks))
# print("Total size: " + str(total_size))






#
# def get_common_words(file_str):
#     f = open(file_str, "r")
#
#     lines = f.read().splitlines()
#
#     common_words = {}
#     index = 0
#
#     for line in lines:
#         word_arr = line.split()
#
#         for word in word_arr:
#             if word not in common_words:
#                 common_words[word] = 1
#             else:
#                 common_words[word] += 1
#
#
#
#     sorted_words_list = sorted(common_words.items(), key=lambda kv: kv[1])
#
#     print(sorted_words_list)
#
#
#
#
#
#
# get_common_words("genre_list.txt")
