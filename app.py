from flask import Flask, render_template, request
from db_saver import *
from flask_sqlalchemy import SQLAlchemy
from parser_web import *

app = Flask("여기로가잡!")
# db=SQLAlchemy(app)

#메인화면
@app.route('/')
def home():
    jobs = select_all()
    return render_template("home.html", jobs=jobs)

#검색페이지
@app.route('/search', methods = ['GET', 'POST'])
def search():
    keyword = request.args.get("keyword")
    jobs_list = select_all()
    index_list= search_keyword(keyword)
    return render_template('search.html', index_list = index_list, keyword=keyword, jobs=jobs_list)
    
#세부화면페이지
@app.route('/detail', methods = ['GET', 'POST'])
def detail():
    jobs=select_all()
    return render_template('detail.html', jobs=jobs)