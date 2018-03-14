from flask import *
from wtforms import Form
from dbconnect import connection
from MySQLdb import escape_string as esc
import gc

app = Flask(__name__)
app.secret_key = 'T\xa0\x96W\x1cZ\x02\x81zZ\xf0\xbd\xe1"+\x05\x83\x1fc\xde]y>\xe3'

@app.route('/')
def main_page():
    c, conn = connection()
    c.execute("SELECT * FROM links");
    links = c.fetchall()
    c.close()
    conn.close()
    gc.collect()
    return render_template("index.html",links=links)

@app.route('/submit_link', methods=['POST','GET'])
def submit_link():
    if request.method == 'POST':
        # database stuff
        c, conn = connection()
        title = request.form['title']
        newlink = request.form['newlink']
        c.execute("INSERT INTO links (title,link) VALUES (%s,%s)",
                  (esc(title),esc(newlink)) )
        conn.commit()
        flash("Link Submitted!")
        c.close()
        conn.close()
        gc.collect()
        return redirect(url_for("main_page"))
    else:
        return render_template("submit.html")

@app.route('/delete_link/<int:id>')
def delete(id):
    c, conn = connection()
    c.execute("DELETE FROM links where id=%s",(str(id),))
    conn.commit()
    flash("Deleted!")
    c.close()
    conn.close()
    gc.collect()
    return redirect(url_for("main_page"))

if __name__ == '__main__':
    app.debug=True
    app.run()
