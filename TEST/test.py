# import requests

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'}

# def insta(link):
#     url = ((link)+'?__a=1')
#     print(url)
#     data = requests.get(url, headers=headers)
#     if data.status_code == 200:
#         print("valid")
#     jsonData = data.json()


#     list_of_sources = jsonData['graphql']['shortcode_media']['display_resources']

#     link = list_of_sources[-1]['src']

#     local_file = 'local_copy.jpg'

#     data = requests.get(link)

#     with open(local_file, 'wb')as file:
#         file.write(data.content)



# insta('https://www.instagram.com/p/CaAYRQSKjvV/')
















# # using datetime module
# import datetime;
  
# # ct stores current time
# ct = datetime.datetime.now()
# print("current time:-", ct)
  

import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'}

# def instaVideo(link):
#     url = ((link)+'?__a=1')
#     print(url)
#     data = requests.get(url, headers=headers)
#     if data.status_code == 200:
#         print("valid")
# #     jsonData = data.json()

# #     req_data = jsonData['graphql']['shortcode_media']['video_url']


# # insta('https://www.instagram.com/p/CaqwFPEg6iL/')

# def instaVideo(link):
#     url = ((link)+'?__a=1')
#     print(url)
#     data = requests.get(url, headers=headers)
#     if data.status_code == 200:
#         print("valid")
#     jsonData = data.json()

#     req_data = jsonData['graphql']['shortcode_media']
#     print(req_data)

# instaVideo('https://www.instagram.com/reel/Ca9-iMAgSfd/')
import youtube_dl

url = input('Enter YouTube Link : ')

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

with ydl:
    result = ydl.extract_info(
        url,
        download=False
    )
video = result
print(video)