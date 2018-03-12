from flask import *

app = Flask(__name__)	

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/newlink')
def addnewlink():
    return render_template("newlink.html")

if __name__ == '__main__':
    app.debug=True
    app.run()
