# section 12-1
# 파이썬 데이터베이스 연동 (SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

print(sqlite3.version )
print(sqlite3.sqlite_version)

now = datetime.datetime.now()
print(now)
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)

# DB 생성 & Auto Commit (Rollback)
conn = sqlite3.connect('C:/PYTHON_BASIC/learn/resource/database.db', isolation_level = None)

# Cursor
c = conn.cursor()
print(type(c))

# 테이블 생성(data type : TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

# 데이터 삽입
#c.execute("INSERT INTO users VALUES(1, 'LEE', 'chang2595@naver.com', '010-5265-2595','empty', ?)",(nowDatetime,) )
#c.execute("INSERT INTO users(id, username, email,phone,website,regdate) VALUES (?,?,?,?,?,?)",              (2, 'park', 'park@com', '010-~','park.com', nowDatetime))
# 위에 주석 처리 안하면 id INTEGER PRIMARY KEY --> primary key 이기때문에
# 실행할 때마다 계속 들어갈수가 없음

# Many 삽입 (튜플, 리스트)
userList = (
    (3,'lee','l33@','010','lee.com',nowDatetime),
    (4,'cho','cho@','010','cho.com',nowDatetime),
    (5,'lim','lim@','010','lim.com',nowDatetime)
)
# 요로코롬 한방에 insert 하는게 훨 빠르다
#c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?)",userList)

# 테이블 데이터 삭제
# conn.execute("DELETE FROM users") 넣은거 싹다 삭제

# 커밋 : isolation_level = None 일 경우 자동 반영 (auto commit)
# conn.commit() 이거 쓰면 전꺼 반영
# conn.rollback() 전꺼 취소
conn.close() # 접속 해제