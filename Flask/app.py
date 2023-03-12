import os

from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split

app = Flask(__name__,template_folder='template')


@app.route('/')
def home():
   return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/LNews')
def LNews():
    return render_template('latest_news.html')

@app.route("/TStory")
def TStory():
    return render_template('top_stories.html')


if __name__ == '__main__':
    app.run(debug=True)