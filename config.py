from pymongo import MongoClient

try:
    client = MongoClient("mongodb+srv://movie:movie@cluster0.m6gra.mongodb.net/db_movie?retryWrites=true&w=majority")
    client.server_info()
except:
    print("connection error")

print("loading...")

db = client["db_movie"]
col = db["new_col_movie"]

# TITLE
t = col.find({},{'title': 1})
title = []
for data in t:
	title.append(data['title'])

# KEYWORDS
k = col.find({},{'keywords': 1})
keywords = []
for data in k:
	keywords.append(data['keywords'])

# DIRECTOR
d = col.find({},{'director': 1})
director = []
for data in d:
	director.append(data['director'])

# GENRE
g = col.find({},{'genre': 1})
genre = []
for data in g:
	genre.append(data['genre'])

# VOTE_AVERAGE
va = col.find({},{'vote_average': 1})
vote_average = []
for data in va:
	vote_average.append(data['vote_average'])

# VOTE_COUNT
vc = col.find({},{'vote_count': 1})
vote_count = []
for data in vc:
	vote_count.append(data['vote_count'])

# CAST
c = col.find({},{'cast': 1})
cast = []
for data in c:
	cast.append(data['cast'])

# WEIGHTED AVERAGE
wa = col.find({},{'weighted_average' : 1})
weighted_average = []
for data in wa:
	weighted_average.append(data['weighted_average'])

# # COMBINING
# co = col.find({}, {'combining' : 1})
# combining = []
# for data in co:
# 	combining.append(data['combining'])

# INDEX
i = col.find({}, {'index' : 1})
index = []
for data in i:
	index.append(data['index'])

# OVERVIEW
ov = col.find({}, {'overview' : 1})
overview = []
for data in ov:
	overview.append(data['overview'])

print("*** Connected Successfully to MongoDB Cluster ***")