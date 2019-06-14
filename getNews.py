import requests
import pprint
url = ('https://newsapi.org/v2/everything?'
       'domains=wsj.com,nytimes.com&pageSize=100&'
       'apiKey=' + key.key)
response = requests.get(url)
pp = pprint.PrettyPrinter(4)
# print(response.json())	
# pp.pprint(response.json()['articles'][0]['title'])

headlines = open('headlines.txt', 'w')
for i in response.json()['articles']:	
	headlines.write(i['title'])
	print(i['title'])
	headlines.write('\n')

headlines.close()
