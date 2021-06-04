from pymongo import MongoClient

try:
    client = MongoClient("mongodb+srv://movie:movie@cluster0.m6gra.mongodb.net/db_movie?retryWrites=true&w=majority")
    client.server_info()
except:
    print("connection error")

db = client["db_movie"]
col = db["col_movie"]

# TITLE
t = col.find({},{'title': 1})
title = []
for data in t:
	title.append(data['title'])
print("1-----------------------------------------------------------------------")
# print(title)

# KEYWORDS
k = col.find({},{'keywords': 1})
keywords = []
for data in k:
	keywords.append(data['keywords'])
print("2-----------------------------------------------------------------------")
# print(keywords)

# DIRECTOR
d = col.find({},{'director': 1})
director = []
for data in d:
	director.append(data['director'])
print("3-----------------------------------------------------------------------")
# print(director)

# GENRE
g = col.find({},{'genre': 1})
genre = []
for data in g:
	genre.append(data['genre'])
print("4-----------------------------------------------------------------------")
# print(genre)

# VOTE_AVERAGE
va = col.find({},{'vote_average': 1})
vote_average = []
for data in va:
	vote_average.append(data['vote_average'])
print("5-----------------------------------------------------------------------")
# print(vote_average)

# VOTE_COUNT
vc = col.find({},{'vote_count': 1})
vote_count = []
for data in vc:
	vote_count.append(data['vote_count'])
print("6-----------------------------------------------------------------------")
# print(vote_count)

# CAST
c = col.find({},{'cast': 1})
cast = []
for data in c:
	cast.append(data['cast'])
print("7-----------------------------------------------------------------------")
# print(cast)
print("OK!")
