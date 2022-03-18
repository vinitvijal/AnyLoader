import os
import youtube_dl
import webbrowser

ydl_opts = {
     'noplaylist' : True, 
}


def youMenu():
    print()
    print('     ~ ~ ~ YouTube Downloader ~ ~ ~   ')
    print('\n\n')
    print('   1. YouTube Video Download. (Beta) ')
    print('   2. YouTube Audio (Browser) Download.')
    print('   3. Main Menu.\n\n')
    Option = input('Select Option (1,2,3...) : ')
    if Option == '1':
        os.chdir('YouVideos')

        youLink = input('Enter YouTube Link : ')
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(youLink, download=True) 
        print('\n\ntitle       : %s' %(meta['title']))

        print('\n\nSuccessfully Downloaded!!!')
        os.chdir('..')

        youMenu()
    
    elif Option == '2':
        os.chdir('YouMusic')
        url = input('Enter YouTube Link : ')


        ydl = youtube_dl.YoutubeDL(ydl_opts)

        with ydl:
            result = ydl.extract_info(
                url,
                download=False
            )
        if 'entries' in result:
            # Can be a playlist or a list of videos
            audio = result['entries'][0]
        else:
            # Just a video
            audio = result
        
        link = audio['requested_formats'][-1]['url']
        webbrowser.open(link)
        print('Now Download From Browser....\n')
        os.chdir('..')

        youMenu()
        
    elif Option == '3':
        pass
    else:
        print('Wrong Input Try Again...\n\n')
        youMenu()


