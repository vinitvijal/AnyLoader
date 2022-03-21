import requests

link='https://www.instagram.com/its.vinit_vijal__/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'}

url = ((link)+'?__a=1')
print(url)
data = requests.get(url, headers=headers)
if data.status_code == 200:
    print("valid")

jsonData = data.json()

bio = jsonData['graphql']['user']['biography']
followers = jsonData['graphql']['user']['edge_followed_by']['count']




print('Bio : \n',bio)
print('Followers : ',followers)