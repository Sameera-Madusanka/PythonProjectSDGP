from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split

app = Flask (__name__,template_folder='Front End')

@app.route("/")
def Hello():
    return render_template('index.html')
app.run(debug=True)