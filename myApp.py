# FLASK MODULE WORKING

from flask import Flask, render_template, request
from numpy import tile
from main import show_data, gen, top, rate

app = Flask(__name__)

# route() function of the Flask class is a decorator, which tells the application which URL should call the associated function.
@app.route('/',methods = ['GET'])
def show_index_html():
    return render_template('index.html', movies=[], ratings=[])

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

# post GENRES
@app.route('/getG', methods = ['POST'])
def show_genre():
    ch2 = request.form['gen']
    ch2 = str(ch2)
    titles,ratings = gen(ch2)
    return render_template('index.html', titles = titles, ratings=ratings)

# post SEARCH
@app.route('/send_data', methods = ['POST'])
def get_data_from_html():
        play = request.form['play']
        movies,ratings = show_data(play)
        return render_template('index.html', movies = movies, ratings=ratings)

if __name__ == '__main__':
    app.run(debug=True)
