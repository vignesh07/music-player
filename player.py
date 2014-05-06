import os
from os import listdir
import pyglet
import random
from pyglet import app
from pyglet import window

song_list=[]   ##empty list to store the list of songs

for file in os.listdir("."):
	if ".mp3" in file:
		song_list.append(file)           ##listdir will list all files and even the subdirectories, so I just 
										 ##used a workaround to add only the mp3 files


player = pyglet.media.Player()           ##player object has the option of queueing

random.shuffle(song_list)
random.shuffle(song_list)
random.shuffle(song_list)               
random.shuffle(song_list)   ##making the playlist random

for song in song_list:
	
	audio = pyglet.resource.media(song)
	player.queue(audio)



player.play()
pyglet.app.run()



	





	





	
	

	
