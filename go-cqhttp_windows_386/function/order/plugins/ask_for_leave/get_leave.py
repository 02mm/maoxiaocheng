import pymysql
import re
import datetime

def get_leave(informa: list):
    #判断时间是否合理
    print(informa)
    Date = []
    date = informa[2]
    try:
        Date.append(int(re.findall('(.*?)月',date)[0]))
        Date.append(int(re.findall('月(.*?)日',date)[0]))
        Date.append(int(re.findall('第(.*?)大节',date)[0]))
    except:
        return 3
    print(Date)
    print('\n\n\n\n')
    for i in Date:
        if i == []:
            return 3
    p = datetime.datetime.now()
    if Date[0] < p.month or Date[0] - p.month >= 2:
        return 4
    if Date[1] < p.day or Date[1] - p.day >= 2:
        return 4
    if Date[2] not in [1,2,3,4]:
        return 4
    if Date[1] == p.day and Date[2] == 1 and p.hour > 8:
        return 5
    elif Date[1] == p.day and Date[2] == 2 and p.hour > 10:
        return 5
    elif Date[1] == p.day and Date[2] == 3 and p.hour > 14:
        return 5
    elif Date[1] == p.day and Date[2] == 4 and p.hour > 16:
        return 5
    db = pymysql.connect(host='43.143.194.132',
                         port=3306,
                         user='maoxiaocheng',
                         passwd='yzc200212.',
                         database='maoxiaocheng')

    cursor = db.cursor()
    sql = f'select time from leave_from where name = "{informa[1]}"'
    cursor.execute(sql)
    res = cursor.fetchall()
    print(res)
    for i in res:
        if i[0] == informa[2]:
            return 6
    sql = f'INSERT INTO leave_from (direction,name,time,reason) ' \
          f'value ("{informa[0]}","{informa[1]}","{informa[2]}","{informa[3]}");'
    cursor.execute(sql)
    db.commit()
    db.close()
    return 0


