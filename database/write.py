# 数据库内容导入
import pandas
import bcrypt
import sys
sys.path.insert(0,'..')
import connect
import mysql.connector


def getCursor():
    global dbconn
    global connection
    connection = mysql.connector.connect(user=connect.user, \
    password=connect.dbpw, host=connect.host, \
    database=connect.db, autocommit=True)
    dbconn = connection.cursor()
    return dbconn

# insert data to database
def insert(sql, parameters):
    connection = getCursor()
    connection.execute(sql, parameters)
    return connection.lastrowid

poems = pandas.read_csv('poems.csv')
for index, row in poems.iterrows():
    sql = """
        INSERT INTO poems (title, author, poem_text)
        VALUES
        (%s, %s, %s)
    """
    parameters = (row['title'], row['author'], row['poembr'])
    insert(sql, parameters)