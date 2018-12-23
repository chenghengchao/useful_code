import requests
import datetime
import os
import pathlib
from apscheduler.schedulers.blocking import BlockingScheduler


def mk_data_dir():
    current_day = datetime.datetime.now().strftime('%Y-%m-%d')
    os.mkdir("./"+current_day)
    a = pathlib.Path().joinpath(current_day)
    print(a)
    return a, current_day


def get_data():

    data_dir, current_day = mk_data_dir()
    url = 'http://ef.zhiweidata.com/index/index.do'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.9 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    res = requests.post(url, headers=headers).json()
    print(res)

    # all_event = res['allEventsInf']
    # eventProportion = res['eventProportion']
    import pandas as pd
    event_d = {'name':[], 'bdInfulence':[], 'infExponent': [], 'startTime': [], 'tags':[],
               'type': [], 'wbInfulence':[], 'wxInfulence': []}
    monthEvents = res['monthEvent']
    for e in monthEvents:
        event_d['name'].append(e['name'])
        event_d['bdInfulence'].append(e['bdInfulence'])
        event_d['infExponent'].append(e['infExponent'])
        event_d['startTime'].append(e['startTime'])
        event_d['tags'].append(e['tags'])
        event_d['type'].append(e['type'])
        event_d['wbInfulence'].append(e['wbInfulence'])
        event_d['wxInfulence'].append(e['wxInfulence'])
    event_df = pd.DataFrame(event_d)
    event_df.to_csv(data_dir.joinpath(current_day+'-data-monthEvent.csv'), encoding='utf-8', index=None)

    eventProportion = res['eventProportion']
    # eventPr_df = pd.DataFrame.from_dict(eventProportion, orient='index')
    eventPr_df = pd.DataFrame({'type':list(eventProportion.keys()), 'value': list(eventProportion.values())})
    eventPr_df.to_csv(data_dir.joinpath(current_day+'-data-eventProportion.csv'), encoding='utf-8', index=None)

    allEventsInf = res['allEventsInf']
    allEvents_df = pd.DataFrame({'type': list(allEventsInf.keys()), 'value': list(allEventsInf.values())})
    allEvents_df.to_csv(data_dir.joinpath(current_day+'-data-allEventInf.csv'), encoding='utf-8',index=None)

    topEvents = res['topEvents']
    topEvents_d = {'name':[], 'bdInfulence':[], 'infExponent': [], 'startTime': [], 'tags':[],
               'type': [], 'wbInfulence':[], 'wxInfulence': []}
    for e in topEvents:
        topEvents_d['name'].append(e['name'])
        topEvents_d['bdInfulence'].append(e['bdInfulence'])
        topEvents_d['infExponent'].append(e['infExponent'])
        topEvents_d['startTime'].append(e['startTime'])
        topEvents_d['tags'].append(e['tags'])
        topEvents_d['type'].append(e['type'])
        topEvents_d['wbInfulence'].append(e['wbInfulence'])
        topEvents_d['wxInfulence'].append(e['wxInfulence'])
    topEvents_df = pd.DataFrame(topEvents_d)
    topEvents_df.to_csv(data_dir.joinpath(current_day+'-data-topEvent.csv'), encoding='utf-8', index=None)

    eventId = []
    for e in monthEvents:
        eventId.append(e['eventId'])
    # eventId[:3]
    url = 'http://ef.zhiweidata.com/index/oneEvent.do'
    headers = {
        'Referer':'http://ef.zhiweidata.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.9 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
    }
    import time
    events = []
    one_event_dict = {'allDifferInf': [], 'classDifferInf':[], 'eventId': [], 'inf': [], 'message': [], 'name':[], 'sevenday':[], 'state':[], 'type': []}
    for i, id in enumerate(eventId):
        try:
            print(i+1)
            one_event = requests.post(url, headers=headers, data={'eventId':id}).json()
    #     one_event_df = pd.DataFrame.from_dict(one_event, orient='columns')
    #     events.append(one_event_df)
            one_event_dict['allDifferInf'].append(one_event['allDifferInf'])
            one_event_dict['classDifferInf'].append(one_event['classDifferInf'])
            one_event_dict['eventId'].append(one_event['eventId'])
            one_event_dict['inf'].append(one_event['inf'])
            one_event_dict['name'].append(one_event['name'])
            one_event_dict['sevenday'].append(one_event['sevenDay'])
            one_event_dict['message'].append(one_event['message'])
            one_event_dict['state'].append(one_event['state'])
            one_event_dict['type'].append(one_event['type'])
    #     print(one_event_dict)
            one_event_df = pd.DataFrame(one_event_dict)
            time.sleep(3)
            events.append(one_event_df)
        except:
            print(eventId[i])
            one_event = requests.post(url, headers=headers, data={'eventId':id}).json()
    #     one_event_df = pd.DataFrame.from_dict(one_event, orient='columns')
    #     events.append(one_event_df)
            one_event_dict['allDifferInf'].append(one_event['allDifferInf'])
            one_event_dict['classDifferInf'].append(one_event['classDifferInf'])
            one_event_dict['eventId'].append(one_event['eventId'])
            one_event_dict['inf'].append(one_event['inf'])
            one_event_dict['name'].append(one_event['name'])
            one_event_dict['sevenday'].append(one_event['sevenDay'])
            one_event_dict['message'].append(one_event['message'])
            one_event_dict['state'].append(one_event['state'])
            one_event_dict['type'].append(one_event['type'])
    #     print(one_event_dict)
            one_event_df = pd.DataFrame(one_event_dict)
            time.sleep(3)
            events.append(one_event_df)
            continue
    events2 = pd.concat(events)
    events2 = pd.DataFrame(one_event_dict)
    events2.to_csv(data_dir.joinpath(current_day+'-data-oneEvents.csv'), index=False, encoding='utf-8')


def main():
    scheduler = BlockingScheduler()
    print('test started')
    scheduler.add_job(get_data, 'cron',
                      day_of_week='0-6',
                      hour='17', minute='14', second='0')
    # entrance()
    scheduler.start()


if __name__ == '__main__':
    # mk_data_dir()
    main()
