from flask import render_template
from flask_script import Manager,Server

from AutoBeta import app,db,Target

manager = Manager(app)
manager.add_command("server",Server())

@manager.shell
def make_shell_context():
    return dict(app=app,db=db,Target=Target)

target=Target.query.get(1)
print(target.DB_name)

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    manager.run()