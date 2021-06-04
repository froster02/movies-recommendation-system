# ************************************************* RECOMMENDATION SYSTEM *****************************************************************

from operator import index
import pandas as pd
import numpy as np
# from config import *

# ************************************************** (REVERT CHANGES) ******************************

df = pd.read_csv('new_cleaned_dataset.csv')

# id|crew|keywords|title|overview|popularity|release_date|status|tagline|vote_average|vote_count|genre|director|index|cast

# ************************************************* Cosine Similarity *******************************************************************

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def fun1_fillna(x):
    if isinstance(x, list):
        return [str(i.replace("NaN", "")) for i in x]
    else:
        if isinstance(x, str):
            return str(x.replace("NaN", ""))
        else:
            return ''

def fun2_enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

def create_similarity():
    features = ['cast', 'keywords', 'director', 'genre']

    for feature in features:
        df[feature] = df[feature].apply(fun1_fillna)
    def combined_features(row):
        return row['cast'] + " " + row['keywords'] + " " + row['director']+ " " +row['genre']

    df['combining'] = df.apply(combined_features, axis=1)

    count = CountVectorizer()
    count_matrix = count.fit_transform(df['combining'])
    cosine_sim = cosine_similarity(count_matrix)

    return df, cosine_sim
  
def show_data(movie):

    df, cosine_sim = create_similarity()

    try:
        movie_index = df.loc[df['title']==movie].index[0]
    except:
        return['Sorry! The movie you requested is not in our database. Please check the spelling or try with other movies!'], ['¯\_(ツ)_/¯']

    i = int(movie_index)

    similar_movies = list(fun2_enumerate(cosine_sim[i]))
        
    sorted_similar_movies = sorted(similar_movies,key = lambda x:x[1], reverse = True)  

    # sorted_similar_movies = sorted_similar_movies[1:11]      
                    
    i=0
    j=0

    title_list1 =[None]*10    
    rating_list1 =[None]*10
    detail_list1 =[None]*10

    for element in sorted_similar_movies:
                
        # s = get_title(element[0])
        index = element[0]
        s = df[df.index == index]["title"].values[0]
        r = df[df.index == index]["vote_average"].values[0]
        idx = df[df.index == index]["index"].values[0]
 
        title_list1[j]=s
        rating_list1[j]=r
        detail_list1[j]=idx

        j=j+1 
        i=i+1
        if i>=10:
            break
                
    return (title_list1, rating_list1, detail_list1)

def send_detail(index):
    t = df[df.index == index]["title"].values[0]
    d = df[df.index == index]["director"].values[0]
    r = df[df.index == index]["vote_average"].values[0]
    o = df[df.index == index]["overview"].values[0]
    return (t, d, r, o)

# ************************************************* WEIGHTED AVERAGE *********************************************************************************

def top(choice):
    res = 0
    v = df['vote_count'] 
    R = df['vote_average'] 
    C = df['vote_average'].mean() 
    m = df['vote_count'].quantile(0.70) 

    res = ((R*v)+ (C*m))/(v+m)

    df['weighted_average'] = res

    movie_sorted_ranking=df.sort_values('weighted_average',ascending=False)

    title = movie_sorted_ranking['title'].head(choice)
    ratings = movie_sorted_ranking['vote_average'].head(choice)

    list3 = title.values.tolist()
    list4 = ratings.values.tolist()

    return list3, list4

# ***************************************************** RATING ************************************************************

def rate(ch1):

    res = 0
    v = df['vote_count'] 
    R = df['vote_average'] 
    C = df['vote_average'].mean() 
    m = df['vote_count'].quantile(0.70) 

    res = round(((R*v)+ (C*m))/(v+m),1)

    df['weighted_average'] = res

    movie_sorted_ranking=df.sort_values('weighted_average',ascending=False)
    
    i=0
    List5 =[]    
    List6 =[]

    for element in range(0, len(movie_sorted_ranking)):
        if ((movie_sorted_ranking.iloc[element]['weighted_average'] >= ch1) and (movie_sorted_ranking.iloc[element]['weighted_average'] <= ch1 + 0.9)):
            List5.append(movie_sorted_ranking.iloc[element]['title'])
            List6.append(movie_sorted_ranking.iloc[element]['weighted_average'])

            i=i+1
            if i>=10:
                break    
    return (List5, List6)
    
# *****************************testing for mongoDB****************************