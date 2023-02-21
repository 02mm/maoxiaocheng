import flask
from flask import Flask,request
import pymysql
from Excel_download import data_download

app = Flask(__name__)


@app.route('/')
def leave():  # put application's code here
    # 连接数据库
    db = pymysql.connect(host='43.143.194.132',
                         port=3306,
                         user='maoxiaocheng',
                         passwd='yzc200212.',
                         database='maoxiaocheng')
    # 创建游标对象
    cursor = db.cursor()
    #取出leave_seven表中所有数据
    sql = 'select * from leave_from;'
    cursor.execute(sql)
    respon = cursor.fetchall()
    db.close()
    ai_data = []
    java_data = []
    html_data =[]
    cpu_data = []
    design_data = []
    secre_data =[]
    for p in range(len(respon)):
        dict = {}
        dict['name'] = respon[p][1]
        dict['date'] = respon[p][2]
        dict['reason'] = respon[p][3]
        if respon[p][0] == '人工智能':
            ai_data.append(dict)
        elif respon[p][0] == 'Java':
            java_data.append(dict)
        elif respon[p][0] == '全栈':
            html_data.append(dict)
        elif respon[p][0] == 'CPU&OS':
            cpu_data.append(dict)
        elif respon[p][0] == '设计':
            design_data.append(dict)
        elif respon[p][0] == '秘书处':
            secre_data.append(dict)
    for i in range(len(ai_data)):
        ai_data[i]['id'] = i+1
    for i in range(len(java_data)):
        java_data[i]['id'] = i+1
    for i in range(len(html_data)):
        html_data[i]['id'] = i+1
    for i in range(len(cpu_data)):
        cpu_data[i]['id'] = i+1
    for i in range(len(design_data)):
        design_data[i]['id'] = i+1
    for i in range(len(secre_data)):
        secre_data[i]['id'] = i+1
    data = {'ai_data':ai_data,'java_data':java_data,'html_data':html_data,'cpu_data':cpu_data,'design_data':design_data,'secre_data':secre_data}
    return flask.render_template('leave_seven.html',data=data)

@app.route('/adjust')
def adjust():  # put application's code here
    # 连接数据库
    db = pymysql.connect(host='43.143.194.132',
                         port=3306,
                         user='maoxiaocheng',
                         passwd='yzc200212.',
                         database='maoxiaocheng')
    # 创建游标对象
    cursor = db.cursor()
    #取出leave_seven表中所有数据
    sql = 'select * from adjust_class;'
    cursor.execute(sql)
    respon = cursor.fetchall()
    db.close()
    ai_data = []
    java_data = []
    html_data =[]
    cpu_data = []
    design_data = []
    secre_data =[]
    for p in range(len(respon)):
        dict = {}
        dict['name'] = respon[p][1]
        dict['i_date'] = respon[p][2]
        dict['l_date'] = respon[p][3]
        dict['reason'] = respon[p][4]
        if respon[p][0] == '人工智能':
            ai_data.append(dict)
        elif respon[p][0] == 'Java':
            java_data.append(dict)
        elif respon[p][0] == '全栈':
            html_data.append(dict)
        elif respon[p][0] == 'CPU&OS':
            cpu_data.append(dict)
        elif respon[p][0] == '设计':
            design_data.append(dict)
        elif respon[p][0] == '秘书处':
            secre_data.append(dict)
    for i in range(len(ai_data)):
        ai_data[i]['id'] = i+1
    for i in range(len(java_data)):
        java_data[i]['id'] = i+1
    for i in range(len(html_data)):
        html_data[i]['id'] = i+1
    for i in range(len(cpu_data)):
        cpu_data[i]['id'] = i+1
    for i in range(len(design_data)):
        design_data[i]['id'] = i+1
    for i in range(len(secre_data)):
        secre_data[i]['id'] = i+1
    data = {'ai_data':ai_data,'java_data':java_data,'html_data':html_data,'cpu_data':cpu_data,'design_data':design_data,'secre_data':secre_data}
    return flask.render_template('adjust_seven.html',data=data)


@app.route('/excel_download')
def down_load():
    direction = request.args.get('dir')
    dict = {'all':'','ai':'人工智能','java':'Java','html':'全栈','cup':'CPU&OS','desgin':'设计','serce':'秘书处'}
    link = data_download(dict[direction])
    return flask.send_file(link)


if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=5000)
