import mysql.connector

server="localhost"
port=3306
database="studentmanagement"
username="root"
password="@Yenngan2275"

conn = mysql.connector.connect(
                host=server,
                port=port,
                database=database,
                user=username,
                password=password)

#Thêm mới một sinh viên
print("1."+"Thêm mới một sinh viên"+"-"*10)
cursor = conn.cursor()
sql="insert into student (code,name,age) values (%s,%s,%s)"
val=("sv07","Trần Duy Thanh",45)
cursor.execute(sql,val)
conn.commit()
print(cursor.rowcount," record inserted")
cursor.close()

#Thêm mới nhiều Student
print("3."+"Thêm mới nhiều Student"+"-"*10)
cursor = conn.cursor()
sql="insert into student (code,name,age) values (%s,%s,%s)"
val=[
    ("sv08","Trần Quyết Chiến",19),
    ("sv09","Hồ Thắng",22),
    ("sv10","Hoàng Hà",25),
     ]
cursor.executemany(sql,val)
conn.commit()
print(cursor.rowcount," record inserted")
cursor.close()
