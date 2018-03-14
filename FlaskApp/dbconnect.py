import MySQLdb

pwd = "brownie" #open('password.txt').read().strip()

def connection():
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd=pwd,
                           db='maxentropy')
    c = conn.cursor()
    return c, conn
