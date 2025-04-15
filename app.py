# for backend
from flask import Flask, render_template, request, jsonify
# for reading csv
import pandas as pd
#Mood Extractor
from textblob import TextBlob
app = Flask(__name__)

def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0.5:
        return "Energetic"
    elif analysis.sentiment.polarity < 0:
        return "Sad"
    elif analysis.sentiment.polarity <= 0.5 and analysis.sentiment.polarity > 0:
        return "Happy"
    
    else:
        return "Neutral"

# text1=input("Enter mood")
# mood=get_sentiment(text1)

#to match song with mood
def recommend_song(mood):
    
    df = pd.read_csv("songvsmood.csv")
    df.columns = df.columns.str.strip()
    filtered_songs = df[df["mood"] == mood]
    return filtered_songs.sample(1).to_dict(orient="records")[0]
    
#convert dataframe to list of dict
# songs_list = recommend_song(mood)
# # to dict 
# songs_dict = songs_list[0]

# #to fetch song
# print(songs_dict["song_name"])
    



#for flask app

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    text = data.get("text", "")

    # Get mood from text
    mood = get_sentiment(text)

    # Get recommended song
    song = recommend_song(mood)

    return jsonify({"song": song, "mood": mood})  # Send JSON response

if __name__ == "__main__":
    app.run(debug=True)