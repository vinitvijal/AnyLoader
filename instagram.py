import sys
import requests
import datetime
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'}



def instaPhoto(link):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'}
    url = ((link)+'?__a=1')
    print(url)
    data = requests.get(url, headers=headers)

    if data.status_code == 200:
        print("valid")
    jsonData = data.json()


    list_of_sources = jsonData['graphql']['shortcode_media']['display_resources']

    link = list_of_sources[-1]['src']

    local_file = str(datetime.datetime.now())+'.jpeg'

    data = requests.get(link)

    with open(local_file, 'wb')as file:
        file.write(data.content)
        print('\nDownloaded Successfully!!!')

    instaMenu()

def instaVideo(link):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'}
    url = ((link)+'?__a=1')
    print(url)
    data = requests.get(url, headers=headers)
    if data.status_code == 200:
        print("valid")
    
    jsonData = data.json()

    videolink = jsonData['graphql']['shortcode_media']['video_url']
    local_file = str(datetime.datetime.now())+'.mp4'

    data = requests.get(videolink)

    with open(local_file, 'wb')as file:
        file.write(data.content)
        print('\nDownloaded Successfully!!!')
    instaMenu()

def instaMenu():
    print()
    print('     ~ ~ ~ Instagram Downloader ~ ~ ~   ')
    print('\n\n')
    print('   1. Photos Downloader.')
    print('   2. Videos Downloader.')
    print('   3. Reels Downloader.')
    print('   4. Complete Profile Downloader (Upcoming).')
    print('   5. Main Menu.')
    print('\n\n')
    choice = input('Select You Choice : ')
    if choice == '1':
        os.chdir('InstaPhotos')
        link = input('Photo URL : ')
        instaPhoto(link)
        os.chdir('..')


    elif choice == '2':
        link = input('Video URL : ')
        os.chdir('InstaVideos')
        instaVideo(link)
        os.chdir('..')


    elif choice == '3':
        link = input('Reels URL : ')
        os.chdir('InstaReels')
        instaVideo(link)
        os.chdir('..')


    elif choice == '4':
        print('\n\nUnder Development Wait for the Update!!!!\n')
        instaMenu()
    elif choice == '5':
        print('\n\n')
        pass
    else:
        pass

instaMenu()