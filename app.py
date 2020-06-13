from pymongo import MongoClient           # pymongo 임포트
from flask import Flask, render_template
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta                      # dbsparta 생성


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/mapprac')
def mapprac():
    return render_template('mapprac.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
