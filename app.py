from flask import Flask, render_template, request
from recommender import recommend_similar_songs  # Import your recommendation function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html', recommended_songs=[])

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.form['user_input']
    recommended_songs = recommend_similar_songs(user_input)
    return render_template('homepage.html', recommended_songs=recommended_songs)

if __name__ == '__main__':
    app.run(debug=True)
