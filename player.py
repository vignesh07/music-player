import os
import pyglet
import random

# empty list to store the list of songs
song_list = []

for file in os.listdir("."):
    if ".wav" in file:
        # listdir will list all files and subdirectories, so I just used a workaround to add only the .wav files
        # EDIT: To use .mp3 files, you will have to use AVbin otherwise this error occurs...
            # pyglet.media.riff.WAVEFormatException: AVbin is required to decode compressed media
        song_list.append(file)

# player object has the option of queueing
player = pyglet.media.Player()

# making the playlist random
random.shuffle(song_list)
random.shuffle(song_list)
random.shuffle(song_list)               
random.shuffle(song_list)

for song in song_list:
    audio = pyglet.resource.media(song)
    player.queue(audio)

player.play()
pyglet.app.run()
