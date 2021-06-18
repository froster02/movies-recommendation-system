# ************************************************* RECOMMENDATION SYSTEM *****************************************************************

# from operator import index
import operator
from re import L
from pymongo import ASCENDING
# import pandas as pd
from config import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# df = pd.read_csv('testing_dataset.csv', low_memory=False)

# id|crew|keywords|title|overview|popularity|release_date|status|tagline|vote_average|vote_count|genre|director|index|cast

# ************************************************* Cosine Similarity *******************************************************************

# def fun1_fillna(x):
#     if isinstance(x, list):
#         return [str(i.replace("NaN", "")) for i in x]
#     else:
#         if isinstance(x, str):
#             return str(x.replace("NaN", ""))
#         else:
#             return ''

# def fun2_enumerate(sequence, start=0):
#     n = start
#     for elem in sequence:
#         yield n, elem
#         n += 1

# def create_similarity():
#     # features = ['cast', 'keywords', 'director', 'genre']

#     # for feature in features:
#     #     df[feature] = df[feature].apply(fun1_fillna)
#     # def combined_features(row):
#     #     return row['cast'] + " " + row['keywords'] + " " + row['director']+ " " +row['genre']

#     # df['combining'] = df.apply(combined_features, axis=1)

#     # count = CountVectorizer()
#     # count_matrix = count.fit_transform(df['combining'])
#     # cosine_sim = cosine_similarity(count_matrix)

#     # return df, cosine_sim
#     cm = CountVectorizer().fit_transform(combining)
#     cs = cosine_similarity(cm)

#     return cs
  
def show_data(movie):

    def features(director, keywords, cast, genre):
        combining = []
        for i in range(0, len(director)):
            combining.append(director[i] + ' ' + keywords[i] + ' ' + cast[i] + ' ' + genre[i])
        return combining
    combining = features(director, keywords, cast, genre)

    cm = CountVectorizer().fit_transform(combining)
    cs = cosine_similarity(cm)
    # df, cosine_sim = create_similarity()

    try:
        # movie_index = df.loc[df['title']==movie].index[0]
        # movie_index = df[df['title']==movie].index[0]
        movie_index = title.index(movie)
    except:
        return['Sorry! The movie you requested is not in our database. Please check the spelling or try with other movies!'], ['¯\_(ツ)_/¯'], []

    # i = int(movie_index)

    # similar_movies = list(fun2_enumerate(cosine_sim[i]))
    similar_movies = list(enumerate(cs[movie_index]))
        
    sorted_similar_movies = sorted(similar_movies,key = lambda x:x[1], reverse = True)  

    # sorted_similar_movies = sorted_similar_movies[1:11]      
                    
    i=0
    j=0

    # title_list1 =[None]*10    
    # rating_list1 =[None]*10
    # detail_list1 =[None]*10

    title_list1 =[]   
    rating_list1 =[]
    detail_list1 =[]
    director_list1 =[]

    for element in sorted_similar_movies:
                
        # s = get_title(element[0])
        # idx = element[0]
        # s = df[df.index == index]["title"].values[0]
        # r = df[df.index == index]["vote_average"].values[0]
        # idx = df[df.index == index]["index"].values[0]
        
        movie_title = title[element[0]]
        movie_rating = vote_average[element[0]]
        movie_dir = director[element[0]]

        title_list1.append(movie_title)
        rating_list1.append(movie_rating)
        director_list1.append(movie_dir)
        detail_list1.append(element[0])
 
        # title_list1[j]=s
        # rating_list1[j]=r
        # detail_list1[j]=idx

        j=j+1 
        i=i+1
        if i>=10:
            break
                
    return (title_list1, rating_list1, detail_list1, director_list1)

# ***************************************
def show_director(dir):

    def features(director):
        combining = []
        for i in range(0, len(director)):
            combining.append(director[i])
        return combining
    combining = features(director)

    cm = CountVectorizer().fit_transform(combining)
    cs = cosine_similarity(cm)

    try:
        movie_index = director.index(dir)
    except:
        return['Sorry! The movie you requested is not in our database. Please check the spelling or try with other movies!'], ['¯\_(ツ)_/¯'], []

    similar_movies = list(enumerate(cs[movie_index]))
        
    sorted_similar_movies = sorted(similar_movies,key = lambda x:x[1], reverse = True)      
                    
    i=0
    j=0

    title_list1 =[]   
    rating_list1 =[]
    detail_list1 =[]
    genre_list1 =[]

    for element in sorted_similar_movies:
        
        movie_title = title[element[0]]
        movie_rating = vote_average[element[0]]
        movie_genre = genre[element[0]]

        title_list1.append(movie_title)
        rating_list1.append(movie_rating)
        genre_list1.append(movie_genre)
        detail_list1.append(element[0])

        j=j+1 
        i=i+1
        if i>=5:
            break
                
    return (title_list1, rating_list1, detail_list1, genre_list1)

