from flask import Flask, render_template, redirect, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
Scss(app=app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app=app)

class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Integer, default = 0)
    created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"Task {self.id}" 

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        currentTask = request.form['content']
        newTask = MyTask(content=currentTask)
        try:
            db.session.add(newTask)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"ERROR {e}")
            return f"ERROE {e}"
    else:
        tasks = MyTask.query.order_by(MyTask.created).all()
        return render_template("index.html", tasks=tasks)
    
@app.route("/delete/<int:id>")

def delete(id:int):
    delete_task = MyTask.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"ERROR {e}"
    

@app.route("/update/<int:id>", methods = ["GET", "POST"])

def edit(id:int):
    edit_task = MyTask.query.get_or_404(id)
    if request.method == "POST":
        edit_task.content = request.form['content']
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"ERROR {e}"
    else:
        return render_template("edit.html", task=edit_task)


if __name__ in "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)