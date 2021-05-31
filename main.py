# ************************************************* RECOMMENDATION SYSTEM *****************************************************************

# IMPORT PYTHON LIBRARIES
import pandas as pd
import numpy as np
import math
from ast import literal_eval

# READ THE DATA FROM CSV FILE   
# ds1 = pd.read_csv('/Users/arushnaudiyal/Desktop/testing-movies/Dataset/tmdb_5000_credits.csv')
# ds2 = pd.read_csv('/Users/arushnaudiyal/Desktop/testing-movies/Dataset/tmdb_5000_movies.csv')
df = pd.read_csv('/Users/arushnaudiyal/Desktop/testing-movies/Dataset/cleaned_dataset.csv')

# CLEANING DATASET 
# ds1 = ds1.rename(index=str, columns={"movie_id" : "id"})

# merged = ds1.merge(ds2, on='id')

# merged = merged.drop(columns=['budget','homepage','original_language','title_x','production_companies','production_countries','release_date','revenue','runtime','spoken_languages','tagline','title_y'])

# merged = merged.rename(index=str, columns={"original_title" : "title"})

# features = ['cast', 'crew', 'keywords', 'genres']
# for feature in features:
#     merged[feature] = merged[feature].apply(literal_eval)

# def get_director(x):
#     for i in x:
#         if i['job'] == 'Director':
#             return i['name']
#     return np.nan

# def get_list(x):
#     if isinstance(x, list):
#         names = [i['name'] for i in x]
#         if len(names) > 3:
#             names = names[:3]
#         return names
#     return []

# merged['director'] = merged['crew'].apply(get_director)

# features = ['cast', 'keywords', 'genres']
# for feature in features:
#     merged[feature] = merged[feature].apply(get_list)

# merged['index'] = range(0, len(merged))

merged = df


# ************************************************* Cosine Similarity *******************************************************************

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_title(index):
    # for i in range(0, len(df)):
    #   if(df.iloc[i]["index"]==index):
    #     t = df.iloc[i]["title"]
    # return t
    return df[df.index == index]["title"].values[0]

    # FETH THE VALUES OF RATINGS FROM INDEX
def get_ratings(index):
    # for i in range(0, len(df)):
    #   if(df.iloc[i]["index"]==index):
    #     r = df.iloc[i]["vote_average"]
    # return r
    return df[df.index == index]["vote_average"].values[0]

    # FETH THE VALUES OF INDEX FROM TITLE
# def get_index(title):
#     for i in range(0,len(merged)):
#         if(merged.iloc[i]["title"]==title):
#             index=merged.iloc[i]["index"]
#     return index

def create_similarity():
# Apply clean_data function to your features.
    features = ['cast', 'title', 'director', 'genre']

    for feature in features:
        # merged[feature] = merged[feature].apply(clean_data)
        df[feature] = df[feature].fillna('')
    def combined_features(row):
        # return ' '.join(row['keywords']) + ' ' + ' '.join(row['cast']) + ' ' + row['director'] + ' ' + ' '.join(row['genre'])
        return ' '.join(row['title']) + ' ' + ' '.join(row['cast']) + ' ' + row['director'] + ' ' + ' '.join(row['genre'])
        # return row['keywords']+" "+row['cast']+" "+row['genre']+" "+row['title']

    df['combining'] = df.apply(combined_features, axis=1)

    count = CountVectorizer()
    count_matrix = count.fit_transform(df['combining'])

    cosine_sim = cosine_similarity(count_matrix)
    return df, cosine_sim
  
def show_data(movie):

    df, cosine_sim = create_similarity()

    # liked_movie = movie        
    # movie_index = get_index(liked_movie)

    try:
        movie_index = df.loc[df['title']==movie].index[0]
    except:
        return['Sorry! The movie you requested is not in our database. Please check the spelling or try with other movies!'], ['¯\_(ツ)_/¯']

    i = int(movie_index)

        # Give index to values and then typecase to list
    similar_movies = list(enumerate(cosine_sim[i]))
        
        # sorted list of the specified iterable object
    sorted_similar_movies = sorted(similar_movies,key = lambda x:x[1], reverse = True)        
                    
    i=0
    j=0
    List1 =[None]*10    
    List2 =[None]*10

    for element in sorted_similar_movies:
                
        s = get_title(element[0])
        r = get_ratings(element[0])
                
        List1[j]=s
        List2[j]=r

        j=j+1
            
        i=i+1
        if i>=10:
            break
                
    return (List1, List2)

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


#****************************************************** GENRES ******************************************************************************

def gen(ch2):

    merged['genres'] = merged['genres'].fillna('[]').apply(literal_eval).apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])

    s = merged.apply(lambda x: pd.Series(x['genres']),axis=1).stack().reset_index(level=1, drop=True)
    s.name = 'genre'
    gen_md = merged.drop('genres', axis=1).join(s)

    df1 = gen_md[gen_md['genre'] == ch2]

    v = df1['vote_count']
    r = df1['vote_average']
    C = r.mean()
    m = v.quantile(0.95)
    
    qualified = df1[(v >= m) & (v.notnull()) & (r.notnull())][['title', 'vote_count', 'vote_average', 'popularity']]
    qualified['vote_count'] = qualified['vote_count'].astype('int')
    qualified['vote_average'] = qualified['vote_average'].astype('int')
    
    qualified['wr'] = qualified.apply(lambda x: (x['vote_count']/(x['vote_count']+m) * x['vote_average']) + (m/(m+x['vote_count']) * C), axis=1)
    qualified = qualified.sort_values('wr', ascending=False)

    title = qualified['title'].head(ch2)
    ratings = qualified['vote_average'].head(ch2)

    list7 = title.values.tolist()
    list8 = ratings.values.tolist()

    return list7, list8
# gen('Adventure').head()
