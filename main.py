# ************************************************* RECOMMENDATION SYSTEM *****************************************************************

import operator
from re import L
from pymongo import ASCENDING
from config import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
  
def show_data(movie):

    def features(director, keywords, cast, genre):
        combining = []
        for i in range(0, len(director)):
            combining.append(director[i] + ' ' + keywords[i] + ' ' + cast[i] + ' ' + genre[i])
        return combining
    combining = features(director, keywords, cast, genre)

    cm = CountVectorizer().fit_transform(combining)
    cs = cosine_similarity(cm)

    try:
        movie_index = title.index(movie)
    except:
        return['Sorry! The movie you requested is not in our database. Please check the spelling or try with other movies!'], ['¯\_(ツ)_/¯'], [], []

    similar_movies = list(enumerate(cs[movie_index]))
        
    sorted_similar_movies = sorted(similar_movies,key = lambda x:x[1], reverse = True)  

    sorted_similar_movies = sorted_similar_movies[1:11]      
                    
    i=0
    j=0

    title_list1 =[]   
    rating_list1 =[]
    detail_list1 =[]
    director_list1 =[]

    for element in sorted_similar_movies:
        
        movie_title = title[element[0]]
        movie_rating = vote_average[element[0]]
        movie_dir = director[element[0]]

        title_list1.append(movie_title)
        rating_list1.append(movie_rating)
        director_list1.append(movie_dir)
        detail_list1.append(element[0])

        j=j+1 
        i=i+1
        if i>=10:
            break
                
    return (title_list1, rating_list1, detail_list1, director_list1)

# *************************************** GET DIRECTOR ************************************************

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
        return['Sorry! The movie you requested is not in our database. Please check the spelling or try with other movies!'], ['¯\_(ツ)_/¯'], [],[]

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

# ******************************************* GET GENRE ************************************************

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
        return['Sorry! The movie you requested is not in our database. Please check the spelling or try with other movies!'], ['¯\_(ツ)_/¯'], [], []

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
        movie_dir = genre[element[0]]

        title_list1.append(movie_title)
        rating_list1.append(movie_rating)
        detail_list1.append(element[0])
        genre_list1.append(movie_dir)

        j=j+1 
        i=i+1
        if i>=5:
            break
                
    return (title_list1, rating_list1, detail_list1, genre_list1)

# 

def send_detail(index):
    t = title[index]
    d = director[index]
    r = vote_average[index]
    o = overview[index]
    return (t, d, r, o)

# ************************************************* WEIGHTED AVERAGE *********************************************************************************

def top(choice):

    list5 = []
    list6 = []

    list1 = weighted_average
    list2 = title

    zipped = zip(list1, list2)

    res = sorted(zipped, key=operator.itemgetter(0), reverse=True)

    list3, list4 = [list(x) for x in zip(*res)]

    for i in range(choice):
        list5.append(list4[i])
        list6.append(list3[i])
        i+=1
    
    return list5, list6
        

# ***************************************************** RATING ************************************************************

def rate(ch1):
    
    list1 = weighted_average

    list1 = [float(i) for i in list1]

    list2 = title
    list5 = []
    list6 = []

    if ch1 > 7 or ch1 < 6:
        return['Sorry the rating range you are looking for is not in our dataset'],['¯\_(ツ)_/¯']

    zipped = [x for x in zip(list1, list2) if x[0] >= ch1 and x[0] <= (ch1 + 0.9)]

    res = sorted(zipped, key=operator.itemgetter(0), reverse=True)

    list3, list4 = [list(x) for x in zip(*res)]

    for i in range(10):
        list5.append(list4[i])
        list6.append(list3[i])
        i+=1
    
    return list5, list6
    
# ************************************  FLASK MODULE WORKING    ******************************************

from flask import Flask, render_template, request
from numpy import tile
from main import show_data, top, rate, send_detail, show_director, show_genre

app = Flask(__name__)

# route() function of the Flask class is a decorator, which tells the application which URL should call the associated function.
@app.route('/',methods = ['GET'])
def show_index_html():
    return render_template('index.html')

# post SEARCH
@app.route('/send_data', methods = ['POST'])
def get_data_from_html():
        play = request.form['play']
        movies,ratings,details,genres = show_data(play)
        return render_template('searchOnly.html', movies = movies, ratings=ratings, details=details, genres=genres)

# post DETAILS
@app.route('/send_detail', methods = ['POST'])
def send_details():
        detail_btn = request.form['detail_btn']
        detail_btn = int(detail_btn)
        t, o, r, d = send_detail(detail_btn)
        return render_template('details.html',t=t,o=o,r=r,d=d)

# post HITS
@app.route('/get_top', methods = ['POST'])
def show_top_movies():
    choice = request.form['top']
    choice = int(choice)
    titles,ratings = top(choice)
    return render_template('index.html', titles = titles, ratings=ratings)

# post RATINGS
@app.route('/get_rate', methods = ['POST'])
def show_ratings():
    ch1 = request.form['rate']
    ch1 = float(ch1)
    titles,ratings = rate(ch1)
    return render_template('index.html', titles = titles, ratings=ratings)

# post DIRECTOR
@app.route('/send_director', methods = ['POST'])
def show_dir():
        dir = request.form['dir']
        movies,ratings,details,genres = show_director(dir)
        return render_template('SearchResult.html', movies = movies, ratings=ratings, details=details, genres=genres)

# post GENRE
@app.route('/send_genre', methods = ['POST'])
def show_gen():
        gen = request.form['gen']
        movies,ratings,details, genres= show_genre(gen)
        return render_template('SearchResult.html', movies = movies, ratings=ratings, details=details, genres=genres)

@app.route('/post', methods=['POST'])
def cool_form():
    return render_template('index.html')

@app.route('/browse', methods=['POST'])
def browse():
    return render_template('browseMore.html')

if __name__ == '__main__':
    app.run(debug=True)
