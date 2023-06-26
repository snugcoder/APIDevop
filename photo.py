import requests
#idea1: i want to have the API return an image of the day when
#the user enters in a date

#response format from flickr
flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
sets   = flickr.photosets.getList(user_id='73509078@N00')
title  = sets['photosets']['photoset'][0]['title']['_content']

print('First set title: %s' % title)

response = requests.post()

