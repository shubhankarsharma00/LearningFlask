import MySQLdb

pwd = open('password.txt').read().strip()

def connection():
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           password=pwd,
                           db='maxentropy')
    c = conn.cursor()
    return c, conn
