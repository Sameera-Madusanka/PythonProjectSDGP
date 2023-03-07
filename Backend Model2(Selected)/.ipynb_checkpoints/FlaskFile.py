from flask import Flask , render_template,url_for,request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model PassiveAggressiveClassifier
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split

app = Flask(__name__)

if __name__=='__main__'
tfvect = TfidfVectorizer(stop_words='english',max_features=0.7)
loaded_model = pickle.load(open('model.pkl','rb'))
dataframe = pd.read_csv('news.csv')
x = dataframe['text']
y = dataframe['label']
x_train , x_test , y_train , y_test = train_test_split(x,y, test_size=0.2 , random_state=0)

def fake_news_det(news):
    tfid_x_train = tfvect.fit_transform(x_train)
    tfid_x_train = tfvect.transform(x_test)
    input_data = [news]
    vectorized_input_data = tfvect.transform(input_data)
    prediction = loaded_model.predict(vectorized_input_data)
    return
@app.route('/')
def home():
    return render_template('\Front End\Extension\index.html')

if __name__ == '__main__':
    app.run(debug=True)