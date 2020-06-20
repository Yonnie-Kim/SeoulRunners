from pymongo import MongoClient           # pymongo 임포트
from flask import Flask, render_template, jsonify, request


app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta                      # dbsparta 생성


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/mapprac')
def mapprac():
    return render_template('mapprac.html')


@app.route('/mapprac2')
def mapprac2():
    return render_template('mapprac2.html')


@app.route('/tmapprac')
def tmapprac():
    return render_template('tmapprac.html')

# 경로입력
# route = {
#     "routeNo": 2,
#     "originX": 126.976462,
#     "originY": 37.575697,
#     "destinationX": 126.993741,
#     "destinationY": 37.570536,
#     "passX": 126.985383,
#     "passY": 37.576479,
#     "originName": "경복궁",
#     "destinationName": "종로3가",
# }
# db.runningroutes.insert_one(route)

# DB정보를 불러오는 json db 페이지


@app.route('/tmapdb', methods=['GET'])
def read_routes():
    # 1. DB에서 루트 정보 모두 가져오기
    routes = list(db.runningroutes.find({}, {'_id': 0}))
    # 2. 성공 여부 & 리뷰 목록 반환하기
    return jsonify({'result': 'success', 'routes': routes})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