# ************************************

# 

def show_genre(gen):

    def features(genre):
        combining = []
        for i in range(0, len(genre)):
            combining.append(genre[i])
        return combining
    combining = features(genre)

    cm = CountVectorizer().fit_transform(combining)
    cs = cosine_similarity(cm)

    try:
        movie_index = genre.index(gen)
    except:
        return['Sorry! The movie you requested is not in our database. Please check the spelling or try with other movies!'], ['¯\_(ツ)_/¯'], []

    similar_movies = list(enumerate(cs[movie_index]))
        
    sorted_similar_movies = sorted(similar_movies,key = lambda x:x[1], reverse = True)      
                    
    i=0
    j=0

    title_list1 =[]   
    rating_list1 =[]
    detail_list1 =[]

    for element in sorted_similar_movies:
        
        movie_title = title[element[0]]
        movie_rating = vote_average[element[0]]

        title_list1.append(movie_title)
        rating_list1.append(movie_rating)
        detail_list1.append(element[0])

        j=j+1 
        i=i+1
        if i>=5:
            break
                
    return (title_list1, rating_list1, detail_list1)

# 

def send_detail(index):
    t = title[index]
    d = director[index]
    r = vote_average[index]
    o = overview[index]
    return (t, d, r, o)

# ************************************************* WEIGHTED AVERAGE *********************************************************************************

def top(choice):
    # res = 0
    # v = df['vote_count'] 
    # R = df['vote_average'] 
    # C = df['vote_average'].mean() 
    # m = df['vote_count'].quantile(0.70) 

    # res = ((R*v)+ (C*m))/(v+m)

    # df['weighted_average'] = res

    # movie_sorted_ranking=sorted(weighted_average,ascending=False)
    # movie_sorted_ranking=sorted(weighted_average,reverse=True)

    # title = movie_sorted_ranking['title'].head(choice)
    # ratings = movie_sorted_ranking['vote_average'].head(choice)

    # list3 = title.values.tolist()
    # list4 = ratings.values.tolist()

    # String list ot int list

    list5 = []
    list6 = []

    list1 = weighted_average
    list2 = title

    zipped = zip(list1, list2)

    res = sorted(zipped, key=operator.itemgetter(0), reverse=True)

    list3, list4 = [list(x) for x in zip(*res)]

    for i in range(choice):
        # print(list3[i], list4[i])
        list5.append(list4[i])
        list6.append(list3[i])
        i+=1
    
    return list5, list6
        

# ***************************************************** RATING ************************************************************

def rate(ch1):

    # res = 0
    # v = df['vote_count'] 
    # R = df['vote_average'] 
    # C = df['vote_average'].mean() 
    # m = df['vote_count'].quantile(0.70) 

    # res = round(((R*v)+ (C*m))/(v+m),1)

    # df['weighted_average'] = res

    # movie_sorted_ranking=sorted(weighted_average,ascending=False)
    # movie_sorted_ranking = sorted(weighted_average,reverse=True)
    
    list1 = weighted_average

    list1 = [float(i) for i in list1]

    # print(res)

    list2 = title
    list5 = []
    list6 = []

    if ch1 > 7 or ch1 < 6:
        return['Sorry the rating range you are looking for is not in our dataset'],['¯\_(ツ)_/¯']

    zipped = [x for x in zip(list1, list2) if x[0] >= ch1 and x[0] <= (ch1 + 0.9)]

    res = sorted(zipped, key=operator.itemgetter(0), reverse=True)
    # print(res)

    list3, list4 = [list(x) for x in zip(*res)]

    for i in range(10):
        # print(list3[i], list4[i])
        list5.append(list4[i])
        list6.append(list3[i])
        i+=1
    
    return list5, list6
    
