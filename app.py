import mysql.connector
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    db_init()
    return "<h1>Hello, Flask !</h1>"


def db_init():
    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="secret")

    cursor = mydb.cursor()

    cursor.execute("DROP DATABASE IF EXISTS stock")
    cursor.execute("CREATE DATABASE stock")
    cursor.close()

    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="secret",
        database="stock")

    cursor = mydb.cursor()

    cursor.execute("DROP TABLE IF EXISTS products")
    cursor.execute("CREATE TABLE products (name VARCHAR(255),description VARCHAR(255))")
    cursor.close()
    return 'init database'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
