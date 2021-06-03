# from pymongo import MongoClient

# try:
#     client = MongoClient("mongodb+srv://movie:movie@cluster0.m6gra.mongodb.net/db_movie?retryWrites=true&w=majority")
#     client.server_info()
# except:
#     print("connection error")

# db = client["db_movie"]
# col = db["col_movie"]

# # TITLE
# def titling():
# 	x = col.find({},{'title': 1})

# 	title = []
# 	for data in x:
# 		title.append(data['title'])

# # KEYWORDS
# def keywording():
# 	x = col.find({},{'keywords': 1})

# 	keywords = []
# 	for data in x:
# 		keywords.append(data['keywords'])

# # DIRECTOR
# def directoring():
# 	x = col.find({},{'director': 1})

# 	director = []
# 	for data in x:
# 		director.append(data['director'])

# # GENRE
# def genreing():
# 	x = col.find({},{'genre': 1})

# 	genre = []
# 	for data in x:
# 		genre.append(data['genre'])

# # VOTE_AVERAGE
# def voteAverage():
# 	x = col.find({},{'vote_average': 1})

# 	vote_average = []
# 	for data in x:
# 		vote_average.append(data['vote_average'])

# # VOTE_COUNT
# def voteCount():
# 	x = col.find({},{'vote_count': 1})

# 	vote_count = []
# 	for data in x:
# 		vote_count.append(data['vote_count'])

# # CAST
# def casting():
# 	x = col.find({},{'cast': 1})

# 	vote_count = []
# 	for data in x:
# 		vote_count.append(data['cast'])

