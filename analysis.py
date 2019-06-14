from textblob import TextBlob

file = open('headlines.txt', 'r')
news = file.readlines()
for i in news:
	i = i[0:-1]

for i in news:
	dat = TextBlob(i)
	if dat.sentiment[0] > 0.5:
		print(dat + '\n')