from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig


app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

class Target(db.Model):
    __tablename__ = 'aop_target'

    id = db.Column(db.Integer(),primary_key=True)
    DB_name = db.Column(db.VARCHAR(20))
    IP = db.Column(db.VARCHAR(15))
    OS = db.Column(db.VARCHAR(20))
    type = db.Column(db.VARCHAR(10))
    status = db.Column(db.VARCHAR(20))
    nodes = db.Column(db.Integer())
    waring = db.Column(db.Integer())

    # def __init__(self,DB_name):
    #     self.DB_name = DB_name
    #
    # def __repr__(self):
    #     return "<DB_name '{}'>".format(self.DB_name)




@app.route('/',methods=['POST','GET'])
@app.route('/<int:page>',methods=['GET'])
def list(page=1,items_num=10):
    posts=Target.query.all()
    sum = 100
    pages = int(sum/items_num) + 1
    start = page - 2
    end = page + 2
    if page <= 3:
        start = 1
        end = 5
    if page >= pages -2:
        start = pages - 5
        end = pages
    print(page,start,end)

    return render_template("index.html", posts=posts,page=page,pages=pages,list=range(start,end + 1))


if __name__ == '__main__':
    app.run()
