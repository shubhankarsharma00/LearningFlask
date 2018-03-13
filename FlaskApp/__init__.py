from flask import *

app = Flask(__name__)
app.secret_key = 'T\xa0\x96W\x1cZ\x02\x81zZ\xf0\xbd\xe1"+\x05\x83\x1fc\xde]y>\xe3'

@app.route('/')
def main_page():
    return render_template("index.html")

@app.route('/submit_link', methods=['POST','GET'])
def submit_link():
    if request.method == 'POST':
        # database stuff
        flash("Link Submitted!")
        return redirect(url_for("main_page"))
    else:
        return render_template("submit.html")

if __name__ == '__main__':
    app.debug=True
    app.run()
