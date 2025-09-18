import pymysql
from dotenv import load_dotenv
import os
load_dotenv()
'''conn = pymysql.connect(
    host = os.getenv('127.0.0.1'),
    user = os.getenv('root'),
    password = os.getenv('root1234'),
    database = os.getenv('shopdb')
)'''

conn = pymysql.connect(
    host = os.getenv('DB_HOST'),
    user = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD'),
    database = os.getenv('DB_NAME')
)
print("DB 연결 성공")
conn.close()

