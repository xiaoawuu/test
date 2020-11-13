
def insertData(db,cursor,tablename,*key,**kwargs):# *key返回的是元组(),**返回的是字典
    values = []
    for value in kwargs.values():
        values.append(value)
    print(tuple(values))
    sql = 'insert into {} {}'.format(tablename,key).replace("'","")+' VALUES {}'.format(tuple(values))
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        print("成功添加数据")
        print("插入数据的ID：",cursor.lastrowid)
    except Exception as e:
        print(e)
        db.rollback()

