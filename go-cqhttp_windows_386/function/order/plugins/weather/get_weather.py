import requests
import  xlrd2


def get_wether(city: str) -> str:
    #返回天气
    city_adcode = get_code(city)
    if city_adcode == 0:
        return '主人您好！小毛暂只支持查询地球天气。。。'
    print(city_adcode)
    url = f'https://restapi.amap.com/v3/weather/weatherInfo?key=f69823a7011d73cb2b2778391a3490f0&city={city_adcode}&output=JSON'
    response = requests.get(url)
    result = response.json()
    if int(result['count']) == 0:
        return '主人您好！您所查的城市暂无信息，QWQ...'
    res = f"主人您好！{result['lives'][0]['province']}省{result['lives'][0]['city']}现在的天气为{result['lives'][0]['weather']}。\n" \
          f"温度：{result['lives'][0]['temperature']}℃,风力：{result['lives'][0]['windpower']}，空气湿度：{result['lives'][0]['humidity']}" \
          f"\n最后一次查询时间：\n{result['lives'][0]['reporttime']}"
    if int(result['lives'][0]['temperature']) <= 0:
        res+='\n室外低温，注意保暖！'
    if int(result['lives'][0]['temperature']) >= 35:
        res+='\n室外高温，注意降暑！'
    if '雨' in result['lives'][0]['weather']:
        res+='天下雨，勤带伞！'
    return res

def get_code(city: str) ->int :
    #查询城市对应的编码
    work = xlrd2.open_workbook('E:\桌面\Study\qq机器人\go-cqhttp_windows_386\\function\order\plugins\AMap_adcode_citycode.xlsx')
    #获取工作表内容
    sheet1_content1 = work.sheet_by_index(0)
    #获取第一列内容,城市的中文名
    cityNames = sheet1_content1.col_values(0)
    # 获取第二列内容,获取所有城市的adcode
    adcodes = sheet1_content1.col_values(1)
    # 设置城市编码初始值为''
    adcode = ''
    for i in range(1,3526):
        if city in cityNames[i]:
            return int(adcodes[i])
    if adcode == '':
        return 0

async def get_weather_of_city(city: str) -> str:
    return get_wether(city)