import mysql.connector

mysql_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '0000', 
    'database': 'your_database'
}

conn = mysql.connector.connect(**mysql_config) ## '**딕셔너리'는 딕셔너리 언패킹 파이썬 문법(d = {a=1, b=2} -> **d = (1, 2))
cursor = conn.cursor()