import pymysql
import xlwt
import time

def conn_sql():
    # 连接数据库
    db = pymysql.connect(host='43.143.194.132',
                         port=3306,
                         user='maoxiaocheng',
                         passwd='yzc200212.',
                         database='maoxiaocheng')
    return db

def data_download(direction=''):
    # 获取数据
    cursor = conn_sql().cursor()
    if direction != '':
        sql = f'select * from leave_from where direction = "{direction}"'
        cursor.execute(sql)
        data = cursor.fetchall()
        # 创建Excel表格
        book = xlwt.Workbook(encoding='utf-8', style_compression=0)
        sheet = book.add_sheet('请假人员', cell_overwrite_ok=True)
        sheet.write_merge(0, 0, 0, 2, str(direction))
        col = ('姓名', '时间', '理由')
        for i in range(3):
            sheet.write(1, i, col[i])
        for p in range(2, len(data) + 2):
            sheet.write(p, 0, data[p - 2][1])
            sheet.write(p, 1, data[p - 2][2])
            sheet.write(p, 2, data[p - 2][3])
        sql = f'select * from adjust_class where direction = "{direction}"'
        cursor.execute(sql)
        data_2 = cursor.fetchall()
        sheet_2 = book.add_sheet('调研学人员', cell_overwrite_ok=True)
        sheet_2.write_merge(0, 0, 0, 2, str(direction))
        col = ('姓名', '调前时间','调后时间', '理由')
        for i in range(4):
            sheet_2.write(1,i,col[i])
        for p in range(2, len(data_2) + 2):
            sheet_2.write(p, 0, data_2[p - 2][1])
            sheet_2.write(p, 1, data_2[p - 2][2])
            sheet_2.write(p, 2, data_2[p - 2][3])
            sheet_2.write(p, 3, data_2[p - 2][4])
        dict = {'人工智能':'ai','Java':'java','全栈':'html','CPU&OS':'cup&os','设计':'desgin','秘书处':'serce'}
        path = f'E:\桌面\Study\qq_robte\\flaskProject\Excel\\{dict[direction]}_leave_adjust({int(time.time())}).xlsx'
    else:
        sql = f'select * from leave_from'
        cursor.execute(sql)
        data = cursor.fetchall()
        # 创建Excel表格
        book = xlwt.Workbook(encoding='utf-8',style_compression=0)
        sheet = book.add_sheet('请假人员',cell_overwrite_ok=True)
        col = ('方向','姓名','时间','理由')
        for i in range(4):
            sheet.write(0,i,col[i])
        for p in range(1,len(data)+1):
            sheet.write(p, 0, data[p - 1][0])
            sheet.write(p, 1, data[p - 1][1])
            sheet.write(p, 2, data[p - 1][2])
            sheet.write(p, 3, data[p - 1][3])
        sql = f'select * from adjust_class'
        cursor.execute(sql)
        data_2 = cursor.fetchall()
        sheet_2 = book.add_sheet('调研学人员', cell_overwrite_ok=True)
        col = ('方向','姓名', '调前时间','调后时间', '理由')
        for i in range(5):
            sheet_2.write(0,i,col[i])
        for p in range(1, len(data_2) + 1):
            sheet_2.write(p, 0, data_2[p - 1][0])
            sheet_2.write(p, 1, data_2[p - 1][1])
            sheet_2.write(p, 2, data_2[p - 1][2])
            sheet_2.write(p, 3, data_2[p - 1][3])
            sheet_2.write(p, 4, data_2[p - 1][4])
        path =  f'E:\桌面\Study\qq_robte\\flaskProject\Excel\\all_leave_adjust({int(time.time())}).xlsx'
    book.save(path)
    conn_sql().close()
    print('导出成功。。。')
    return path

def main():
    print(data_download())

if __name__ == '__main__':
    main()



