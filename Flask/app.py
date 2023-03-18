import os

from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split

app = Flask(__name__,template_folder='template')
tfvect = TfidfVectorizer(stop_words='english', max_df=0.7)
loaded_model = pickle.load(open('model_01.pkl', 'rb'))
dataframe = pd.read_csv('news_01.csv')
x = dataframe['text']
y = dataframe['label']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

def fake_news_det(news):
    tfid_x_train = tfvect.fit_transform(x_train)
    tfid_x_test = tfvect.transform(x_test)
    input_data = [news]
    vectorized_input_data = tfvect.transform(input_data)
    prediction = loaded_model.predict(vectorized_input_data)
    return prediction

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        pred = fake_news_det(message)
        print(pred)
        return render_template('index.html', prediction=pred)
    else:
        return render_template('index.html', prediction="Something went wrong")




@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/LNews')
def LNews():
    return render_template('latest_news.html')

@app.route('/TStory')
def TStory():
    return render_template('top_stories.html')

@app.route('/test')
def test():
    return render_template('query.html')



@app.route('/news1India')
def news1India():
    return render_template('Air India seals record order for almost 500 Airbus Boeing jets.html')

@app.route('/news2Paris')
def news2Paris():
    return render_template('Paris Olympics Ukrainian president Volodymyr Zelenskyy says no place for Russia at 2024 Games while invasion continues.html')

@app.route('/news3Ferrari')
def news3Ferrari():
    return render_template('Ferrari reveal their Valentine as new car launched for 2023 Formula 1 championship challenge.html')
@app.route('/news4Six')
def news4Six():
    return render_template('Six Nations 2023 England Kyle Sinckler a doubt for Wales game due to facial injury.html')
@app.route('/news5Earth')
def news5Earth():
    return render_template('Earthquake fans anti-Syrian sentiment in Turkey amid desperate conditions.html')

@app.route('/news6Newz')
def news6Newz():
    return render_template('New Zealand declares national emergency as Cyclone Gabrielle wreaks havoc.html')

@app.route('/news7Tesla')
def news7Tesla():
    return render_template('Tesla workers launch campaign to form union in New York.html')
@app.route('/news8Ben')
def news8Ben():
    return render_template('Ben Duckett will take every chance for England, while New Zealand overlook Trent Boult.html')
@app.route('/news9China')
def news9China():
    return render_template('China Xi calls for early resolution of Iran nuclear issue.html')
@app.route('/news10Leb')
def news10Leb():
    return render_template('Lebanon PM under house arrest in Saudi Arabia.html')



if __name__ == '__main__':
    app.run(debug=True)