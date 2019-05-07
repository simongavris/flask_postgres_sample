from flask import Flask
import psycopg2 as psy
import datetime
import os

con = psy.connect(
        host=os.environ.get("DBHOST", "127.0.0.1"),
        database=os.environ.get("DBNAME","test"),
        user=os.environ.get("DBUSER", "postgres"),
        password=os.environ.get("DBPASSWORD", "secret")
)

def create_table(connection):
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS requests (id serial PRIMARY KEY, request varchar);")
    connection.commit()
    cur.close()


def write_db(connection, string):
    cur = connection.cursor()
    try:
        cur.execute("INSERT INTO requests (request) VALUES ('" + string + "');")
    except:
        connection.rollback()
    connection.commit()
    cur.close()

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    write_db(con, path)
    return 'Requested path: %s' % path

if __name__ == '__main__':
    create_table(con)
    app.run(debug=True, host='0.0.0.0')

