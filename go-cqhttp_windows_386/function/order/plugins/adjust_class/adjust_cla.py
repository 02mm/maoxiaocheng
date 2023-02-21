import pymysql
import re
import datetime

def adjust_cla(informa: list):
    #判断时间是否合理
    # 调整前的时间
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
    if p.month == Date[0] and p.day == Date[1]:
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

    # 调整后的时间
    date_2 = informa[3]
    try:
        Date_2 = int(re.findall('第(.*?)大节',date_2)[0])
    except:
        return 3
    p = datetime.datetime.now()
    if p.month == Date[0] and p.day == Date[1]:
        if Date_2 not in [1,2,3,4]:
            return 4
        if Date_2 == 1 and p.hour > 8:
            return 5
        elif Date_2 ==2 and p.hour > 10:
            return 5
        elif Date_2 ==3 and p.hour > 14:
            return 5
        elif Date_2 ==4 and p.hour > 16:
            return 5

    db = pymysql.connect(host='43.143.194.132',
                         port=3306,
                         user='maoxiaocheng',
                         passwd='yzc200212.',
                         database='maoxiaocheng')

    cursor = db.cursor()
    sql = f'select i_time from adjust_class where name = "{informa[1]}"'
    cursor.execute(sql)
    res = cursor.fetchall()
    for i in res:
        if i[0] == informa[2]:
            return 6
    sql = f'INSERT INTO adjust_class (direction,name,i_time,l_time,reason) ' \
          f'value ("{informa[0]}","{informa[1]}","{informa[2]}","{informa[3]}","{informa[4]}");'
    cursor.execute(sql)
    db.commit()
    db.close()
    return 0

