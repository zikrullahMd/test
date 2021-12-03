from types import MethodType
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
db = SQLAlchemy(app);

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)
    time = db.Column(db.DateTime, default= datetime.datetime.now)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route("/", methods=['GET','POST'])
def main():
    if request.method=='POST':
        tit = request.form['title']
        des = request.form['desc']
        todo = Todo(title=tit,description=des)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    print(allTodo)
    return render_template('index.html',allTodo=allTodo)

@app.route("/delete/<int:sno>")
def delete(sno):
    allTodo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(allTodo)
    db.session.commit()
    return redirect("/")

@app.route("/update")
def update():
    
    return 'this is showing'

if __name__ == "__main__":
    app.run(debug=True)