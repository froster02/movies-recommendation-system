# ************************************************* RECOMMENDATION SYSTEM *****************************************************************

import pandas as pd
import numpy as np

df = pd.read_csv('/Users/arushnaudiyal/Desktop/testing-movies/Dataset/cleaned_dataset.csv')

merged = df

# ************************************************* Cosine Similarity *******************************************************************

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_title(index):
    return df[df.index == index]["title"].values[0]

def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        #Check if director exists. If not, return empty string
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''

def get_ratings(index):
    return df[df.index == index]["vote_average"].values[0]

def create_similarity():
    features = ['cast', 'director', 'genre', 'keywords']

    for feature in features:
        # df[feature] = df[feature].fillna('')
        df[feature] = df[feature].apply(clean_data)
    def combined_features(row):
        # return ' '.join(row['cast']) + ' ' + row['genre'] + ' ' + ' '.join(row['title'])
        return row['cast']+" "+row['genre']+" "+row['title']+row['keywords']

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

    similar_movies = list(enumerate(cosine_sim[i]))
        
    sorted_similar_movies = sorted(similar_movies,key = lambda x:x[1], reverse = True)  

    sorted_similar_movies = sorted_similar_movies[1:11]      
                    
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
df1 = df
def gen(ch2):

    df1 = df.loc[df['genre']==ch2].index[0]

    v = df1['vote_count']
    r = df1['vote_average']
    C = r.mean()
    m = v.quantile(0.95)
    
    qualified = df1[(v >= m) & (v.notnull()) & (r.notnull())][['title', 'vote_count', 'vote_average']]
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
