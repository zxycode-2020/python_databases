import pymysql

db = pymysql.connect("localhost", "root", "111111", "kaige")
cursor = db.cursor()

# 检查表是否存在，如果存则删除
#建表
sql = 'create table bandcard(id int auto_increment primary key, money int not null)'
cursor.execute(sql)


cursor.close()
db.close()

