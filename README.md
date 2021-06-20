# python-movie-recommendation-system

Content Based Recommender System recommends movies similar to the movie user likes.

Recommendation is based on Cosine Similarity and Weighted Average.

# Procedure

Step 1 : The dataset is used is downloaded from Kaggle.
         Dataset : https://www.kaggle.com/tmdb/tmdb-movie-metadata
       
Step 2 : Cleaned the dataset in data_preprocessing.ipynb file to remove the null values and to drop some fields.

Step 3 : Uploaded the dataset on to the [MongoDB Atlas Cluster]() client globally.

Step 4 : Fetch the data from MongoDB using NoSQL queries in Config.py file.

Step 5 : Imported the data into the main.py file to for operating.

Step 6 : Rendered the data onto the localhost using Flask framework.


### Built With

* [NoSQL]()
* [Python]()
* [Flask]()
* [HTML]()
* [CSS]()
