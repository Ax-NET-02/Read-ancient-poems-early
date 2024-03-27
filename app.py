from flask import Flask, render_template
import connect
from flask_mysqldb import MySQL
import MySQLdb.cursors


# 数据库配置
app = Flask(__name__)
app.config['SECRET_KEY'] = 'moviemagicsecretkey'

app.config['MYSQL_HOST'] = connect.host
app.config['MYSQL_USER'] = connect.user
app.config['MYSQL_PASSWORD'] = connect.dbpw
app.config['MYSQL_DB'] = connect.db
app.config['MYSQL_PORT'] = connect.port

# 初始化MySQL
mysql = MySQL(app)


@app.route("/")
def index():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    sql = """
        SELECT
            poems.poem_id, 
            poems.title, 
            poems.author, 
            poems.poem_text
        FROM
            poems
        """
    cursor.execute(sql)
    verse = cursor.fetchall()
         
    return render_template('index.html', verse=verse)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)