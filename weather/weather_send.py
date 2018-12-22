#coding:utf-8
import requests
import datetime
import itchat
from apscheduler.schedulers.blocking import BlockingScheduler


def get_weather(city):
    key = 'IwKTtP7vQ5Mahn5dykDACKqKdzFUY2uT'
    # city = '北京'
    city = city
    url = 'http://api.map.baidu.com/telematics/v3/weather?location={}&output=json&ak={}'.format(city, key)
    # url = 'http://api.map.baidu.com/telematics/v2/search?q={}&region={}&output=json&ak={}'.format('饭店', city, key)
    App_secret = '7a9676bb8ceea89685eaeb9ec4c7fb4b'
    AppID = 'wx92a5fb372a254be2'

    # print(url)
    response = requests.get(url)
    weather_dict = response.json()
    # pprint.pprint(weather_dict)
    print(weather_dict['results'][0]['currentCity'])
    weather_data = weather_dict['results'][0]['weather_data']
    return weather_data


def send_message():
    server_url = "https://sc.ftqq.com/SCU36607T4fdf46b69754b0337d4138932b8290915bfe90450ed40.send"
    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    title = now_time + 'weather'
    weather_data = get_weather("北京")
    content1 = u"今日天气：" + weather_data[0]['weather'] + weather_data[0]['wind'] + weather_data[0]['temperature']
    tmpstr = u"未来三天："
    content2 = weather_data[1]['date'] + weather_data[1]['weather'] + weather_data[1]['wind'] + weather_data[1]['temperature']
    content3 = weather_data[2]['date'] + weather_data[2]['weather'] + weather_data[2]['wind'] + weather_data[2]['temperature']
    content4 = weather_data[3]['date'] + weather_data[3]['weather'] + weather_data[3]['wind'] + weather_data[3]['temperature']
    content = content1 + "\n" + tmpstr + "\n" + content2 + "\n" + content3 + "\n" + content4
    params = {
        'text': title,
        'desp': content
    }
    response = requests.get(server_url, params=params)
    if response.json()['errno'] == 0:
        print("success")
    else:
        print(response.json()['errmsg'])


def get_weather2():
    url = 'https://www.sojson.com/open/api/weather/json.shtml?city=北京'
    data={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    weather = requests.get(url, headers=data).json()
    # print weather
    if weather['status'] == 200:
        # print()
        item = weather['data']
        # return item
    else:
        print("error")
        return
    weather = item

    wendu = weather['wendu']

    content2 = weather['forecast'][0]['fx']
    content3 = weather['forecast'][0]['fl']
    content4 = weather['forecast'][0]['high']
    content5 = weather['forecast'][0]['low']
    content6 = weather['forecast'][0]['type']
    content1 = weather['forecast'][0]['notice']
    content = " 风向：" + content2 + " " + "当前温度： " + wendu + "℃" + " " + content4 + " " + content5 + " " + content6 + " 风力： " + str(content3) + " " + content1
    # print(content)
    return content


def send_msg(content):
    # weather = get_weather2()
    # content = "notice: " + weather['forecast'][0]['notice'] + "\n" + "fx: " + weather['forecast'][0]['fx'] + "\n" + "fl: " + weather['forecast'][0]['fl'] + "\n" + "high: " + weather['forecast'][0]['high'] + "\n" + "low: " + weather['forecast'][0]['low'] + "\n" + "type: "+weather['forecast'][0]['type']
    server_url = "https://sc.ftqq.com/SCU36607T4fdf46b69754b0337d4138932b8290915bfe90450ed40.send"
    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    title = now_time + ': weather'
    params = {
        'text': title,
        'desp': content
    }
    response = requests.get(server_url, params=params)
    if response.json()['errno'] == 0:
        print("发送成功")
    else:
        print(response.json()['errmsg'])
        print("发送失败")


def get_air_condition():

    # https: // www.nowapi.com / api / weather.pm25
    sign = '5d2531e10cf7955a66e27c8ee60143a6'
    AppKey = '38465'
    url = 'http://api.k780.com'
    params = {
        'app': 'weather.pm25',
        'weaid': '北京',
        'appkey': AppKey,
        'sign': sign,
        'format': 'json',
    }
    # params = urlencode(params)

    f = requests.get(url, params=params)
    nowapi_call = f.json()
    # print content
    # a_result = json.loads(nowapi_call)
    # print(nowapi_call)
    level = None
    remark = None
    if nowapi_call:
        if nowapi_call['success'] != '0':

            level = nowapi_call['result']['aqi_levnm']
            remark = nowapi_call['result']['aqi_remark']

            # print(level)
            # print(remark)
        else:
            print(nowapi_call['msgid'] + ' ' + nowapi_call['msg'])
    else:
        print('Request nowapi fail.')
    content = level + " " + remark
    return " 空气质量： " + content


def main():
    scheduler = BlockingScheduler()
    print('test started')
    scheduler.add_job(entrance, 'cron',
                      day_of_week='0-6',
                      hour='21', minute='13', second='0')
    # entrance()
    scheduler.start()


def entrance():
    friends = itchat.search_friends(name=u'hitchenghengchao')
    username = friends[0]['UserName']
    air_condition = get_air_condition()
    print(air_condition)
    weather = get_weather2()
    print(weather)
    # send_msg(air_condition+weather)
    today_t = datetime.datetime.now()#.strftime('%Y-%m-%d %H:%M:%S')
    itchat.send('Hello, ' + u'我是机器人超，现在开始播报天气: \n时间：{}\n{}\n{}'.format(today_t, air_condition, weather), toUserName=username)


@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    if msg['Text'] == u'天气':
        entrance()

if __name__ == '__main__':
    # send_message()
    # data = get_weather("北京")
    # for item in data:
    #     for k, v in item.items():
    #         print k, v
    #     # print item[]
    # print(data)
    # get_weather2()
    # send_msg()

    # main()
    itchat.auto_login()
    itchat.run()
    # entrance()
    main()


