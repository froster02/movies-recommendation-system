# FLASK MODULE WORKING

from flask import Flask, render_template, request
from numpy import tile
from main import show_data, top, rate, send_detail, show_director, show_genre

app = Flask(__name__)

# route() function of the Flask class is a decorator, which tells the application which URL should call the associated function.
@app.route('/',methods = ['GET'])
def show_index_html():
    # return render_template('index.html', movies=[], ratings=[])
    return render_template('index.html')

# post SEARCH
@app.route('/send_data', methods = ['POST'])
def get_data_from_html():
        play = request.form['play']
        movies,ratings,details,genres = show_data(play)
        return render_template('SearchResult.html', movies = movies, ratings=ratings, details=details, genres=genres)

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
        movies,ratings,details = show_genre(gen)
        return render_template('SearchResult.html', movies = movies, ratings=ratings, details=details)

@app.route('/post', methods=['POST'])
def cool_form():
    return render_template('index.html')

@app.route('/browse', methods=['POST'])
def browse():
    return render_template('browseMore.html')

if __name__ == '__main__':
    app.run(debug=True)
