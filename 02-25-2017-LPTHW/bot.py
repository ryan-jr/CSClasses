# bot.py

import tweepy
import requests
import random

from io import BytesIO

from PIL import Image
from PIL import ImageFile

from secrets import *

ImageFile.LOAD_TRUNCATED_IMAGES = True 

# Create OAuthHandler instance and use OAuth for authentication
auth = OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)

# Construct API instance
api = tweepy.API(auth)


def tweet_image(url, username, status_id):
    
    """
    Function to take/read an image from the tweet stream
    and return a scrambled image
    """

    filename = 'temp.png'

	# Send a get request
    request = requests.get(url, stream = True)
    if request.status_code == 200:
        # Read data from downloaded bytes and Return a PIL.Image.image
        i = Image.open(BytesIO(request.content))

		# Saves the image under the given filename
        i.save(filename)
        scramble(filename)

		# Update the authenticated User's status

        api.update_with_media('scramble.png', status = '@{0}'.format(username), in_reply_to_status_id = status_id)
    else:
        print("unable to download image")



def scramble(filename):
	BLOCKLEN = 64 # 64 is default but we can adjust

	img = Image.open(filename)
	width, height = img.size

	xblock = width // BLOCKLEN
	yblock = height // BLOCKLEN

	# Create 4 tuples defining L, R, T, B pixel coordination
	blockmap = [(xb * BLOCKLEN, yb * BLOCKLEN, (xb + 1) * BLOCKLEN, (yb + 1) * BLOCKLEN) 
	for xb in range(xblock) for yb in range(yblock)]

	shuffle = list(blockmap)
	
	# Shuffle the sequence
	random.shuffle(shuffle)

	# Creates a new image with the given mode/size
	result = Image.new(img.mode, (width, height))
	for box, sbox in zip(blockmap, shuffle):
		# Returns rectangular section from original image
		crop = img.crop(sbox)
		# Pastes the cropped pixel into the new image object
		result.paste(crop, box)
	result.save('scramble.png')




# Create a class inheriting StreamListener from tweepy
class BotStreamer(tweepy.StreamListener):

	# Called when a new status arrives
	def on_status(self, status):
		username = status.user.screen_name
		status_id = status.id 

	# Provide structured data from Tweets
	if 'media' in status.entities:
		for image in status.entities['media']:
			tweet_image(image['media_url'], username, status_id)




myStreamListener = BotStreamer()

# Construct Stream instance
stream = tweepy.Stream(auth, myStreamListener)

stream.filter(track=['@rypytweet1995'])



"""
# Examples of getting public tweets and friend lists via tweepy

public_tweets = api.home_timeline()
for tweet in public_tweets:
	print(tweet.text)


user = api.get_user('rypytweet1995')
for friend in user.friends():
	print(friend.screen_name)

"""


